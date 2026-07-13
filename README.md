# Laser Projector Wavelength Selection Tool

An interactive CIE 1931 tool for choosing which laser wavelengths to run in a
multi-color projector. Build a set of real lasers, hover the chromaticity diagram to
read any color's **perceived brightness** and the exact per-laser power to make it, and
shade the whole gamut by hue, achievable brightness, or the optical power each color
costs — weighted for how the beam is seen (on a surface, or aerial through clear air,
fog, or haze).

**▶ Live tool: https://kcriqui.github.io/d65_mixer/**
**· 📄 Research brief: https://kcriqui.github.io/d65_mixer/research.html**

It's a single self-contained `d65_mixer.html` — no build step, runs anywhere you can
open the file. When served over http(s) it also loads `catalog.json` and `configs.json`
(see **Deploying / customizing**); opened as a local file it falls back to copies
embedded in the HTML, so it always works standalone.

## Features

- **Laser catalog** — Coherent OPSL (Genesis MX / Taipan) in STM (single-mode) and MTM
  (multimode) variants, plus generic diode and DPSS lines, each with wavelength and beam
  specs. Editable in-app (⚙ Database) and shippable as JSON.
- **Color Probe** — hover the CIE 1931 diagram to read a color's perceived brightness
  (bar) plus the per-laser power bars and total to reproduce it at maximum brightness.
- **Three gamut views** — *Hue* (the reproducible gamut), *Brightness* (max achievable
  brightness across the gamut), and *Power* (the optical watts each color costs vs the
  installed power — so you can see that a "10 W" projector rarely emits its full rating).
- **Perceived brightness** — a relative index (PB) from a mesopic luminous-efficiency
  curve set by a dark-adaptation slider (photopic → scotopic, the Purkinje shift) plus
  cube-root compression. Not lumens; a relative brightness index.
- **Mix & Medium** — Raw ⇄ Beam-corrected power (watts scale with each beam's spot area
  at a viewing distance, with a colored-halo warning on spot-size mismatch), and a
  viewing medium: Graphics (surface, neutral), or aerial Clear air (Rayleigh ∝1/λ⁴),
  Fog (Mie, neutral), or Haze.
- **Presets & saved setups** — broad "preload" starting points (All diode + DPSS,
  All OPSL STM, All OPSL MTM); save / restore / export your own tuned setups
  (per-setup or all, as JSON). Ships with default saved setups (from `configs.json`)
  that are seeded into your editable list on first run — edit or delete them freely.
- **Editable databases** — keep your own named laser databases in the browser; the
  built-in default is read-only. Export / import as JSON.

## Deploying / customizing

The base laser database and the shipped configurations live in two JSON files, so you
can deploy your own build **without editing the HTML**:

- **`catalog.json`** — the base laser database (array of laser objects).
- **`configs.json`** — default saved setups seeded into each user's editable list on
  first run (e.g. a manufacturer's per-product presets). Users can then edit or delete
  them. An array of `{ "name": "...", "lasers": [ ... ] }`.

Served over http(s), the tool fetches these at startup — so **replacing the JSON files
is all a deployer needs to do.** Opened as a local `file://` (where browsers block
`fetch`), or when the files are absent, it falls back to copies embedded in the HTML,
so the single file still works.

Keep the embedded fallbacks in sync after editing the JSON:

```
node build-data.mjs
```

That regenerates the `BUILTIN_CATALOG` / `BUILTIN_CONFIGS` blocks inside `d65_mixer.html`
from the JSON. To preview JSON edits locally, serve the folder and open the localhost
URL — opening the file directly via `file://` shows the last-built embedded copy, not
your latest JSON:

```
python -m http.server 8000
# then open http://localhost:8000/d65_mixer.html
```

## The math

Additive mixing sums CIE 1931 2° tristimulus values per monochromatic line; the gamut is
the convex hull of the chromaticity points. The Color Probe solves the non-negative
powers that reproduce a color at maximum brightness within each laser's power cap.
Perceived brightness weights radiant watts by a mesopic luminous-efficiency curve plus a
cube-root compression (a relative index, not lumens). Beam geometry never changes the
on-axis chromaticity — only the radiant watts needed, and hence which line is limiting.

## Origin

Grew out of the original matplotlib scripts `d65_mixer.py` / `d65_mixer2.py`.
