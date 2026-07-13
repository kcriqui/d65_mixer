// build-data.mjs — regenerate the embedded BUILTIN_CATALOG / BUILTIN_CONFIGS fallbacks
// inside d65_mixer.html from catalog.json and configs.json.
//
//   node build-data.mjs
//
// catalog.json / configs.json are the source of truth. At runtime the tool fetches them
// (so a deployer customizes by just replacing those files — no HTML editing); this script
// keeps the embedded fallbacks in sync so the single file still works when opened via
// file:// or when the JSON is absent.
import { readFileSync, writeFileSync } from 'node:fs';

const catalog = JSON.parse(readFileSync('catalog.json', 'utf8'));
const configs = JSON.parse(readFileSync('configs.json', 'utf8'));
if (!Array.isArray(catalog) || !Array.isArray(configs))
  throw new Error('catalog.json and configs.json must each be a JSON array');

const fmt = arr => arr.length ? '[\n' + arr.map(o => '  ' + JSON.stringify(o)).join(',\n') + '\n]' : '[]';

const block =
`/* @gen:data — BUILTIN_CATALOG + BUILTIN_CONFIGS are generated from catalog.json / configs.json
   by build-data.mjs. Do NOT hand-edit between the markers; edit the JSON (or Export from the
   app over it), then run:  node build-data.mjs
   These are the embedded fallbacks used when the JSON can't be fetched (e.g. opened via file://). */
const BUILTIN_CATALOG = ${fmt(catalog)};
const BUILTIN_CONFIGS = ${fmt(configs)};
/* @end:gen */`;

let html = readFileSync('d65_mixer.html', 'utf8');
const genRe = /\/\* @gen:data[\s\S]*?@end:gen \*\//;
const origRe = /const mk = [\s\S]*?const BUILTIN_CATALOG = \[[\s\S]*?\n\];/;
if (genRe.test(html)) html = html.replace(genRe, block);
else if (origRe.test(html)) html = html.replace(origRe, block);
else throw new Error('Could not find the data block (@gen:data markers or the original mk/BUILTIN_CATALOG) in d65_mixer.html');

writeFileSync('d65_mixer.html', html);
console.log(`build-data: injected ${catalog.length} catalog entries + ${configs.length} shipped configs into d65_mixer.html`);
