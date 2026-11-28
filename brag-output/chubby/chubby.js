// Chubby: the @wierd_stuff_i_make mascot. A chibi panda inventor in flat vector with ink outlines.
// panda({ view: 'front'|'side'|'back', expr: 'neutral'|'focused'|'proud'|'oops', tag: {n:'#002', c:'#FF8A3D'} }) -> SVG inner markup,
// drawn in a 400x560 box with the origin at the centre of the feet line minus 250 (feet at y = 250).
const K = {
  ink: '#161922', fur: '#F7F6F2', shade: '#E4E2DC', teal: '#18A999', tealL: '#7FE0D3', tealD: '#0E6B61',
  brass: '#C9A24A', brassD: '#8A6A22', blush: 'rgba(255,128,140,.38)', tongue: '#FF8FA3', pencil: '#F2C14E', paper: '#ECEEF2', smoke: '#B9BFCC', spark: '#FF8A3D',
};
const SW = 7; // the ink line
const ol = (extra = '') => `stroke="${K.ink}" stroke-width="${SW}" stroke-linejoin="round" stroke-linecap="round" ${extra}`;

function goggleRing(x, y, r = 46) {
  return `<circle cx="${x}" cy="${y}" r="${r + 8}" fill="none" stroke="${K.ink}" stroke-width="${SW}"/>
    <circle cx="${x}" cy="${y}" r="${r}" fill="${K.tealL}" fill-opacity=".38" stroke="${K.brass}" stroke-width="13"/>
    <circle cx="${x}" cy="${y}" r="${r - 7}" fill="none" stroke="${K.brassD}" stroke-width="2.5"/>
    ${[0, 1, 2, 3].map((i) => { const a = i * Math.PI / 2 + .6; return `<circle cx="${(x + Math.cos(a) * (r + 1)).toFixed(1)}" cy="${(y + Math.sin(a) * (r + 1)).toFixed(1)}" r="3" fill="${K.brassD}"/>`; }).join('')}
    <path d="M${x - r * .55} ${y - r * .35} A ${r * .7} ${r * .7} 0 0 1 ${x - r * .05} ${y - r * .62}" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".85"/>`;
}
function eye(x, y, expr, side) {
  if (expr === 'focused') return `<path d="M${x - 16} ${y + 2} Q${x} ${y - 8} ${x + 16} ${y + 2}" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/><path d="M${x - 18} ${y - 20} L${x + 14} ${y - 13 + (side < 0 ? 0 : 0)}" stroke="#fff" stroke-width="5" stroke-linecap="round" transform="rotate(${side * -12} ${x} ${y})"/>`;
  if (expr === 'proud') return `<path d="M${x - 16} ${y + 4} Q${x} ${y - 16} ${x + 16} ${y + 4}" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/>`;
  const r = expr === 'oops' ? 17 : 14, p = expr === 'oops' ? 6 : 8;
  return `<circle cx="${x}" cy="${y}" r="${r}" fill="#fff"/><circle cx="${x + side * 2}" cy="${y + 1}" r="${p}" fill="${K.ink}"/><circle cx="${x - 4}" cy="${y - 5}" r="3.2" fill="#fff"/>`;
}
function belt(view) {
  // clipped to the body; buckle, the pencil-and-ruler pocket, scissors, the tape roll and the AI-token pouch
  const band = `<g clip-path="url(#bodyclip-${view})"><rect x="-130" y="148" width="260" height="34" fill="${K.teal}" ${ol()}/></g>`;
  if (view === 'back') return band + `<g transform="translate(-14,150)"><circle cx="0" cy="18" r="22" fill="${K.paper}" ${ol()}/><circle cx="0" cy="18" r="9" fill="${K.fur}" ${ol('stroke-width="5"')}/></g>`;
  const buckle = view === 'front' ? `<rect x="-20" y="144" width="40" height="42" rx="7" fill="${K.brass}" ${ol()}/><rect x="-8" y="156" width="16" height="18" rx="3" fill="${K.brassD}"/>` : '';
  const pocket = view === 'front' ? `<g transform="translate(-74,160)">
      <rect x="2" y="-58" width="13" height="66" rx="2" fill="${K.pencil}" ${ol('stroke-width="5"')}/><path d="M2 -58 L8.5 -76 L15 -58 Z" fill="#E9C9A0" ${ol('stroke-width="5"')}/><path d="M6 -70 L8.5 -76 L11 -70 Z" fill="${K.ink}"/>
      <rect x="18" y="-48" width="16" height="58" rx="2" fill="#F3EBD8" ${ol('stroke-width="5"')}/>${[0, 1, 2, 3].map((i) => `<path d="M18 ${-40 + i * 11} h7" stroke="${K.ink}" stroke-width="3"/>`).join('')}
      <rect x="-6" y="0" width="48" height="50" rx="10" fill="${K.tealD}" ${ol()}/><path d="M-6 12 h48" stroke="${K.ink}" stroke-width="4"/></g>` : '';
  const pouch = view === 'front' || view === 'side' ? `<g transform="translate(${view === 'front' ? 70 : 28},168)">
      ${[[-16, -10], [2, -16], [17, -8]].map(([x, y]) => `<g transform="translate(${x},${y})"><circle r="13" fill="${K.tealL}" ${ol('stroke-width="5"')}/><text x="0" y="5" text-anchor="middle" font-family="DM Mono" font-weight="500" font-size="12" fill="${K.tealD}">AI</text></g>`).join('')}
      <path d="M-30 -2 Q-34 44 0 48 Q34 44 30 -2 Z" fill="${K.teal}" ${ol()}/><path d="M-30 -2 Q0 12 30 -2" fill="none" stroke="${K.ink}" stroke-width="5"/>
      <circle cx="0" cy="22" r="9" fill="${K.brass}" ${ol('stroke-width="4"')}/></g>` : '';
  const scissors = view === 'front' ? `<g transform="translate(-22,188) rotate(8)"><path d="M0 0 L-6 34 M0 0 L6 34" stroke="#9AA1B2" stroke-width="7" stroke-linecap="round"/><path d="M0 0 L-6 34 M0 0 L6 34" stroke="${K.ink}" stroke-width="2" stroke-linecap="round" opacity=".6"/><circle cx="-9" cy="-10" r="9" fill="none" stroke="${K.teal}" stroke-width="6"/><circle cx="9" cy="-10" r="9" fill="none" stroke="${K.teal}" stroke-width="6"/></g>` : '';
  const tape = view === 'front' ? `<g transform="translate(118,165)"><circle r="20" fill="${K.paper}" ${ol()}/><circle r="8" fill="${K.fur}" ${ol('stroke-width="5"')}/></g>` : '';
  return band + buckle + pocket + pouch + scissors + tape;
}
function tagShape(n, c, s = 1) {
  const dark = c === K.ink || c === '#3D4FE0';
  return `<g transform="scale(${s})"><path d="M-70 -30 L70 -30 L70 30 L-70 30 L-92 8 L-92 -8 Z" fill="${c}" ${ol()}/><circle cx="-74" cy="0" r="7" fill="${K.paper}" ${ol('stroke-width="4"')}/>
    <text x="8" y="12" text-anchor="middle" font-family="DM Mono" font-weight="500" font-size="34" fill="${dark ? '#fff' : K.ink}">${n}</text></g>`;
}

function front(expr, tag) {
  const armsUp = false, armsFwd = expr === 'focused' || expr === 'oops' || expr === 'proud';
  let s = `<defs><clipPath id="bodyclip-front"><ellipse cx="0" cy="130" rx="112" ry="100"/></clipPath></defs>`;
  // legs, then the body, then the arms
  s += `<ellipse cx="-56" cy="226" rx="46" ry="34" fill="${K.ink}"/><ellipse cx="56" cy="226" rx="46" ry="34" fill="${K.ink}"/>
    <ellipse cx="-58" cy="232" rx="20" ry="13" fill="#3C4150"/><ellipse cx="58" cy="232" rx="20" ry="13" fill="#3C4150"/>`;
  s += `<ellipse cx="0" cy="130" rx="112" ry="100" fill="${K.fur}" ${ol()}/><path d="M-120 62 Q0 22 120 62 L120 112 Q0 76 -120 112 Z" fill="${K.ink}" clip-path="url(#bodyclip-front)"/>`;
  s += belt('front');
  if (armsUp) s += `<ellipse cx="-118" cy="40" rx="32" ry="64" fill="${K.ink}" transform="rotate(-28 -118 40)"/><ellipse cx="118" cy="40" rx="32" ry="64" fill="${K.ink}" transform="rotate(28 118 40)"/>`;
  else if (armsFwd) s += `<ellipse cx="-62" cy="128" rx="32" ry="56" fill="${K.ink}" transform="rotate(-48 -62 128)"/><ellipse cx="62" cy="128" rx="32" ry="56" fill="${K.ink}" transform="rotate(48 62 128)"/>`;
  else s += `<ellipse cx="-110" cy="120" rx="32" ry="62" fill="${K.ink}" transform="rotate(22 -110 120)"/><ellipse cx="110" cy="120" rx="32" ry="62" fill="${K.ink}" transform="rotate(-22 110 120)"/>`;
  // what the paws hold
  if (expr === 'focused') s += `<g transform="translate(0,150) rotate(-8)"><rect x="-46" y="-26" width="92" height="56" rx="10" fill="${K.paper}" ${ol()}/><path d="M-30 -8 h40 M-30 6 h60" stroke="#9AA1B2" stroke-width="5" stroke-linecap="round"/>
      <g transform="translate(30,-40) rotate(35)"><rect x="-6" y="-40" width="12" height="62" rx="2" fill="${K.pencil}" ${ol('stroke-width="5"')}/><path d="M-6 22 L0 38 L6 22 Z" fill="#E9C9A0" ${ol('stroke-width="5"')}/></g></g>
      <circle cx="-30" cy="150" r="20" fill="${K.ink}"/><circle cx="34" cy="128" r="20" fill="${K.ink}"/>`;
  if (expr === 'oops') s += `<g transform="translate(0,140)"><rect x="-44" y="-18" width="52" height="46" rx="6" fill="${K.teal}" ${ol()}/><path d="M8 -18 L22 -8 L14 4 L26 14 L8 28" fill="${K.tealD}" ${ol()}/>
      <path d="M30 -2 c10 -10 18 6 28 -4 c10 -10 16 6 24 -2" fill="none" stroke="${K.ink}" stroke-width="5" stroke-linecap="round"/>
      <path d="M-4 -40 l10 -14 l2 10 l12 -12" fill="none" stroke="${K.spark}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
      ${[[-30, -70, 22], [-6, -92, 28], [24, -78, 20]].map(([x, y, r]) => `<circle cx="${x}" cy="${y}" r="${r}" fill="${K.smoke}" ${ol('stroke-width="5"')} opacity=".95"/>`).join('')}</g>
      <circle cx="-44" cy="150" r="20" fill="${K.ink}"/><circle cx="48" cy="150" r="20" fill="${K.ink}"/>`;
  if (expr === 'proud') { const tg = tag || { n: '#000', c: K.teal };
    s += `<g transform="translate(0,138) rotate(-6)">${tagShape(tg.n, tg.c, 1.25)}</g><circle cx="-96" cy="146" r="21" fill="${K.ink}"/><circle cx="96" cy="128" r="21" fill="${K.ink}"/>
      <path d="M-150 40 l-26 -14 M-158 76 l-30 0 M150 40 l26 -14 M158 76 l30 0" stroke="${K.ink}" stroke-width="6" stroke-linecap="round"/>`; }
  // head
  s += `<circle cx="-118" cy="-196" r="48" fill="${K.ink}"/><circle cx="118" cy="-196" r="48" fill="${K.ink}"/><circle cx="-118" cy="-196" r="22" fill="#3C4150"/><circle cx="118" cy="-196" r="22" fill="#3C4150"/>`;
  s += `<ellipse cx="0" cy="-96" rx="152" ry="130" fill="${K.fur}" ${ol()}/><path d="M-120 -30 Q0 40 120 -30" fill="none" stroke="${K.shade}" stroke-width="10" stroke-linecap="round" opacity=".7"/>`;
  s += `<rect x="-151" y="-106" width="40" height="22" fill="${K.teal}" ${ol('stroke-width="5"')}/><rect x="111" y="-106" width="40" height="22" fill="${K.teal}" ${ol('stroke-width="5"')}/>`;
  s += `<ellipse cx="-62" cy="-88" rx="42" ry="52" fill="${K.ink}" transform="rotate(22 -62 -88)"/><ellipse cx="62" cy="-88" rx="42" ry="52" fill="${K.ink}" transform="rotate(-22 62 -88)"/>`;
  s += eye(-62, -94, expr, -1) + eye(62, -94, expr, 1);
  s += `<rect x="-18" y="-102" width="36" height="14" rx="5" fill="${K.brass}" ${ol('stroke-width="5"')}/>` + goggleRing(-62, -94) + goggleRing(62, -94);
  s += `<circle cx="-104" cy="-28" r="17" fill="${K.blush}"/><circle cx="104" cy="-28" r="17" fill="${K.blush}"/>`;
  s += `<path d="M-14 -40 Q0 -48 14 -40 Q14 -28 0 -24 Q-14 -28 -14 -40 Z" fill="${K.ink}"/>`;
  if (expr === 'proud') s += `<path d="M-30 -12 Q0 30 30 -12 Z" fill="${K.ink}"/><path d="M-14 6 Q0 18 14 6 Q0 0 -14 6 Z" fill="${K.tongue}"/>`;
  else if (expr === 'oops') s += `<path d="M-24 -6 q6 -8 12 0 q6 8 12 0 q6 -8 12 0 q6 8 12 0" fill="none" stroke="${K.ink}" stroke-width="5" stroke-linecap="round" transform="translate(-6,0)"/>
      <path d="M128 -150 q12 20 0 30 q-12 -10 0 -30 Z" fill="${K.tealL}" ${ol('stroke-width="4"')}/>`;
  else s += `<path d="M0 -24 v6 M-20 -10 q10 12 20 0 q10 12 20 0" fill="none" stroke="${K.ink}" stroke-width="5" stroke-linecap="round"/>` +
      (expr === 'focused' ? `<path d="M10 -6 q8 18 20 4 q-4 -10 -20 -4 Z" fill="${K.tongue}" ${ol('stroke-width="4"')}/>` : '');
  return s;
}
function side() {
  let s = `<defs><clipPath id="bodyclip-side"><ellipse cx="0" cy="130" rx="96" ry="100"/></clipPath></defs>`;
  s += `<ellipse cx="-20" cy="226" rx="54" ry="34" fill="${K.ink}"/><ellipse cx="30" cy="232" rx="50" ry="30" fill="${K.ink}"/>`;
  s += `<ellipse cx="0" cy="130" rx="96" ry="100" fill="${K.fur}" ${ol()}/><path d="M-100 60 Q0 24 100 62 L100 112 Q0 78 -100 110 Z" fill="${K.ink}" clip-path="url(#bodyclip-side)"/>`;
  s += belt('side');
  s += `<ellipse cx="22" cy="122" rx="32" ry="62" fill="${K.ink}" transform="rotate(-14 22 122)"/>`;
  s += `<circle cx="-48" cy="-200" r="48" fill="${K.ink}"/><circle cx="-48" cy="-200" r="22" fill="#3C4150"/>`;
  s += `<ellipse cx="-6" cy="-96" rx="140" ry="130" fill="${K.fur}" ${ol()}/><path d="M120 -60 Q164 -46 150 -16 Q132 6 96 -2 Z" fill="${K.fur}" ${ol()}/>`;
  s += `<rect x="-146" y="-106" width="200" height="22" fill="${K.teal}" ${ol('stroke-width="5"')}/>`;
  s += `<ellipse cx="78" cy="-90" rx="34" ry="50" fill="${K.ink}" transform="rotate(-18 78 -90)"/>` + eye(84, -96, 'neutral', 1);
  s += `<ellipse cx="80" cy="-94" rx="22" ry="54" fill="${K.tealL}" fill-opacity=".38" stroke="${K.brass}" stroke-width="13"/><ellipse cx="80" cy="-94" rx="30" ry="62" fill="none" stroke="${K.ink}" stroke-width="${SW}"/>`;
  s += `<circle cx="104" cy="-24" r="15" fill="${K.blush}"/><path d="M146 -40 q12 -2 12 10 q-4 10 -14 6 Z" fill="${K.ink}"/><path d="M128 -6 q10 8 22 -2" fill="none" stroke="${K.ink}" stroke-width="5" stroke-linecap="round"/>`;
  return s;
}
function back() {
  let s = `<defs><clipPath id="bodyclip-back"><ellipse cx="0" cy="130" rx="112" ry="100"/></clipPath></defs>`;
  s += `<ellipse cx="-56" cy="226" rx="46" ry="34" fill="${K.ink}"/><ellipse cx="56" cy="226" rx="46" ry="34" fill="${K.ink}"/>`;
  s += `<ellipse cx="0" cy="130" rx="112" ry="100" fill="${K.fur}" ${ol()}/><path d="M-120 62 Q0 22 120 62 L120 112 Q0 76 -120 112 Z" fill="${K.ink}" clip-path="url(#bodyclip-back)"/>`;
  s += belt('back') + `<circle cx="0" cy="214" r="18" fill="${K.fur}" ${ol()}/>`;
  s += `<ellipse cx="-110" cy="120" rx="32" ry="62" fill="${K.ink}" transform="rotate(22 -110 120)"/><ellipse cx="110" cy="120" rx="32" ry="62" fill="${K.ink}" transform="rotate(-22 110 120)"/>`;
  s += `<circle cx="-118" cy="-196" r="48" fill="${K.ink}"/><circle cx="118" cy="-196" r="48" fill="${K.ink}"/>`;
  s += `<ellipse cx="0" cy="-96" rx="152" ry="130" fill="${K.fur}" ${ol()}/>`;
  s += `<g><rect x="-151" y="-106" width="302" height="22" fill="${K.teal}" ${ol('stroke-width="5"')}/><rect x="-16" y="-110" width="32" height="30" rx="6" fill="${K.brass}" ${ol('stroke-width="5"')}/></g>`;
  return s;
}
function panda(o = {}) { const v = o.view || 'front'; return v === 'side' ? side() : v === 'back' ? back() : front(o.expr || 'neutral', o.tag); }
function pandaSVG(o = {}, w = 400, h = 600, vb = '-200 -330 400 600') { return `<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="${vb}">${panda(o)}</svg>`; }
if (typeof module !== 'undefined') module.exports = { panda, pandaSVG, K, tagShape, goggleRing };
