import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.spatial import distance
from scipy.optimize import minimize_scalar

# Load CIE 1931 2° chromaticity data (CSV with columns: wavelength, x, y)
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
cie_data = np.genfromtxt(os.path.join(__location__, 'CIE_cc_1931_2deg.csv'), delimiter=",", skip_header=1)
wavelengths_full = cie_data[:, 0]
x_vals = cie_data[:, 1]
y_vals = cie_data[:, 2]

# Interpolation functions for chromaticity values
interp_x = interp1d(wavelengths_full, x_vals, bounds_error=False, fill_value="extrapolate")
interp_y = interp1d(wavelengths_full, y_vals, bounds_error=False, fill_value="extrapolate")

# Constants
target_xy = np.array([0.3127, 0.3290])  # D65 white point
power_yellow = 2.0  # 2W yellow laser
wavelength_yellow = 589
wavelength_blue = 488

# Chromaticity coordinates
xy_yellow = np.array([interp_x(wavelength_yellow), interp_y(wavelength_yellow)])
xy_blue = np.array([interp_x(wavelength_blue), interp_y(wavelength_blue)])

# Optimized mix function (ensures colinear mix)
def corrected_mix_error(r):
    mix = xy_yellow + (r / (1 + r)) * (xy_blue - xy_yellow)
    return distance.euclidean(mix, target_xy)

# Find optimal blue power ratio
res = minimize_scalar(corrected_mix_error, bounds=(0.01, 10), method='bounded')
optimal_ratio = res.x
optimal_power_blue = optimal_ratio * power_yellow
corrected_mix_point = xy_yellow + (optimal_ratio / (1 + optimal_ratio)) * (xy_blue - xy_yellow)

# Print result
print(f"🔵 488nm Blue Laser Power Needed: {optimal_power_blue:.2f} W")
print(f"🎯 Combined Chromaticity: x = {corrected_mix_point[0]:.4f}, y = {corrected_mix_point[1]:.4f}")

# Plot results
plt.figure(figsize=(8, 6))
plt.plot(x_vals, y_vals, color='gray', label='CIE 1931 Curve')
plt.fill(x_vals, y_vals, 'lightgray', alpha=0.5)

plt.scatter(*xy_yellow, color='orange', label=f'{wavelength_yellow}nm (Yellow)')
plt.scatter(*xy_blue, color='blue', label=f'{wavelength_blue}nm (Blue)')
plt.scatter(*target_xy, color='white', edgecolors='black', label='D65 White')
plt.plot([xy_yellow[0], xy_blue[0]], [xy_yellow[1], xy_blue[1]], 'k--', label='Mix Line')
plt.scatter(*corrected_mix_point, color='purple',
            label=f'Closest Mix ({optimal_power_blue:.2f}W @ {wavelength_blue}nm)')

plt.xlabel('x')
plt.ylabel('y')
plt.title(f'{wavelength_yellow}nm (2W) + {wavelength_blue}nm Blue → Closest D65 Mix')
plt.legend()
plt.grid(True)
plt.xlim(0, 0.8)
plt.ylim(0, 0.9)
plt.gca().set_facecolor('lightgray')
plt.tight_layout()
plt.show()
