# D65 Laser White Mixer & Gamut Explorer

An interactive CIE 1931 tool for laser-projector color design. Build a set of real
lasers, find the blend that reads as perfect **D65 white**, and see the color
**gamut** those primaries can reproduce.

**▶ Live tool:** _enable GitHub Pages, then this becomes_ `https://<user>.github.io/d65_mixer/`

It's a single self-contained `d65_mixer.html` — no build step, no external requests —
so it runs anywhere you can open the file, including GitHub Pages.

## Features

- **Real laser catalog** — Coherent OPSL (Genesis MX / Taipan) in STM and MTM
  variants, plus generic diode and DPSS lines, each with wavelength and beam specs.
  OPSL beam figures are from Coherent datasheets; diode/DPSS and multimode
  divergence are representative estimates (flagged `est`).
- **D65 white solver** — computes the non-negative optical powers that mix to the
  D65 white point, shown max-normalized against a limiting line (in watts).
- **Gamut** — convex hull of the primaries with Rec.709 / DCI-P3 / Rec.2020 coverage.
- **Presets** — RGB diode, RGB OPSL, All STM, All MTM.
- **Best-subset finder** — fewest lines to white, widest gamut, or the best 2-laser
  pair (closest single pair to D65 when exact white isn't reachable).
- **Beam-corrected power** — a Raw ⇄ Beam-corrected toggle that scales required
  watts by each beam's spot area at a viewing distance
  (Ø = diameter + distance × divergence), for direct-view / beam-show use, with a
  colored-halo warning when spot sizes mismatch.

## The math

Additive mixing sums CIE 1931 2° tristimulus values per monochromatic line; the
gamut is the convex hull of the chromaticity points. Beam geometry never changes the
on-axis white point — only the radiant watts needed to produce it, and hence which
line is "limiting."

## Origin

Grew out of the original matplotlib scripts `d65_mixer.py` / `d65_mixer2.py`.
