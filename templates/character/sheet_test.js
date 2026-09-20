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
//   than trusted. The legacy fixture below predates the Bulky Items merge (weapons/
//   armor/shields as three separate tables, folded into "bulky" rows on load - see
//   migrateLegacyBulkyTables() in the sheet), the Band-to-Length rename, and the
//   sharp-weapon Opening-threshold deletion, on top of the older fields it already
//   covered from before the 2026-08-23 Exchange merge.
//
//   Also covers: Max Wounds by Size, the Wound Log driving current Wounds/Wound
//   Penalty, Patched Wounds capping to missing Wounds, Trauma labels/clamping,
//   the Dying flag, Scar derivation, the Death Clock reset button, Backpack
//   Slots (Size scaling, worn-clothes exclusion, Weapon/Armor/Shield-typed Bulky
//   rows never touching it even though their hidden Other-group Slots input is
//   still in the DOM), Bulky Capacity (flat 5 + Size, counting equipped and spare
//   Weapon/Armor/Shield rows alike, freed only by removing the row, and an
//   Other-typed or untyped row counting toward it not at all), the single Bulky
//   Items table's per-row Type switch (field-group visibility and the Equipped/
//   Worn label), a Skill Base flagged when it exceeds its governing Attribute,
//   the Magic Feats table (Unlock tier -> ranks unlocked, Focus tier -> flat
//   non-stacking roll bonus, flagged when Focus outpaces Unlock - no Skill or
//   Attribute involved, per the 2026-09-14 magic rework), the flat 10-school
//   Spells Known dropdown with no more Arcane/Divine prep-row distinction,
//   Level derived from EXP at its table boundaries, and the Priorities
//   completeness/no-repeats warning.
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
// character_creation.md Step 5: four fixed numbers per priority letter (six
// shrank to four when ARC/FAI were deleted, 2026-09-14), plus the +1 granted
// at levels 4/8/12. The sheet checks the BASE total against that.
const setPriority = (cat, letter) => {
  const el = S.$(`[name="priority:${cat}"]`);
  el.value = letter; S.fire(el, 'change');
};
['attributes','skills','career','feats','race'].forEach((cat, i) => setPriority(cat, 'ABCDE'[i]));
check('A priority shows its array', S.out('out-attrArray'), '3, 2, 1, 0');
setPriority('attributes', 'C'); setPriority('skills', 'A');
check('C priority shows its array', S.out('out-attrArray'), '2, 1, 1, 0');
[['STR',2],['DEX',1],['MIND',1],['CHA',0]].forEach(([k,v]) => S.setAttr(k, v));
check('array assigned whole reads as matching', S.out('out-attrArrayCheck'), 'BASE total 4 - matches');
S.setAttr('CHA', 2);
check('a number the array never handed out is flagged', S.out('out-attrArrayCheck'), 'BASE total 6, expected 4');
S.setAttr('CHA', 0);
// the +1s at 4/8/12 raise the expected total, and nothing else does
const xpEl = S.$('[name="exp"]'); xpEl.value = '1920'; S.fire(xpEl);   // Level 8
check('two banked increases show on the array', S.out('out-attrArray'), '2, 1, 1, 0 (+2)');
check('and raise the expected BASE total', S.out('out-attrArrayCheck'), 'BASE total 4, expected 6');
S.setAttr('STR', 4);
check('spending them clears the check', S.out('out-attrArrayCheck'), 'BASE total 6 - matches');
xpEl.value = '30'; S.fire(xpEl);
[['STR',3],['DEX',2],['MIND',2],['CHA',0]].forEach(([k,v]) => S.setAttr(k, v));

// ---- Initiative = 5 + MIND ----------------------------------------------
for (const mind of [0, 3, 5]) { S.setAttr('MIND', mind); check(`Initiative at MIND ${mind}`, S.out('out-initiative'), 5 + mind); }

// ---- damage split --------------------------------------------------------
S.setAttr('STR', 3); S.setAttr('DEX', 2);
check('Melee damage is STR', S.out('out-meleeDamage'), '+3');
check('Missile damage is DEX', S.out('out-missileDamage'), '+2');

// ---- Wards = 5 + Attribute ----------------------------------------------
check('STR Ward', S.out('ward-STR'), 8);
check('DEX Ward', S.out('ward-DEX'), 7);

// ---- Bulky Items: unified table, gated on a per-row Type ------------------
// Armor Penalty banded off Max Dent Line; Dent/Rend derived from Damage
const armor = S.addRow('bulky');
S.setCol(armor, 'itemType', 'armor');
for (const [maxDent, want] of [[3, '-1'], [5, '-1'], [6, '-2'], [8, '-2'], [9, '-3'], [11, '-3']]) {
  S.setCol(armor, 'maxDent', maxDent); S.setCol(armor, 'maxRend', maxDent + 4);
  S.setCol(armor, 'armorDamage', 0); S.setCol(armor, 'active', true);
  check(`Armor Penalty at Max Dent ${maxDent}`, S.out('out-armorPenalty'), want);
}
check('At 0 Damage, current Dent/Rend equal the Max pair, gap intact', S.out('out-dentRend'), '11 / 15');
check('Per-row computed Dent cell matches', armor.querySelector('[data-col-out="dent"]').textContent, '11');
check('Per-row computed Rend cell matches', armor.querySelector('[data-col-out="rend"]').textContent, '15');
S.setCol(armor, 'armorDamage', 3);
check('Damage lowers both current lines together, gap intact', S.out('out-dentRend'), '8 / 12');
S.setCol(armor, 'armorDamage', 11);
check('Damage >= Max Dent floors Dent at 0', armor.querySelector('[data-col-out="dent"]').textContent, '0');
check('...and Rend reads 0 too rather than a leftover value (armor.md: resolves as Unarmored, not a bottomed-out pair)',
  S.out('out-dentRend'), '0 / 0');
S.setCol(armor, 'armorDamage', 0);
S.setCol(armor, 'active', false);
check('Unworn armor contributes no Penalty', S.out('out-armorPenalty'), '0');
check('Unworn armor contributes no Dent/Rend', S.out('out-dentRend'), '0 / 0');
check('Armor row selects the Worn label, not Equipped', armor.querySelector('[data-role="activeLabel"]').textContent, 'Worn');

// ---- Shield Guard: highest only, never summed ---------------------------
const buckler = S.addRow('bulky');
S.setCol(buckler, 'itemType', 'shield');
S.setCol(buckler, 'guard', 1); S.setCol(buckler, 'active', true);
check('One Buckler', S.out('out-shieldGuard'), '+1');
check('Shield row selects the Equipped label', buckler.querySelector('[data-role="activeLabel"]').textContent, 'Equipped');
const heater = S.addRow('bulky');
S.setCol(heater, 'itemType', 'shield');
S.setCol(heater, 'guard', 2); S.setCol(heater, 'active', true);
check('Buckler + Heater takes the HIGHEST, not the sum', S.out('out-shieldGuard'), '+2');
S.click('btnGuardHit');
check('A lost Parry degrades the highest shield only', S.out('out-shieldGuard'), '+1');
check('...and the Buckler was untouched', buckler.querySelector('[data-col="guard"]').value, '1');
S.setCol(heater, 'active', false);

// ---- Weapon Attack / Parry ----------------------------------------------
S.setSkill('Two-Handed Blades', 3);
S.setSkill('Ranged', 4);
const sword = S.addRow('bulky');
S.setCol(sword, 'itemType', 'weapon');
S.setCol(sword, 'skill', 'Two-Handed Blades');
check('Attack is the Weapon Skill alone', sword.querySelector('[data-col-out="atkBonus"]').textContent, '+3');
check('Parry adds Guard', sword.querySelector('[data-col-out="parryBonus"]').textContent, '+4');
const bow = S.addRow('bulky');
S.setCol(bow, 'itemType', 'weapon');
S.setCol(bow, 'skill', 'Ranged');
check('Missile attack still uses its Skill', bow.querySelector('[data-col-out="atkBonus"]').textContent, '+4');
check('A bow cannot Parry', bow.querySelector('[data-col-out="parryBonus"]').textContent, '-');

// ---- Type switch shows/hides the matching field group only ---------------
// (mirrors the Spells tab's School-driven prep-field switch)
const weaponGroup = sword.querySelector('[data-fields="weapon"]');
const armorGroup = sword.querySelector('[data-fields="armor"]');
const shieldGroup = sword.querySelector('[data-fields="shield"]');
const otherGroup = sword.querySelector('[data-fields="other"]');
check('Weapon type shows the weapon field group', weaponGroup.style.display, '');
check('Weapon type hides the armor field group', armorGroup.style.display, 'none');
check('Weapon type hides the shield field group', shieldGroup.style.display, 'none');
check('Weapon type hides the other field group', otherGroup.style.display, 'none');
S.setCol(sword, 'itemType', 'armor');
check('Switching type hides the previous field group', weaponGroup.style.display, 'none');
check('...and shows the new one', armorGroup.style.display, '');
S.setCol(sword, 'itemType', 'weapon');
check('Switching back restores the weapon group', weaponGroup.style.display, '');
check('...and the Skill field was never cleared by the switch', sword.querySelector('[data-col-out="atkBonus"]').textContent, '+3');

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

// ---- Wound resolution reads the target's armor lines, not a flat table --
const html = fs.readFileSync(SHEET, 'utf8');
check('Turned Aside / Dent Line / Rend Line resolution present', /Turned Aside[\s\S]{0,300}Dent Line[\s\S]{0,300}Rend Line/.test(html), 'true');
check('Old flat 1-9/10-18/19+ threshold table is gone', /1-9[\s\S]{0,80}10-18[\s\S]{0,80}19\+/.test(html), 'false');

// ---- persistence round-trip ---------------------------------------------
let saveErr = '';
try { S.click('btnSave'); } catch (e) { saveErr = e.message; }
check('Save to localStorage does not throw', saveErr, '');
const stored = S.dom.window.localStorage.getItem('ressam-character-sheet-v1');
check('Something was stored', stored && stored.length > 50, 'true');
const parsed = JSON.parse(stored);
check('Stored tables include bulky', Array.isArray(parsed.tables.bulky), 'true');
const storedSword = parsed.tables.bulky.find((r) => r.itemType === 'weapon' && r.skill === 'Two-Handed Blades');
check('Stored weapon row carries the length column', storedSword && 'length' in storedSword, 'true');
check('Stored weapon row does not carry the deleted opening column', storedSword && 'opening' in storedSword, 'false');

// ---- a saved sheet from BEFORE the Bulky Items merge still loads ---------
// (predates both this merge and the earlier Band-to-Length rename/sharp-weapon
// Opening deletion, so it also exercises the older per-table field drops)
const legacy = {
  fields: { 'attr:STR:base': '4', 'attr:DEX:base': '2', 'attr:MIND:base': '3', brokenIn: '2' },
  tables: {
    weapons: [{ name: 'Old Sword', skill: 'Cleaving Blades', damage: '1d10', reach: 'Medium', critRange: '11', band: 'Long', opening: '4', slots: '1', equipped: true }],
    armor: [{ name: 'Old Mail', type: 'Medium', ar: '4', maxAr: '4', penalty: '2', worn: true }], // pre-Dent/Rend Line field names (ar/maxAr)
    shields: [], clothes: [], backpack: [], wounds: [], scars: [], spells: [],
  },
};
const S3 = boot(legacy);   // seeded before the sheet's script runs
let legacyErr = '';
try {
  check('Legacy save: STR read back', S3.$('[name="attr:STR:base"]').value, '4');
  check('Legacy save: Tempo Die derived from it', S3.out('out-tempoDie'), '1d10');
  check('Legacy save: Initiative from MIND', S3.out('out-initiative'), '8');
  check('Legacy save: the old weapons/armor tables were folded into Bulky Items',
    S3.document.querySelectorAll('#tbl-bulky [data-row]').length, 2);
  check('Legacy save: the migrated weapon row is typed Weapon',
    S3.document.querySelector('#tbl-bulky [data-row]').querySelector('[data-col="itemType"]').value, 'weapon');
  check('Legacy save: no Length value to load leaves the input blank, not broken',
    S3.document.querySelector('#tbl-bulky [data-col="length"]').value, '');
  check('Legacy save: the deleted Band column no longer exists to load into',
    S3.document.querySelector('#tbl-bulky [data-col="band"]'), 'null');
  check('Legacy save: the deleted Opening column no longer exists to load into',
    S3.document.querySelector('#tbl-bulky [data-col="opening"]'), 'null');
  check('Legacy save: old ar/maxAr field names don\'t map to the renamed maxDent/maxRend columns, so Penalty comes back 0',
    S3.out('out-armorPenalty'), '0');
  check('Legacy save: the deleted Broken In field is ignored, not applied',
    S3.$('[name="brokenIn"]'), 'null');
} catch (e) { legacyErr = e.message; }
check('Legacy save loads without throwing', legacyErr, '');

// ---- Max Wounds by Size ---------------------------------------------------
const sizeSel = S.$('[name="size"]');
sizeSel.value = '0.5'; S.fire(sizeSel, 'change');
check('Max Wounds Small', S.out('out-hpMax'), 2);
sizeSel.value = '2'; S.fire(sizeSel, 'change');
check('Max Wounds Large', S.out('out-hpMax'), 4);
sizeSel.value = '1'; S.fire(sizeSel, 'change');
check('Max Wounds Medium', S.out('out-hpMax'), 3);
const hpBonusEl = S.$('[name="hpBonus"]');
hpBonusEl.value = '2'; S.fire(hpBonusEl);
check('Feat Bonus adds to Max Wounds', S.out('out-hpMax'), 5);
hpBonusEl.value = '0'; S.fire(hpBonusEl);

// ---- Wound Log drives current Wounds / Wound Penalty / Dying -------------
const wound1 = S.addRow('wounds');
S.setCol(wound1, 'severity', '2');
check('One Wound of Severity 2 reduces current Wounds', S.out('out-woundsCurrent'), 1);
check('Wound Penalty is -missing Wounds', S.out('out-woundPenalty'), '-2');
check('Not Dying above 0 Wounds', S.out('out-dyingFlag'), 'No');
const wound2 = S.addRow('wounds');
S.setCol(wound2, 'severity', '2');
check('Wounds floor at 0, never negative', S.out('out-woundsCurrent'), 0);
check('At 0 Wounds, Dying flips to Yes', S.out('out-dyingFlag'), 'Yes');

// ---- Patched Wounds cap to missing Wounds ---------------------------------
const patchedEl = S.$('[name="patchedCurrent"]');
patchedEl.value = '10'; S.fire(patchedEl);
check('Patched Wounds clamps to the missing-Wounds cap', patchedEl.value, '3');
check('Patched Max reflects missing Wounds', S.out('out-patchedMax'), 3);
patchedEl.value = '0'; S.fire(patchedEl);

// ---- Death Clock reset (sets to STR total) --------------------------------
S.setAttr('STR', 3);
S.click('btnDeathClockReset');
check('Death Clock reset sets to STR total', S.$('[name="deathClock"]').value, '3');

// ---- Trauma: label + clamp -------------------------------------------------
const traumaEl = S.$('[name="traumaLevel"]');
traumaEl.value = '0'; S.fire(traumaEl);
check('Trauma 0 label', S.out('out-traumaNote'), 'None - 0 to all d12 rolls, Wards, and checks');
traumaEl.value = '3'; S.fire(traumaEl);
check('Trauma 3 label', S.out('out-traumaNote'), 'Critical - -3 to all d12 rolls, Wards, and checks');
traumaEl.value = '7'; S.fire(traumaEl);
check('Trauma clamps at 5, never higher', traumaEl.value, '5');
check('Trauma 5 label', S.out('out-traumaNote'), 'Automatic Death - -5 to all d12 rolls, Wards, and checks');
traumaEl.value = '0'; S.fire(traumaEl);

// ---- Scars: Damage Type -> Scar name --------------------------------------
const scar = S.addRow('scars');
S.setCol(scar, 'damageType', 'Fire');
check('Scar derived from Damage Type (Fire)', scar.querySelector('[data-col-out="scarName"]').textContent, 'Burn');
S.setCol(scar, 'damageType', 'Psychic');
check('Scar derived from Damage Type (Psychic)', scar.querySelector('[data-col-out="scarName"]').textContent, 'Mania');

// ---- Backpack Slots: Size scaling, worn-clothes exclusion, weapons/armor/
// shields never touch it at all (they draw from Bulky Capacity instead) -----
S.setAttr('STR', 3);
sizeSel.value = '1'; S.fire(sizeSel, 'change');
check('Carry Max = 2 x STR x Size', S.out('out-carryMax'), 6);
sizeSel.value = '2'; S.fire(sizeSel, 'change');
check('Carry Max doubles at Large size', S.out('out-carryMax'), 12);
sizeSel.value = '1'; S.fire(sizeSel, 'change');
const pack = S.addRow('backpack');
S.setCol(pack, 'slots', '4');
check('Backpack items count towards carry current', S.out('out-carryCurrent'), 4);
const spareCloak = S.addRow('clothes');
S.setCol(spareCloak, 'slots', '1'); S.setCol(spareCloak, 'worn', false);
check('A carried spare clothing item adds to carry current', S.out('out-carryCurrent'), 5);
S.setCol(spareCloak, 'worn', true);
check('Worn clothing is excluded from carry current', S.out('out-carryCurrent'), 4);
// Every Bulky Items row template carries all four field groups (only the
// matching one is shown), so a Weapon/Armor/Shield row still has an (hidden)
// Other-group Slots input - it must not leak into Backpack Slots regardless.
S.setCol(sword, 'slots', '9'); S.setCol(armor, 'slots', '9'); S.setCol(buckler, 'slots', '9');
check('A Weapon/Armor/Shield row\'s hidden Slots field never counts towards carry current', S.out('out-carryCurrent'), 4);
S.setCol(sword, 'slots', '0'); S.setCol(armor, 'slots', '0'); S.setCol(buckler, 'slots', '0');

// ---- Bulky Capacity: flat 5 + Size, weapons/armor/shields count 1 each, ---
// equipped or spare, and only removing the row frees the space -------------
check('Bulky Max = 5 + Size (Medium +1)', S.out('out-bulkyMax'), 6);
sizeSel.value = '2'; S.fire(sizeSel, 'change');
check('Bulky Max = 5 + Size (Large +2)', S.out('out-bulkyMax'), 7);
// Huge isn't a player-legal Size (rest_and_survival.md) and has no option in
// the sheet's Size dropdown, same as Wounds baseline above - only Small,
// Medium and Large are reachable here.
sizeSel.value = '0.5'; S.fire(sizeSel, 'change');
check('Bulky Max = 5 + Size (Small +0)', S.out('out-bulkyMax'), 5);
sizeSel.value = '1'; S.fire(sizeSel, 'change');
// at this point: 1 armor row, 2 shield rows, 2 weapon rows already exist from
// earlier tests, all typed
check('Bulky current counts every Weapon/Armor/Shield-typed row', S.out('out-bulkyCurrent'), 5);
S.setCol(sword, 'active', true);
check('Equipping a weapon does not change Bulky current - it already counted', S.out('out-bulkyCurrent'), 5);
S.setCol(sword, 'active', false);
check('Unequipping it back does not change Bulky current either', S.out('out-bulkyCurrent'), 5);
const spareAxe = S.addRow('bulky');
S.setCol(spareAxe, 'itemType', 'weapon');
check('Adding a spare weapon row adds 1, before it even has a name', S.out('out-bulkyCurrent'), 6);
spareAxe.querySelector('.row-remove').dispatchEvent(new S.dom.window.MouseEvent('click', { bubbles: true }));
check('Removing the row frees the space back up', S.out('out-bulkyCurrent'), 5);
const untyped = S.addRow('bulky');
check('An untyped row counts towards neither pool', S.out('out-bulkyCurrent'), 5);
check('...and Backpack Slots is unaffected either', S.out('out-carryCurrent'), 4);

// ---- "Other" type: a Bulky Item that isn't Bulky at all -------------------
// (the point of this whole merge - it behaves like an ordinary Backpack item)
S.setCol(untyped, 'itemType', 'other');
S.setCol(untyped, 'slots', '2');
check('An Other-typed row counts towards Backpack Slots', S.out('out-carryCurrent'), 6);
check('...and NOT towards Bulky Capacity', S.out('out-bulkyCurrent'), 5);
check('Other row hides the Equipped/Worn field entirely', untyped.querySelector('[data-role="activeField"]').style.display, 'none');
untyped.querySelector('.row-remove').dispatchEvent(new S.dom.window.MouseEvent('click', { bubbles: true }));
check('Removing the Other row frees its Backpack Slots back up', S.out('out-carryCurrent'), 4);

// ---- Bulky Capacity is a hard cap, unlike Backpack Slots' soft Encumbered -
// (rest_and_survival.md: "You cannot exceed your Bulky Capacity... you have
// nowhere left on your body or straps to put another"). Switching a row's
// Type to Weapon/Armor/Shield is blocked once the pool is already full.
let alertMsg = null;
S.dom.window.alert = function (msg) { alertMsg = msg; };
sizeSel.value = '0.5'; S.fire(sizeSel, 'change'); // Small -> Bulky Max 5, exactly the 5 rows already typed
check('Bulky Max at Small matches the current count (cap test setup)', S.out('out-bulkyMax'), 5);
check('Bulky current is already at the cap', S.out('out-bulkyCurrent'), 5);
const overflowRow = S.addRow('bulky');
S.setCol(overflowRow, 'itemType', 'weapon');
check('Setting Type over the cap raises a warning', (alertMsg || '').indexOf('Bulky Capacity full') !== -1, 'true');
check('...and the Type is reverted rather than applied', overflowRow.querySelector('[data-col="itemType"]').value, '');
check('...so Bulky current stays at the cap', S.out('out-bulkyCurrent'), 5);
alertMsg = null;
S.setCol(overflowRow, 'itemType', 'other');
check('Other is never capped - it never touches Bulky Capacity', overflowRow.querySelector('[data-col="itemType"]').value, 'other');
check('...and no warning fires for an Other row', alertMsg, 'null');
overflowRow.querySelector('.row-remove').dispatchEvent(new S.dom.window.MouseEvent('click', { bubbles: true }));
sizeSel.value = '1'; S.fire(sizeSel, 'change');

// ---- Skill Base flagged red when it exceeds its governing Attribute -------
S.setAttr('MIND', 1);
S.setSkill('Thaumaturgy', 5);
const thaumTotal = S.document.querySelector('tr[data-skill="Thaumaturgy"] [data-skill-total]');
check('Skill Base exceeding its Attribute is flagged', thaumTotal.title.indexOf('exceeds governing Attribute') !== -1, 'true');
S.setSkill('Thaumaturgy', 1);
check('Skill Base within its Attribute is not flagged', thaumTotal.title, '');
S.setSkill('Thaumaturgy', 0);

// ---- Magic Feats: Unlock tier -> ranks, Focus tier -> flat bonus ---------
// (2026-09-14 magic rework - no more Arcane/Divine split, no Skill or
// Attribute involved anywhere in this table; see magic_feats.md)
const pyroUnlock = S.$('[name="magic:Pyromancy:unlock"]');
const pyroFocus = S.$('[name="magic:Pyromancy:focus"]');
const pyroRow = S.document.querySelector('#magicFeatsBody tr[data-school-row="Pyromancy"]');
check('No Unlock shows no ranks available', pyroRow.querySelector('[data-magic-ranks="Pyromancy"]').textContent, '-');
check('No Focus shows +0 bonus', pyroRow.querySelector('[data-magic-bonus="Pyromancy"]').textContent, '+0');
pyroUnlock.value = 'Adept'; S.fire(pyroUnlock, 'change');
check('Adept Unlock grants ranks 1-4', pyroRow.querySelector('[data-magic-ranks="Pyromancy"]').textContent, '1-4');
pyroFocus.value = 'Adept'; S.fire(pyroFocus, 'change');
check('Adept Focus grants a flat +2', pyroRow.querySelector('[data-magic-bonus="Pyromancy"]').textContent, '+2');
check('Focus matching its Unlock is not flagged', pyroRow.querySelector('[data-magic-bonus="Pyromancy"]').title, '');
pyroFocus.value = 'Expert'; S.fire(pyroFocus, 'change');
check('Focus ahead of its Unlock is flagged', pyroRow.querySelector('[data-magic-bonus="Pyromancy"]').title.indexOf('needs the matching Unlock') !== -1, 'true');
pyroFocus.value = 'None'; S.fire(pyroFocus, 'change');
pyroUnlock.value = 'None'; S.fire(pyroUnlock, 'change');

// ---- Spells Known: flat 10-school dropdown, no more Arcane/Divine prep ---
const spellCard = S.addRow('spells');
check('School dropdown has no Arcane/Divine optgroups anymore', spellCard.querySelector('optgroup'), 'null');
check('School dropdown lists all ten schools flat', spellCard.querySelectorAll('[data-col="school"] option').length, 11); // 10 schools + blank
check('No scroll-prep field survives', spellCard.querySelector('[data-role="prepScrolls"]'), 'null');
check('No prep-note field survives', spellCard.querySelector('[data-role="prepNote"]'), 'null');

// ---- Level derived from EXP at the progression table's own boundaries -----
const expEl = S.$('[name="exp"]');
[[0, 1], [29, 1], [30, 1], [119, 1], [120, 2], [269, 2], [270, 3],
 [479, 3], [480, 4], [2429, 8], [2430, 9], [4320, 12], [9999, 12]].forEach(function (pair) {
  expEl.value = String(pair[0]); S.fire(expEl);
  check('Level at EXP ' + pair[0], S.out('level'), pair[1]);
});
expEl.value = '30'; S.fire(expEl);

// ---- Priorities: completeness + no-repeats warning -------------------------
['attributes', 'skills', 'career', 'feats', 'race'].forEach(function (cat, i) { setPriority(cat, 'ABCDE'[i]); });
check('Five unique priorities show no warning', S.$('#out-priorityWarning').style.display, 'none');
setPriority('attributes', '');
check('A missing priority letter raises the warning', S.$('#out-priorityWarning').style.display, '');
check('Warning text explains all five must be assigned', S.out('out-priorityWarning').indexOf('Assign all five') !== -1, 'true');
setPriority('attributes', 'E');
check('A repeated priority letter also raises the warning', S.$('#out-priorityWarning').style.display, '');
check('Warning text calls out the repeat', S.out('out-priorityWarning').indexOf('repeat') !== -1, 'true');
setPriority('attributes', 'A');
check('Fixing the repeat clears the warning', S.$('#out-priorityWarning').style.display, 'none');

// ---- Export: JSON content + filename sanitization -------------------------
// jsdom has no real URL.createObjectURL, so Blob/URL are stubbed here to
// capture what exportJSON() would hand a real browser rather than exercising
// the browser's own object-URL/download machinery (that part still needs a
// real browser - see the manual checklist).
let exportedParts = null, exportedType = null, capturedAnchor = null;
S.dom.window.Blob = function (parts, opts) { exportedParts = parts; exportedType = opts && opts.type; return {}; };
S.dom.window.URL.createObjectURL = function () { return 'blob:fake'; };
S.dom.window.URL.revokeObjectURL = function () {};
const origAppendChild = S.document.body.appendChild.bind(S.document.body);
S.document.body.appendChild = function (node) {
  capturedAnchor = node;
  node.click = function () {}; // jsdom has no real object-URL scheme to navigate to
  return origAppendChild(node);
};

const nameEl = S.$('#characterName');
nameEl.value = '  Sir Reginald  Thornwood '; S.fire(nameEl);
S.click('btnExport');
check('Export builds a JSON blob', exportedType, 'application/json');
const exported = JSON.parse(exportedParts[0]);
check('Exported JSON has a fields object', typeof exported.fields, 'object');
check('Exported JSON has a tables object', typeof exported.tables, 'object');
check('Exported JSON echoes the character name field', exported.fields.characterName, '  Sir Reginald  Thornwood ');
check('Export filename trims and collapses whitespace to underscores', capturedAnchor.download, 'Sir_Reginald_Thornwood.ressam.json');

nameEl.value = '   '; S.fire(nameEl);
S.click('btnExport');
check('A blank/whitespace-only name falls back to "character"', capturedAnchor.download, 'character.ressam.json');
nameEl.value = ''; S.fire(nameEl);

S.document.body.appendChild = origAppendChild;

// ---- report --------------------------------------------------------------
console.log(`\n${pass} passed, ${fail} failed\n`);
if (fail) { failures.forEach((f) => console.log('  FAIL  ' + f)); process.exit(1); }
