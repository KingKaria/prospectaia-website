#!/usr/bin/env node
// Mojibake / encoding regression guard for the ProspectaIA static site.
//
// Scans every tracked text file for the byte-loss mojibake pattern this
// repo suffered once already (UTF-8 misread as Latin-1/Windows-1252,
// with C1 control bytes 0x80-0x9F silently dropped downstream). Exits
// non-zero the moment it finds a known-bad marker so CI or a pre-commit
// hook can block the regression before it reaches production.
//
// Usage: node scripts/check-encoding.js [--generated]
//   --generated  also fail on literal "{{" left in a file (only meaningful
//                for rendered/published output, never for these .dc.html
//                sources -- they are legitimate client-side templates
//                resolved by support.js at runtime in the browser).

const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const CHECK_GENERATED = process.argv.includes('--generated');

const IGNORE_DIRS = new Set(['.git', 'node_modules', 'dist', 'build', '.fixscripts', 'scripts']);
const TEXT_EXTS = new Set(['.html', '.htm', '.js', '.ts', '.tsx', '.jsx', '.json', '.css', '.scss', '.md', '.txt', '.xml', '.svg']);

// Known-bad multi-byte sequences, expressed as escaped codepoints so the
// literal bytes can never be re-mangled by an editor/terminal re-saving
// this file in the wrong encoding. Each is a "double-encoded UTF-8 smart
// punctuation" sequence: the original character's UTF-8 bytes were each
// read back as one Latin-1/Windows-1252 codepoint and re-saved as UTF-8.
const BAD_MARKERS = [
  { name: 'U+FFFD replacement char', re: /�/g },
  { name: 'mis-decoded right single quote', re: /â€™/g },   // â€™
  { name: 'mis-decoded left double quote', re: /â€œ/g },    // â€œ
  { name: 'mis-decoded right double quote', re: /â€/g },   // â€
  { name: 'mis-decoded en dash', re: /â€“/g },              // â€“
  { name: 'mis-decoded em dash', re: /â€”/g },              // â€”
];

// A lone capital A-tilde (U+00C3) is never a real Portuguese letter or
// word on its own -- Portuguese has no words that start with or contain
// a bare capital Ã. Its presence is the reliable fingerprint of the
// UTF-8-read-as-Latin-1 corruption this repo suffered once.
const A_TILDE = /Ã/g;

// Lowercase 'â' (U+00E2) is NOT flagged as a bare character: it is also
// a legitimate Portuguese letter on its own (câmara, âmbito, pânico,
// âncora). An earlier version of this script used a blind
// `text.includes('â')` check and it produced a false positive that
// re-corrupted an already-fixed file. Only flag it as a run of 2+ in a
// row -- the reliable fingerprint of the star-rating mojibake pattern
// ("★★★★★" -> "âââââ").
const A_CIRC_RUN = /â{2,}/g;

function walk(dir, out) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (IGNORE_DIRS.has(entry.name)) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      walk(full, out);
    } else {
      const ext = path.extname(entry.name).toLowerCase();
      if (TEXT_EXTS.has(ext) || entry.name.endsWith('.dc.html')) out.push(full);
    }
  }
}

function findAll(line, re) {
  re.lastIndex = 0;
  const out = [];
  let m;
  while ((m = re.exec(line)) !== null) {
    out.push(m.index);
    if (m[0].length === 0) re.lastIndex++;
  }
  return out;
}

function checkFile(file) {
  const text = fs.readFileSync(file, 'utf8');
  const lines = text.split('\n');
  const findings = [];

  lines.forEach((line, idx) => {
    for (const { name, re } of BAD_MARKERS) {
      for (const col of findAll(line, re)) {
        findings.push({ line: idx + 1, col: col + 1, marker: name, text: line.trim().slice(0, 120) });
      }
    }
    for (const col of findAll(line, A_TILDE)) {
      findings.push({ line: idx + 1, col: col + 1, marker: 'Ã (capital A-tilde)', text: line.trim().slice(0, 120) });
    }
    for (const col of findAll(line, A_CIRC_RUN)) {
      findings.push({ line: idx + 1, col: col + 1, marker: 'a-circumflex run (star mojibake)', text: line.trim().slice(0, 120) });
    }
    if (CHECK_GENERATED) {
      const col = line.indexOf('{{');
      if (col !== -1) {
        findings.push({ line: idx + 1, col: col + 1, marker: 'unresolved template {{ }}', text: line.trim().slice(0, 120) });
      }
    }
  });
  return findings;
}

const files = [];
walk(ROOT, files);

let total = 0;
for (const file of files) {
  const rel = path.relative(ROOT, file);
  const findings = checkFile(file);
  for (const f of findings) {
    console.error(`${rel}:${f.line}:${f.col}: [${f.marker}] ${f.text}`);
    total++;
  }
}

if (total > 0) {
  console.error(`\nEncoding check FAILED: ${total} suspicious occurrence(s) found.`);
  process.exit(1);
}
console.log(`Encoding check passed: ${files.length} files scanned, 0 issues.`);
