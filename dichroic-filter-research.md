# Dichroic / optical-filter research — for laser beam combining

Complete raw output from four parallel web-research agents (2026-07-13), scanning commercially
available optical filters suitable for combining visible laser lines (~460–660 nm — e.g.
460/488/520/532/561/577/590/607/639 nm) onto one collinear beam using dichroics at ~45° AOI.

The distilled, machine-readable version lives in **`dichroics.json`** (used by the tool). This
file preserves the full reports, sources, and data-quality notes for future reference.

Key finding: a **standardized dichroic laser-beam-combiner family** (cut-ons 427/466/503/552/613/659,
>95 %T / >98 %R at 45°) is sold as the same design by **Edmund (86-39x)**, **Newport (DCM10–15,
$370 ea)**, and **Semrock (LaserMUX LM01-###)**. The tool's default generic efficiencies (Transmit
91 % / Reflect 95 %) are the average of the researched 45° edge-dichroic product lines.

---

## 1. Thorlabs

Method note: Thorlabs' product pages are JavaScript-rendered and blocked WebFetch; specs were
extracted from page content surfaced through search. Per-part prices are mostly not exposed that
way, so most price cells are NOT FOUND rather than guessed.

| Vendor | Part / Family | Type | Edge / band (nm) | AOI | %T (pass) | %R (reflect) | Price (USD) | Source | Notes |
|---|---|---|---|---|---|---|---|---|---|
| Thorlabs | DMLP series (DMLP425/445/463/490/505/550/560/567/605/650…) | longpass-dichroic | cut-on 425–1800; visible 425/490/505/550/567/605/650 | 45° | Tavg >90% above cut-on | Ravg >90% below cut-on | NOT FOUND (family) | objectgroup_id=3313 | Primary combiner. UV fused silica, ion-beam-sputtered hard coat, λ/4 @632 nm, 40-20 s/d. Sizes Ø½"(T)/Ø1"/Ø2"(L)/25×36 mm(R)/35×52 mm |
| Thorlabs | DMLP567 (Ø1") | longpass-dichroic | cut-on 567; reflect ≈380–550; transmit ≈584–700 | 45° | Tavg >90% | Ravg >90% | **$165.00** | thorproduct DMLP567 | Confirmed price; representative of Ø1" DMLP |
| Thorlabs | DMLP505R (25×36 mm) | longpass-dichroic | cut-on 505 | 45° | Tavg >90% | Ravg >90% | **$230.00** | objectgroup_id=3313 | Rectangular version price |
| Thorlabs | DMSP series (DMSP425/490/505/550/567/605/650…) | shortpass-dichroic | cutoff 425–1800; visible 425/490/505/550/567/605/650 | 45° | Tavg >90% below cutoff | Ravg >90% above cutoff | NOT FOUND (family) | objectgroup_id=9240 | UV fused silica hard coat, λ/4 @632 nm, low autofluorescence. Same five sizes as DMLP |
| Thorlabs | RGB combiners (RGB30HA 473/561/640; RGB50HB & RGB50HF 488/561/640; RGB46HB 488/532/640) | laser-combiner (fiber WDM) | 3 lines → 1 SM fiber; ±5 nm/port | fiber (N/A) | high (low insertion loss) | isolation ≥10 dB crosstalk | NOT FOUND | objectgroup_id=8843 | Fiber-coupled, not free-space. 100×80×10 mm; FC/PC or FC/APC |
| Thorlabs | 2-Color combiners (e.g. 488/640; RB41AP, RG45F1 561/640) | laser-combiner (fused-fiber WDM) | 2 lines → 1 common fiber | fiber (N/A) | low insertion loss | isolation >25 dB | NOT FOUND | objectgroup_id=8952 | Fiber WDM; some PM-fiber variants |
| Thorlabs | RGB1-FC | laser-combiner (free-space→fiber module) | 3-channel visible | module | NOT FOUND | NOT FOUND | NOT FOUND | thorproduct RGB1-FC | 3-Channel Visible Laser Combiner |
| Thorlabs | NF series (NF533-17/NF561-18/NF594-23/NF633-25/NF658…) | notch | CWLs 405/488/514/533/561/594/633/658/785/808/980/1064; FWHM ~17–25 | 0° | >90% avg in passbands | stopband OD >6 (T <0.0001%) | NOT FOUND | objectgroup_id=3880 | 0° AOI — edge shifts blue at 45°; usable to reflect one mid-band line but not a 45° part |
| Thorlabs | FBH series (e.g. FBH570-10) | bandpass | various CWL, FWHM ~10 nm; Ø25 mm, 3.5 mm | 0° | ≥85% at CWL | out-of-band OD4–6 | NOT FOUND | objectgroup_id=1860 | Hard-coated UV/VIS bandpass; 0° AOI |
| Thorlabs | FELH (longpass) / FESH (shortpass) edgepass | longpass / shortpass | various cut-on/cutoff | 0° | FELH >90% (FELH0350 >85%); FESH >87% | out-of-band blocked | NOT FOUND | objectgroup_id=6082 | Hard-coated edge filters — 0° AOI, not the 45° combining parts |

**Most relevant:** DMLP series (longpass, 45°) is the primary free-space combining element — reflects
below cut-on, transmits above, both >90%. Pick a cut-on between the two lines being merged (DMLP505 for
488 reflected + ≥520 transmitted; DMLP550/567 around 532/561; DMLP605 around 577–607; DMLP650 around
639). DMSP is the complementary part (transmit short, reflect long). RGB/2-color combiners are turnkey
**fiber** WDM (isolation ≥10 dB / >25 dB), not free-space.

**Sources:** objectgroup_id 3313 (DMLP), 9240 (DMSP), 8843 (RGB), 8952 (2-color), 3880 (notch),
1860 (bandpass), 6082 (edgepass) at thorlabs.com/newgrouppage9.cfm.

**Data gaps:** Only DMLP567 ($165) and DMLP505R ($230) prices confirmable — most render client-side.
Ø1" visible dichroics broadly ~$150–260. Dichroic edges are polarization-dependent at 45° (s/p differ
by tens of nm). Notch/bandpass/edgepass are 0° AOI (secondary). Group pages JS-gated → wavelength lists
representative, not guaranteed-exhaustive.

---

## 2. Edmund Optics

All specs from live Edmund Optics product/family pages. Unconfirmed fields = NOT FOUND.

| Vendor | Part / Stock # | Type | Edge / band (nm) | AOI | %T (pass) | %R (reflect) | Price (USD, qty 1) | Notes |
|---|---|---|---|---|---|---|---|---|
| Edmund | 86-392 (503nm, 25mm) | laser-combiner (longpass dichroic) | cut-on 503; reflect 473–491; transmit 514.5–647.1 | 45° | >95% | >98% | $297 | Fused silica (Corning 7980), hard sputtered, pol. insensitive |
| Edmund | 86-393 (552nm, 25mm) | laser-combiner | cut-on 552; reflect 514.5–543.5; transmit 561.4–790 | 45° | >95% | >98% | $297 | Same family |
| Edmund | 86-394 (613nm, 25mm) | laser-combiner | cut-on 613; reflect 561–594.1; transmit 632.8–790 | 45° | >95% | >98% | $297 | 60-40 SQ, 2mm thick |
| Edmund | 86-395 (659nm, 25mm) | laser-combiner | cut-on 659; reflect 632.8–647.1; transmit 671–790 | 45° | >95% | >98% | $297 | Same family |
| Edmund | 86-397 (466nm, 50mm) | laser-combiner | cut-on 466; reflect 439–457.9; transmit 473–647.1 | 45° | >95% | >98% | $720 | 50mm dia (larger = pricier) |
| Edmund | Family: 427/466/480/503/552/613/659 cut-ons | laser-combiner family | see per-part | 45° | >95% | >98% | $297–$720 | 12.5/25/50mm; LIDT 1 J/cm² @532nm 10ns |
| Edmund | 69-867 (550nm, 12.5mm) | longpass-dichroic (edge) | cut-on 550; transmit 575–1600; reflect 415–515 | 45° | >85% avg (>80% abs) | >97% avg (>95% abs) | $143 | Fused silica, hard coated, low pol. dependence |
| Edmund | 69-880 (650nm, 12.5×17.6mm) | longpass-dichroic (edge) | cut-on 650; transmit 675–1600; reflect 495–610 | 45° | >85% avg | >97% avg | $143 | λ/4 TWE |
| Edmund | Family (Dichroic Longpass) | longpass-dichroic | visible cut-ons 400–750nm | 45° | >85% avg | >97% avg | — | 8-filter kit 400–750nm (#44027) |
| Edmund | 69-178 (500nm, 12.5mm) | shortpass-dichroic (edge) | cut-off 500 (±2%); transmit 325–480; reflect 520–610 | 45° | >85% avg | >97% avg | $140 | AR on S2; hard sputtered on S1 |
| Edmund | Family (Dichroic Shortpass) | shortpass-dichroic | cut-offs 400/450/500/550/600/650/700/750 | 45° | >85% avg | >97% avg | kit $1,387 | 8-filter kit #44029 (25mm) |
| Edmund | 67-119 (532nm, 25mm) | notch (OD 4.0) | notch CWL 532; FWHM 26.6; transmit 400–700 | **0°** | 90% | >99% at CWL | $465 | Hard coated; reflects the 532 line |
| Edmund | 532nm OD 6.0 notch (e.g. 28612) | notch (OD 6.0) | CWL 532; ±2.5% | 0° | high | >99% | NOT FOUND | Deeper blocking; Raman |
| Edmund | 39-356 (532nm, 25mm, 5nm) | bandpass (laser line) | CWL 532 ±1; FWHM 5 ±1 | **0°** | >85% | ≥4.0 OD block | $360 | Hard coated line clean-up |

**Most relevant:** TECHSPEC Dichroic Laser Beam Combiners (family 14451; 86-392…86-397) — purpose-built,
45°, >95%T / >98%R at popular laser lines, pol. insensitive, fused-silica hard-sputtered. Cut-ons 427/466/
480/503/552/613/659 in 12.5/25/50mm. Reflect bands are narrow (tuned to lines, e.g. 473–491, 514.5–543.5),
so each reflects one line and transmits everything longer — the cascade topology for the 460–660 set.
Downside: not high LIDT (1 J/cm² @532nm). Also Dichroic Longpass (family 14288) / Shortpass (14198) edge
filters — general 45° edge dichroics, >85%T / >97%R, broadband, cheaper ($140–143).

**Sources:** edmundoptics.com/f/dichroic-laser-beam-combiners-8f67c2b5/14451; /p/…/28852 (503),
/p/…/28854 (613); /f/dichroic-longpass-filters/14288; /f/dichroic-shortpass-filters/14198;
/p/…/21656 (532 OD4 notch); /p/…/39632 (532 5nm bandpass).

**Data gaps:** Combiner reflect bands are narrow line-specific windows — verify each part's reflect band
covers the intended line (427/480 parts' exact bands NOT FOUND). Notch/bandpass are 0° AOI. Combiner
%T/%R are thresholds at laser lines; edge-filter %T (>85%) is pol.-averaged. Prices single-unit list
(2026-07); volume breaks exist (613nm → $234 at 26+).

---

## 3. Newport & Semrock (IDEX)

| Vendor | Part / Family | Type | Edge / Band (nm) | AOI | %T (pass) | %R (reflect) | Price (USD) | Source |
|---|---|---|---|---|---|---|---|---|
| Semrock | LM01-427-25 (LaserMUX) | laser-combiner / longpass-dichroic | 427 edge; R 372–415, T 439–647.1 | 45° (0.35%/°) | Tavg >95% (439–647.1) | Ravg >98% (372–415) | NOT FOUND (obsolete SKU) | idex-hs |
| Semrock | LM01-466-25 | laser-combiner / longpass-dichroic | 466 edge; R 439–457.9, T 473–647.1 | 45° | Tavg >95% (473–647.1) | Ravg >98% (439–457.9) | NOT FOUND | semrock / idex-hs |
| Semrock | LM01-503-25 | laser-combiner / longpass-dichroic | 503 edge; R 473–491, T 514.5–647.1 | 45° | Tavg >95%; Tabs >95% p-pol | Ravg >98%; Rabs >96% p, >99% s | NOT FOUND | ahf.de (Semrock) |
| Semrock | LM01-552-25 | laser-combiner / longpass-dichroic | 552 edge; R 514.5–543.5, T 561.4–790 | 45° | Tavg >95% (561.4–790) | Ravg >98% (514.5–543.5) | NOT FOUND (obsolete SKU) | idex-hs |
| Semrock | LM01-613-25 | laser-combiner / longpass-dichroic | 613 edge; R 561.4–594.1, T 632.8–790 | 45° | Tavg >95% (632.8–790) | Ravg >98% (561.4–594.1) | NOT FOUND | idex-hs / ahf.de |
| Semrock | LM01-659-25 | laser-combiner / longpass-dichroic | 659 edge; R 632.8–647.1, T 671–790 | 45° | Tavg >95% (671–790) | Ravg >98% (632.8–647.1) | NOT FOUND (obsolete SKU) | idex-hs |
| Semrock | Di03-R### (Laser BrightLine: R405/R488/R514/R532/R635/R660) | dichroic-beamsplitter (super-res/TIRF) | single-edge at named line | 45° | high (numeric NOT FOUND) | high at line (numeric NOT FOUND) | NOT FOUND | idex-hs / 3doptix |
| Semrock | FF###-Di03 (BrightLine epi-fluor, FF409/FF495…) | dichroic-beamsplitter (longpass) | edge at named nm | 45° | high T | high R | NOT FOUND | 3doptix |
| Semrock | NF03-532E-25 (StopLine) | notch | 532 notch, ~17 nm BW, OD >6 | ~0° | high T UV–1600 | reflects rejected line | NOT FOUND | idex-hs / semrock |
| Newport | DCM10 | longpass-dichroic combiner | cut-on 427; R 372–415, T 439–647.1 | 45° | >95% (439–647.1) | >98% (372–415) | **$370** | newport.com |
| Newport | DCM11 | longpass-dichroic combiner | cut-on 466; R 439–458, T 473–647.1 | 45° | >95% (473–647.1) | >98% (439–458) | **$370** | newport.com |
| Newport | DCM12 | longpass-dichroic combiner | cut-on 503; R 473–491, T 514.5–647.1 | 45° | >95% (514.5–647.1) | >98% (473–491) | **$370** | newport.com |
| Newport | DCM13 | longpass-dichroic combiner | cut-on 552; R 515–544, T 561.4–790 | 45° | >95% (561.4–790) | >98% (515–544) | **$370** | newport.com |
| Newport | DCM14 | longpass-dichroic combiner | cut-on 613; R 561–594, T 632.8–790 | 45° | >95% (632.8–790) | >98% (561–594) | **$370** | newport.com |
| Newport | DCM15 | longpass-dichroic combiner | cut-on 659; R 633–647, T 671–790 | 45° | >95% (671–790) | >98% (633–647) | **$370** (4-wk lead) | newport.com |
| Newport | 10SWF-400-B | shortpass filter | cut-off 400 ±2; T 325–385, reflect 420–485 | 45° | (UV pass) | high R 420–485 | NOT FOUND | newport.com |

Shared: all LM01 and DCM parts are Ø25.0 mm. LM01 = 3.5 mm mounted ring / 22 mm CA; 0.35%/° edge shift.
DCM = IBS coating, pol.-insensitive. LM01 quotes separate s/p absolute Rabs/Tabs at each laser line.

**Most relevant:** Semrock **LaserMUX (LM01-###-25)** — purpose-built longpass dichroics that reflect the
shorter line(s) and transmit everything longer, cascadable to merge N beams. Tiles the visible almost
exactly onto the line list: 427 (reflect 375/405), 466 (440/458), 503 (473/488), 552 (514.5/532/543.5),
613 (561/594), 659 (633/635/647). Ravg >98%, Tavg >95%, explicit per-line s/p specs. **Caveat: individual
LM01 SKUs flagged "obsolete" on the IDEX store**, but line still marketed/stocked by distributors; a newer
16-line LaserMUX exists. **Newport DCM10–15** is the near-identical set, IBS-coated, pol.-insensitive,
**in stock at $370 ea** — the cleanest priced path.

**Sources:** newport.com/f/dichroic-laser-beam-combiners; idex-hs.com/…/combining-or-separating-laser-beams;
ahf.de …/lasermux-dichroic-beamsplitter-473-491/F38-M03 (LM01-503 verbatim numbers);
idex-hs.com/store LM01 detail pages; idex-hs.com/…/find-the-right-dichroic-beamsplitter (Di03); NF03-532E.

**Data gaps:** Newport publishes $370 (all DCM10–15); Semrock/IDEX publish no prices (quote via
semrock@idexcorp.com or AHF / AVR Optics / Laser2000). LaserMUX SKU obsolescence — verify live availability;
Newport DCM is the in-stock priced path. Di03 exact %T/%R NOT FOUND on reachable pages (Rabs typ. >95–98%,
Tavg >90% per Semrock SearchLight, not asserted here). NF03 notches are ~0° AOI. Neither stock set has an
edge purpose-built to isolate 561 vs 577/590 finely — the 552 part reflects up to 543.5 and the 613 part
reflects 561–594 as a block, so closely-spaced yellow-orange lines need custom / Di03-class single-edge parts.

---

## 4. Other vendors (Chroma, Omega, Alluxa, Iridian, Materion, Knight, laser-show OEM)

Most are custom/quote houses; category pages are JS-rendered and part-level specs live on datasheets / RFQ.
**Alluxa** is the one publishing hard part numbers **and** prices online.

| Vendor | Part / Family | Type | Edge / band (nm) | AOI | %T | %R | Price (USD) | Note |
|---|---|---|---|---|---|---|---|---|
| Alluxa | Single-Edge Longpass Dichroic Beamsplitters — stock edges 454/494/507.5/559/560/597/604/642/681/409 nm (ULTRA at 454/494/559/560/681) | longpass-dichroic | listed edge per part | catalog dichroics typ. 45° | high (# NOT FOUND on catalog) | high (# NOT FOUND) | **$258–$392** (409/507.5/642=$258; 597/604=$277; ULTRA=$392) | Only vendor here with public part list + prices. 25.2×35.6 mm, 1.05 mm. Steep-edge, hard-coated (SIRRUS). Most directly usable line-by-line. |
| Alluxa | ULTRA dichroic beamsplitters / polychroics (custom) | longpass/shortpass/multi-edge | UV–IR, any edge | any (incl. 45°) | "ultra-high transmission" (NOT FOUND) | NOT FOUND | quote | Laser-damage-resistant; built to exact line set. |
| Alluxa | 532 / 532-1064 OD6 Notch | notch | 532 (and dual) | 45° option | NOT FOUND | OD6 block | quote | Reflects narrow band; can fold a 532 line. |
| Chroma | T520lpxr, T560lpxr (T-series "lpxr" longpass) | longpass-dichroic beamsplitter | edge = number (520, 560…) | 45° | NOT FOUND (typ. >90–95%) | NOT FOUND (typ. >95–98%) | quote / distributor | Beam steering/combining & fluorescence. 18×26×1 mm, 25 mm dia. |
| Chroma | ZT405/488/561/640rpc, ZT405/488/532/640rpc, ZT405/488/543/640rpc (RPC laser polychroics) | multi-edge dichroic-beamsplitter (laser) | reflects 405/488/561/640 (or 532) lines | 45° | NOT FOUND | high R at design lines | quote | Purpose-built multi-line laser combiner/reflector; closest catalog analog to RGB combining, tuned to specific lines. |
| Chroma | Single/multi-band dichroic beamsplitters (custom) | longpass/shortpass/multiband | any visible edge | typ. 45° | NOT FOUND | NOT FOUND | quote | "Large inventory + custom design." |
| Omega Optical | Dichroics / Beamsplitters / Mirrors (LP/SP/multiband) | dichroic + combiner | any visible edge | typ. 45° | ~100−R−(<1% scatter), dielectric | high | quote (some stock via shop) | Long heritage in dichroics; custom/quote. |
| Iridian Spectral | Beam Combiner Filters / Specialty Beam Combiner | laser-combiner (dichroic) | any 2+ visible lines (e.g. 488 + 632) | **45°** | NOT FOUND | NOT FOUND | quote | Explicitly markets "combine two beams into one" at 45°. 12.5/25 mm. Strong fit; quote-only. |
| Iridian | Dichroic longpass fluorescence filters (e.g. 409 DM) | longpass-dichroic | e.g. 409 edge | 45° | NOT FOUND | NOT FOUND | quote | Confirms visible single-edge dichroics exist as products. |
| Materion Balzers | Dichroic Beamsplitters (all-dielectric) + Splitters/Combiners | dichroic-beamsplitter / combiner | any 260–1550 nm edge | customer-spec (45° typ.) | "low-loss" (NOT FOUND) | NOT FOUND | quote-only | Explicit laser-source combiner line; narrow edge tolerances, randomly-polarized designs. |
| Asahi Spectra | Dichroic beam splitters, LP & SP families | LP/SP/dichroic-beamsplitter | UV–VIS–IR | typ. 45° | NOT FOUND | NOT FOUND | quote | Broad VIS LP/SP catalog; custom combiners on request. |
| Knight Optical | Stock Dichroic Longpass (cut-on 420–740) & Shortpass (cut-off 414–730) mirrors | LP / SP dichroic | 420–740 (LP), 414–730 (SP) | typ. 45° | NOT FOUND (dielectric) | high | stock + custom (quote) | Best non-Alluxa **stock** visible edge coverage; low fluorescence, high-power friendly. |
| Laser Components (dist.) | Dichroic mirrors / SP & LP filters | LP/SP dichroic | 248–3000 nm | 45° | NOT FOUND | high (projector-grade >99%) | quote | Reputable stock/distributor incl. Alluxa datasheets. |
| Lambda Research Optics | Dichroic Beamsplitters / Beam Combiners / Harmonic Separators (SPD/LPD/BC/HHS) | dichroic-beamsplitter / combiner | visible + laser harmonic lines | 45° | NOT FOUND | high | quote | Catalog family explicitly named "Beam Combiners." |
| Avantier / Shanghai Optics | Custom dichroic beamsplitters / mirrors | dichroic-beamsplitter | any visible edge | 45° | NOT FOUND | NOT FOUND | quote | Custom houses; build to line list. |
| Laser-show OEM (CivilLaser / Optlaser / eBay) | RGB combining dichroic mirror sets (reflect 445–473 blue, pass 520–532 green & 635–660 red); 10-packs | laser-combiner (dichroic set) | tuned to 445/450/520/638(660) | 45° | passband high (projector-grade) | R>99% at design line (vendor claim) | **cheap** (eBay 10-pack ~tens of USD) | Exactly the RGB-projector use case, but color-labeled (not per-nm), specs vendor-claimed, loose tolerances. Cheapest by far. |

**Most relevant:** (1) **Alluxa single-edge longpass dichroics** (stock, priced; edges 409/454/494/507.5/
559/560/597/604/642/681) — best balance of spec quality + purchasability + throughput. (2) **Chroma ZT-series
RPC laser polychroics** — multi-line, ideal if lines map to design lines. (3) **Iridian "Beam Combiner
Filters"** and **Materion Balzers** — explicit 45° combiners, design to exact line list, quote-only.
(4) **Knight Optical stock LP/SP** — widest non-Alluxa stock visible coverage. (5) **Laser-show OEM RGB sets**
— literal RGB hardware, far cheaper, coarse/unverified.

**Sources:** alluxa.com/optical-filters-category/dichroic-beamsplitter/single-edge/;
chroma.com/products/part/zt405-488-561-640rpc & …/parts/t560lpxr; iridian.ca/specialty-filters/beam-combiner-filters/;
materionbalzersoptics.com/…/dichroic-beamsplitters.html; omega-optical.com/beamsplitters-and-mirrors-2/;
knightoptical.com/stock/filters/dichroic-filters; asahi-spectra.com/opticalfilters/astronomy_dichroic.asp;
ebay.com/itm/264749845615; civillaser.com …products_id=402.

**Data gaps:** Quote-only (no online prices): Chroma, Omega, Iridian, Materion, Asahi, Knight, Laser
Components, Lambda, Avantier/Shanghai. Alluxa part list + prices firm/public (per-part %T/%R on individual
datasheets). Numeric %T/%R gaps on JS-rendered category pages were NOT substituted with generic figures.
Laser-show OEM specs are vendor-claimed and coarse. At 45°, polarization splits the edge (s vs p) — pick
edges with margin; Alluxa/Iridian/Materion offer unpolarized/45°-optimized designs on request.
