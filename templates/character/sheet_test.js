// Executes character_sheet.html in a real DOM and asserts its computed stats
// against the rules as merged. The sheet is hand-authored plain HTML/CSS/JS with
// no build step, so this is the only thing that checks it beyond reading it.
//
//   RUNNING IT
//
//   jsdom is the one dependency, and it is deliberately NOT vendored here - this
//   repo is markdown and stdlib-only Python, with no package.json and no
//   node_modules. Install it anywhere outside the repo and point NODE_PATH at it:
//
//       mkdir -p ~/.cache/ressam-test && cd ~/.cache/ressam-test
//       npm init -y && npm install jsdom
//       cd -
//       NODE_PATH=~/.cache/ressam-test/node_modules node templates/character/sheet_test.js
//
//   A plain `npm install jsdom` with no version pinned can resolve a release whose
//   engines field requires Node 20+ and pulls in an ESM-only transitive dependency
//   (html-encoding-sniffer -> @exodus/bytes) - under an older Node, `require('jsdom')`
//   then throws ERR_REQUIRE_ESM, which this file's catch block below reports as
//   "jsdom not found" even though npm install succeeded and the package is sitting
//   right there. Debian/Ubuntu's apt-packaged `nodejs` is commonly an old LTS (18
//   on bookworm) and can hit this. If you do: get a current LTS tarball from
//   nodejs.org and put its bin/ ahead of the system one on PATH, rather than
//   pinning an older jsdom - a plain reinstall under the newer Node has also been
//   enough to resolve a compatible version instead.
//
//   Exits 0 with a pass count, or 1 listing every failed assertion.
//
//   WHAT IT COVERS
//
//   The Tempo Pool ladder (both columns, including where they part company above
//   5), Initiative, the melee/missile damage split, Wards, Armor Penalty banding,
//   Shield Guard taking only the highest, per-weapon Attack and Parry, the Tempo
//   spend/refill tracker, localStorage persistence, and - the reason this file is
//   worth keeping - that a character saved BEFORE a rules rework still loads, with
//   its dropped/renamed fields ignored and its derived stats recomputed rather
//   than trusted. The legacy fixture below predates the Band-to-Length rename and
//   the sharp-weapon Opening-threshold deletion, on top of the older fields it
//   already covered from before the 2026-08-23 Exchange merge.
//
//   ADDING A CASE
//
//   check(label, got, want) compares as strings. Booleans go in as 'true'; a
//   querySelector that should find nothing goes in as 'null'. Dispatch input via
//   the setAttr/setSkill/setCol helpers rather than assigning .value directly -
//   the sheet recomputes on bubbled input/change events, so a bare assignment
//   changes the field and nothing else. To test a saved character, pass the save
//   object to boot(); it is seeded through jsdom's beforeParse hook because the
//   sheet reads localStorage as its script runs, and anything set afterwards is
//   already too late.

const fs = require('fs');
const path = require('path');

let JSDOM;
try {
  ({ JSDOM } = require('jsdom'));
} catch (e) {
  if (e.code === 'ERR_REQUIRE_ESM') {
    console.error('jsdom failed to load with ERR_REQUIRE_ESM - a Node version problem, not a missing install.');
    console.error('The installed jsdom pulled in an ESM-only dependency your Node (' + process.version + ') can\'t');
    console.error('require(). Get a current LTS from nodejs.org and put its bin/ ahead of the system node on');
    console.error('PATH, then reinstall jsdom under it - see this file\'s header comment for details.\n');
    console.error(e.message + '\n');
  } else {
    console.error('jsdom not found. It is not vendored in this repo on purpose - see the header of this file.\n');
    console.error('  mkdir -p ~/.cache/ressam-test && cd ~/.cache/ressam-test');
    console.error('  npm init -y && npm install jsdom');
    console.error('  cd -');
    console.error('  NODE_PATH=~/.cache/ressam-test/node_modules node templates/character/sheet_test.js');
  }
  process.exit(2);
}

const SHEET = path.join(__dirname, 'character_sheet.html');

let pass = 0, fail = 0;
const failures = [];
function check(label, got, want) {
  const ok = String(got) === String(want);
  ok ? pass++ : (fail++, failures.push(`${label}: got ${JSON.stringify(String(got))}, want ${JSON.stringify(String(want))}`));
}

function boot(seed) {
  const dom = new JSDOM(fs.readFileSync(SHEET, 'utf8'), {
    runScripts: 'dangerously',
    url: 'http://localhost/sheet.html',
    pretendToBeVisual: true,
    // localStorage has to exist BEFORE the sheet's script runs, or restore()
    // sees an empty store and the legacy-save test measures nothing.
    beforeParse(window) {
      if (seed) window.localStorage.setItem('ressam-character-sheet-v1', JSON.stringify(seed));
    },
  });
  const { document } = dom.window;
  const $ = (s) => document.querySelector(s);
  const out = (id) => document.getElementById(id).textContent.trim();
  const fire = (el, type = 'input') =>
    el.dispatchEvent(new dom.window.Event(type, { bubbles: true }));
  const setAttr = (key, v) => { const el = $(`[name="attr:${key}:base"]`); el.value = String(v); fire(el); };
  const setSkill = (name, v) => {
    const el = document.querySelector(`tr[data-skill="${name}"] [data-role="base"]`);
    el.value = String(v); fire(el);
  };
  const click = (id) => document.getElementById(id).dispatchEvent(new dom.window.MouseEvent('click', { bubbles: true }));
  const addRow = (table) => {
    document.querySelector(`.row-add[data-add-target="${table}"]`)
      .dispatchEvent(new dom.window.MouseEvent('click', { bubbles: true }));
    const rows = document.querySelectorAll(`.dyn-table[data-table="${table}"] [data-row]`);
    return rows[rows.length - 1];
  };
  const setCol = (row, col, v) => {
    const el = row.querySelector(`[data-col="${col}"]`);
    if (el.type === 'checkbox') { el.checked = !!v; fire(el, 'change'); }
    else { el.value = String(v); fire(el); }
  };
  return { dom, document, $, out, setAttr, setSkill, click, addRow, setCol, fire };
}

const S = boot();

// ---- Tempo Pool: DEX + 1 dice, sized by STR ------------------------------
const DIE = { 0: '1d4', 1: '1d4', 2: '1d6', 3: '1d8', 4: '1d10', 5: '1d12' };
for (const str of [0, 1, 2, 3, 4, 5]) {
  S.setAttr('STR', str);
  const want = DIE[str] + (str <= 0 ? ' (Disadv.)' : '');
  check(`Tempo Die at STR ${str}`, S.out('out-tempoDie'), want);
}
for (const dex of [0, 1, 2, 3, 4, 5]) {
  S.setAttr('DEX', dex);
  check(`Tempo Pool at DEX ${dex}`, S.out('out-tempoPool'), dex + 1);
}
// above 5 the two columns part company
S.setAttr('STR', 5); S.$('[name="attr:STR:mod"]').value = '2'; S.fire(S.$('[name="attr:STR:mod"]'));
check('Tempo Die at STR 7 stays 1d12', S.out('out-tempoDie'), '1d12');
S.$('[name="attr:STR:mod"]').value = '0'; S.fire(S.$('[name="attr:STR:mod"]'));
S.setAttr('DEX', 5); S.$('[name="attr:DEX:mod"]').value = '1'; S.fire(S.$('[name="attr:DEX:mod"]'));
check('Tempo Pool at DEX 6 keeps growing', S.out('out-tempoPool'), 7);
S.$('[name="attr:DEX:mod"]').value = '0'; S.fire(S.$('[name="attr:DEX:mod"]'));

// ---- negative Attributes: the three stats that floor ---------------------
// A racial modifier can leave an Attribute at -1 or lower (character_creation.md
// Attribute Limits). Tempo Pool floors at 1 die, Mana and Slots at 0; Wards,
// damage and Initiative take the negative straight.
S.setAttr('DEX', 0); S.$('[name="attr:DEX:mod"]').value = '-1'; S.fire(S.$('[name="attr:DEX:mod"]'));
check('Tempo Pool floors at 1 die at DEX -1', S.out('out-tempoPool'), 1);
check('DEX Ward takes the negative straight', S.out('ward-DEX'), 4);
check('Missile damage takes the negative straight', S.out('out-missileDamage'), '+-1');
S.$('[name="attr:DEX:mod"]').value = '0'; S.fire(S.$('[name="attr:DEX:mod"]'));
S.setAttr('MIND', 0); S.$('[name="attr:MIND:mod"]').value = '-1'; S.fire(S.$('[name="attr:MIND:mod"]'));
check('Max Mana floors at 0 at MIND -1', S.out('out-manaMax'), 0);
check('Initiative still follows MIND below 0', S.out('out-initiative'), 4);
S.$('[name="attr:MIND:mod"]').value = '0'; S.fire(S.$('[name="attr:MIND:mod"]'));
S.setAttr('STR', 0); S.$('[name="attr:STR:mod"]').value = '-1'; S.fire(S.$('[name="attr:STR:mod"]'));
check('Slots floor at 0 at STR -1', S.out('out-carryMax'), 0);
check('Tempo Die at STR -1 is 1d4 at Disadvantage', S.out('out-tempoDie'), '1d4 (Disadv.)');
S.$('[name="attr:STR:mod"]').value = '0'; S.fire(S.$('[name="attr:STR:mod"]'));

// ---- Attributes are a standard array, not a pool -------------------------
// character_creation.md Step 5: six fixed numbers per priority letter, plus the
// +1 granted at levels 4/8/12. The sheet checks the BASE total against that.
const setPriority = (cat, letter) => {
  const el = S.$(`[name="priority:${cat}"]`);
  el.value = letter; S.fire(el, 'change');
};
['attributes','skills','career','feats','race'].forEach((cat, i) => setPriority(cat, 'ABCDE'[i]));
check('A priority shows its array', S.out('out-attrArray'), '3, 2, 2, 1, 1, 0');
setPriority('attributes', 'C'); setPriority('skills', 'A');
check('C priority shows its array', S.out('out-attrArray'), '2, 2, 1, 1, 0, 0');
[['STR',2],['DEX',2],['MIND',1],['ARC',1],['FAI',0],['CHA',0]].forEach(([k,v]) => S.setAttr(k, v));
check('array assigned whole reads as matching', S.out('out-attrArrayCheck'), 'BASE total 6 - matches');
S.setAttr('CHA', 2);
check('a number the array never handed out is flagged', S.out('out-attrArrayCheck'), 'BASE total 8, expected 6');
S.setAttr('CHA', 0);
// the +1s at 4/8/12 raise the expected total, and nothing else does
const xpEl = S.$('[name="exp"]'); xpEl.value = '1920'; S.fire(xpEl);   // Level 8
check('two banked increases show on the array', S.out('out-attrArray'), '2, 2, 1, 1, 0, 0 (+2)');
check('and raise the expected BASE total', S.out('out-attrArrayCheck'), 'BASE total 6, expected 8');
S.setAttr('STR', 4);
check('spending them clears the check', S.out('out-attrArrayCheck'), 'BASE total 8 - matches');
xpEl.value = '30'; S.fire(xpEl);
[['STR',3],['DEX',2],['MIND',2],['ARC',1],['FAI',0],['CHA',0]].forEach(([k,v]) => S.setAttr(k, v));

// ---- Initiative = 5 + MIND ----------------------------------------------
for (const mind of [0, 3, 5]) { S.setAttr('MIND', mind); check(`Initiative at MIND ${mind}`, S.out('out-initiative'), 5 + mind); }

// ---- damage split --------------------------------------------------------
S.setAttr('STR', 3); S.setAttr('DEX', 2);
check('Melee damage is STR', S.out('out-meleeDamage'), '+3');
check('Missile damage is DEX', S.out('out-missileDamage'), '+2');

// ---- Wards = 5 + Attribute ----------------------------------------------
check('STR Ward', S.out('ward-STR'), 8);
check('DEX Ward', S.out('ward-DEX'), 7);

// ---- Armor Penalty banded off Max AR ------------------------------------
const armor = S.addRow('armor');
for (const [maxAr, want] of [[2, '-1'], [4, '-1'], [5, '-2'], [7, '-2'], [8, '-3'], [10, '-3']]) {
  S.setCol(armor, 'maxAr', maxAr); S.setCol(armor, 'ar', maxAr); S.setCol(armor, 'worn', true);
  check(`Armor Penalty at Max AR ${maxAr}`, S.out('out-armorPenalty'), want);
}
S.setCol(armor, 'worn', false);
check('Unworn armor contributes no Penalty', S.out('out-armorPenalty'), '0');

// ---- Shield Guard: highest only, never summed ---------------------------
const buckler = S.addRow('shields');
S.setCol(buckler, 'guard', 1); S.setCol(buckler, 'equipped', true);
check('One Buckler', S.out('out-shieldGuard'), '+1');
const heater = S.addRow('shields');
S.setCol(heater, 'guard', 2); S.setCol(heater, 'equipped', true);
check('Buckler + Heater takes the HIGHEST, not the sum', S.out('out-shieldGuard'), '+2');
S.click('btnGuardHit');
check('A lost Parry degrades the highest shield only', S.out('out-shieldGuard'), '+1');
check('...and the Buckler was untouched', buckler.querySelector('[data-col="guard"]').value, '1');
S.setCol(heater, 'equipped', false);

// ---- Weapon Attack / Parry ----------------------------------------------
S.setSkill('Two-Handed Blades', 3);
S.setSkill('Ranged', 4);
const sword = S.addRow('weapons');
S.setCol(sword, 'skill', 'Two-Handed Blades');
check('Attack is the Weapon Skill alone', sword.querySelector('[data-col-out="atkBonus"]').textContent, '+3');
check('Parry adds Guard', sword.querySelector('[data-col-out="parryBonus"]').textContent, '+4');
const bow = S.addRow('weapons');
S.setCol(bow, 'skill', 'Ranged');
check('Missile attack still uses its Skill', bow.querySelector('[data-col-out="atkBonus"]').textContent, '+4');
check('A bow cannot Parry', bow.querySelector('[data-col-out="parryBonus"]').textContent, '-');

// ---- Length column replaced Band; Opening threshold column is gone ------
// (the sharp-weapon 4/3 threshold was deleted from exchange.md - every
// weapon takes an Opening on the same flat margin of 5 now)
const lengthInput = sword.querySelector('[data-col="length"]');
check('Length column exists, floors at 1', lengthInput && lengthInput.min, '1');
check('Length column caps at 5', lengthInput && lengthInput.max, '5');
check('No band column survives', sword.querySelector('[data-col="band"]'), 'null');
check('No opening column survives', sword.querySelector('[data-col="opening"]'), 'null');
check('No crit column survives', sword.querySelector('[data-col="crit"]'), 'null');

// ---- Tempo tracker -------------------------------------------------------
S.setAttr('DEX', 3);           // pool 4
S.click('btnTempoRefill');
check('Refill fills the pool', S.out('out-tempoCurrent'), 4);
S.click('btnTempoSpend'); S.click('btnTempoSpend');
check('Spending takes dice', S.out('out-tempoCurrent'), 2);
S.click('btnTempoSpend'); S.click('btnTempoSpend'); S.click('btnTempoSpend');
check('Pool floors at 0, never negative', S.out('out-tempoCurrent'), 0);
S.click('btnTempoRefill');
check('Refill is the refill', S.out('out-tempoCurrent'), 4);

// ---- Wound Thresholds are flat text, not a STR lookup -------------------
const html = fs.readFileSync(SHEET, 'utf8');
check('Flat Wound Thresholds present', /1-9[\s\S]{0,80}10-18[\s\S]{0,80}19\+/.test(html), 'true');

// ---- persistence round-trip ---------------------------------------------
let saveErr = '';
try { S.click('btnSave'); } catch (e) { saveErr = e.message; }
check('Save to localStorage does not throw', saveErr, '');
const stored = S.dom.window.localStorage.getItem('ressam-character-sheet-v1');
check('Something was stored', stored && stored.length > 50, 'true');
const parsed = JSON.parse(stored);
check('Stored tables include weapons', Array.isArray(parsed.tables.weapons), 'true');
check('Stored weapon carries the length column', 'length' in parsed.tables.weapons[0], 'true');
check('Stored weapon does not carry the deleted opening column', 'opening' in parsed.tables.weapons[0], 'false');

// ---- a saved sheet from BEFORE this rework still loads -------------------
const legacy = {
  fields: { 'attr:STR:base': '4', 'attr:DEX:base': '2', 'attr:MIND:base': '3', brokenIn: '2' },
  tables: {
    weapons: [{ name: 'Old Sword', skill: 'Cleaving Blades', damage: '1d10', reach: 'Medium', critRange: '11', band: 'Long', opening: '4', slots: '1', equipped: true }],
    armor: [{ name: 'Old Mail', type: 'Medium', ar: '4', maxAr: '4', penalty: '2', worn: true }],
    shields: [], clothes: [], backpack: [], wounds: [], scars: [], spells: [],
  },
};
const S3 = boot(legacy);   // seeded before the sheet's script runs
let legacyErr = '';
try {
  check('Legacy save: STR read back', S3.$('[name="attr:STR:base"]').value, '4');
  check('Legacy save: Tempo Die derived from it', S3.out('out-tempoDie'), '1d10');
  check('Legacy save: Initiative from MIND', S3.out('out-initiative'), '8');
  check('Legacy save: no Length value to load leaves the input blank, not broken',
    S3.document.querySelector('#tbl-weapons [data-col="length"]').value, '');
  check('Legacy save: the deleted Band column no longer exists to load into',
    S3.document.querySelector('#tbl-weapons [data-col="band"]'), 'null');
  check('Legacy save: the deleted Opening column no longer exists to load into',
    S3.document.querySelector('#tbl-weapons [data-col="opening"]'), 'null');
  check('Legacy save: Armor Penalty re-derived from Max AR, ignoring the old typed value',
    S3.out('out-armorPenalty'), '-1');
  check('Legacy save: the deleted Broken In field is ignored, not applied',
    S3.$('[name="brokenIn"]'), 'null');
} catch (e) { legacyErr = e.message; }
check('Legacy save loads without throwing', legacyErr, '');

// ---- report --------------------------------------------------------------
console.log(`\n${pass} passed, ${fail} failed\n`);
if (fail) { failures.forEach((f) => console.log('  FAIL  ' + f)); process.exit(1); }
