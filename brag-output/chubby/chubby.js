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

// ---------- v2: natural proportions (head ~ body), goggles pushed up on the forehead, expressive eyes ----------
const HY = -140, HRX = 126, HRY = 106;           // head centre and radii
const BY = 92, BRX = 124, BRY = 140;             // body
const GY = -222, GR = 26;                         // goggles on the forehead
// the belt was drawn for the v1 body (cy 130, band at y 148-182): place it on the v2 body
const beltOn = (view) => `<g transform="translate(0,-24) scale(1.1,1)">${belt(view).replace(/url\(#bodyclip-(\w+)\)/g, 'url(#beltclip-$1)')}</g>`;
const beltClip = (view) => `<clipPath id="beltclip-${view}"><ellipse cx="0" cy="${BY + 24}" rx="${BRX / 1.1}" ry="${BRY}"/></clipPath>`;

// eyes: a white eye in the black patch, a big pupil, two highlights, a lid and a brow on the fur above. Every expression moves all of them.
function eyeV2(x, y, expr, s) {   // s = -1 left, +1 right
  const brow = { neutral: [0, -8], focused: [14 * s, 6], proud: [-6 * s, -16], oops: [-14 * s, -14] }[expr] || [0, -8];
  const by = y - 44 + brow[1];
  let out = `<path d="M${x - 20} ${by + 4 * s * 0} Q${x} ${by - 9} ${x + 20} ${by}" transform="rotate(${brow[0]} ${x} ${by})" fill="none" stroke="${K.ink}" stroke-width="9" stroke-linecap="round"/>`;
  if (expr === 'proud') return out + `<path d="M${x - 15} ${y + 5} Q${x} ${y - 13} ${x + 15} ${y + 5}" fill="none" stroke="#fff" stroke-width="6.5" stroke-linecap="round"/>`;
  const r = expr === 'oops' ? 18 : 16, pr = expr === 'oops' ? 6.5 : 10.5, px = x + (expr === 'focused' ? 4 * s * 0 + 4 : s * 1.5), py = y + (expr === 'focused' ? 5 : 1);
  out += `<circle cx="${x}" cy="${y}" r="${r}" fill="#fff"/><circle cx="${px}" cy="${py}" r="${pr}" fill="${K.ink}"/>
    <circle cx="${px - pr * .45}" cy="${py - pr * .5}" r="${expr === 'oops' ? 2.6 : 4}" fill="#fff"/><circle cx="${px + pr * .45}" cy="${py + pr * .35}" r="1.8" fill="#fff"/>`;
  if (expr === 'focused') out += `<path d="M${x - r - 2} ${y - 2} L${x + r + 2} ${y - 2} L${x + r + 2} ${y - r - 4} L${x - r - 2} ${y - r - 4} Z" fill="${K.ink}"/><path d="M${x - r} ${y - 2} L${x + r} ${y - 2}" stroke="#fff" stroke-width="3" opacity=".5"/>`;
  return out;
}
function goggleUp(x, y, r = GR) {   // a ring seen from above the brow: the lens tilts up, so it is a slightly flattened ellipse
  return `<ellipse cx="${x}" cy="${y}" rx="${r + 7}" ry="${r + 4}" fill="none" stroke="${K.ink}" stroke-width="${SW}"/>
    <ellipse cx="${x}" cy="${y}" rx="${r}" ry="${r - 3}" fill="${K.tealL}" fill-opacity=".55" stroke="${K.brass}" stroke-width="10"/>
    <ellipse cx="${x}" cy="${y}" rx="${r - 6}" ry="${r - 9}" fill="none" stroke="${K.brassD}" stroke-width="2"/>
    <path d="M${x - r * .5} ${y - r * .25} A ${r * .6} ${r * .5} 0 0 1 ${x + r * .05} ${y - r * .5}" fill="none" stroke="#fff" stroke-width="4.5" stroke-linecap="round" opacity=".9"/>`;
}
function headFront(expr) {
  let s = `<circle cx="-100" cy="-228" r="40" fill="${K.ink}"/><circle cx="100" cy="-228" r="40" fill="${K.ink}"/><circle cx="-100" cy="-228" r="18" fill="#3C4150"/><circle cx="100" cy="-228" r="18" fill="#3C4150"/>`;
  s += `<ellipse cx="0" cy="${HY}" rx="${HRX}" ry="${HRY}" fill="${K.fur}" ${ol()}/><path d="M-96 -72 Q0 -30 96 -72" fill="none" stroke="${K.shade}" stroke-width="9" stroke-linecap="round" opacity=".7"/>`;
  // goggles up on the forehead, strap round the head
  const hw = HRX * Math.sqrt(1 - Math.pow((GY - HY) / HRY, 2));
  s += `<rect x="${-hw}" y="${GY - 10}" width="${hw - 70}" height="20" fill="${K.teal}" ${ol('stroke-width="5"')}/><rect x="70" y="${GY - 10}" width="${hw - 70}" height="20" fill="${K.teal}" ${ol('stroke-width="5"')}/>`;
  s += `<rect x="-14" y="${GY - 7}" width="28" height="13" rx="5" fill="${K.brass}" ${ol('stroke-width="4.5"')}/>` + goggleUp(-44, GY) + goggleUp(44, GY);
  // the patches and the eyes
  s += `<ellipse cx="-47" cy="-134" rx="31" ry="40" fill="${K.ink}" transform="rotate(24 -47 -134)"/><ellipse cx="47" cy="-134" rx="31" ry="40" fill="${K.ink}" transform="rotate(-24 47 -134)"/>`;
  s += eyeV2(-46, -138, expr, -1) + eyeV2(46, -138, expr, 1);
  s += `<circle cx="-86" cy="-92" r="15" fill="${K.blush}"/><circle cx="86" cy="-92" r="15" fill="${K.blush}"/>`;
  s += `<path d="M-12 -100 Q0 -107 12 -100 Q12 -90 0 -86 Q-12 -90 -12 -100 Z" fill="${K.ink}"/>`;
  if (expr === 'proud') s += `<path d="M-26 -76 Q0 -40 26 -76 Z" fill="${K.ink}"/><path d="M-12 -59 Q0 -50 12 -59 Q0 -64 -12 -59 Z" fill="${K.tongue}"/>`;
  else if (expr === 'oops') s += `<path d="M-22 -70 q5.5 -7 11 0 q5.5 7 11 0 q5.5 -7 11 0 q5.5 7 11 0" fill="none" stroke="${K.ink}" stroke-width="5" stroke-linecap="round" transform="translate(-0,0)"/>
      <path d="M112 -190 q11 18 0 27 q-11 -9 0 -27 Z" fill="${K.tealL}" ${ol('stroke-width="4"')}/>`;
  else s += `<path d="M0 -86 v5 M-17 -74 q8.5 10 17 0 q8.5 10 17 0" fill="none" stroke="${K.ink}" stroke-width="5" stroke-linecap="round"/>` +
      (expr === 'focused' ? `<path d="M8 -71 q7 16 18 3 q-4 -9 -18 -3 Z" fill="${K.tongue}" ${ol('stroke-width="4"')}/>` : '');
  return s;
}
function bodyFront(expr, tag, view = 'front') {
  const fwd = expr === 'focused' || expr === 'oops' || expr === 'proud';
  let s = `<defs><clipPath id="bodyclip2-${view}"><ellipse cx="0" cy="${BY}" rx="${BRX}" ry="${BRY}"/></clipPath>${beltClip(view)}</defs>`;
  s += `<ellipse cx="-62" cy="228" rx="50" ry="34" fill="${K.ink}"/><ellipse cx="62" cy="228" rx="50" ry="34" fill="${K.ink}"/><ellipse cx="-64" cy="235" rx="22" ry="13" fill="#3C4150"/><ellipse cx="64" cy="235" rx="22" ry="13" fill="#3C4150"/>`;
  s += `<ellipse cx="0" cy="${BY}" rx="${BRX}" ry="${BRY}" fill="${K.fur}" ${ol()}/>`;
  s += `<path d="M-140 -10 Q0 -60 140 -10 L140 44 Q0 0 -140 44 Z" fill="${K.ink}" clip-path="url(#bodyclip2-${view})"/>`;
  s += beltOn(view);
  if (fwd) s += `<ellipse cx="-70" cy="78" rx="36" ry="72" fill="${K.ink}" transform="rotate(-42 -70 78)"/><ellipse cx="70" cy="78" rx="36" ry="72" fill="${K.ink}" transform="rotate(42 70 78)"/>`;
  else s += `<ellipse cx="-122" cy="70" rx="36" ry="78" fill="${K.ink}" transform="rotate(16 -122 70)"/><ellipse cx="122" cy="70" rx="36" ry="78" fill="${K.ink}" transform="rotate(-16 122 70)"/>`;
  if (expr === 'focused') s += `<g transform="translate(0,108) rotate(-8)"><rect x="-50" y="-30" width="100" height="62" rx="10" fill="${K.paper}" ${ol()}/><path d="M-32 -10 h44 M-32 6 h64" stroke="#9AA1B2" stroke-width="5" stroke-linecap="round"/>
      <g transform="translate(34,-44) rotate(35)"><rect x="-6" y="-42" width="12" height="64" rx="2" fill="${K.pencil}" ${ol('stroke-width="5"')}/><path d="M-6 22 L0 38 L6 22 Z" fill="#E9C9A0" ${ol('stroke-width="5"')}/></g></g>
      <circle cx="-34" cy="112" r="22" fill="${K.ink}"/><circle cx="38" cy="88" r="22" fill="${K.ink}"/>`;
  if (expr === 'oops') s += `<g transform="translate(0,100)"><rect x="-48" y="-20" width="56" height="50" rx="6" fill="${K.teal}" ${ol()}/><path d="M8 -20 L24 -8 L15 5 L28 16 L8 30" fill="${K.tealD}" ${ol()}/>
      <path d="M32 -2 c10 -10 18 6 28 -4 c10 -10 16 6 24 -2" fill="none" stroke="${K.ink}" stroke-width="5" stroke-linecap="round"/>
      <path d="M-4 -42 l10 -14 l2 10 l12 -12" fill="none" stroke="${K.spark}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
      ${[[-34, -74, 22], [-8, -94, 26], [22, -80, 19]].map(([x, y, r]) => `<circle cx="${x}" cy="${y}" r="${r}" fill="${K.smoke}" ${ol('stroke-width="5"')}/>`).join('')}</g>
      <circle cx="-48" cy="112" r="22" fill="${K.ink}"/><circle cx="52" cy="112" r="22" fill="${K.ink}"/>`;
  if (expr === 'proud') { const tg = tag || { n: '#000', c: K.teal };
    s += `<g transform="translate(0,98) rotate(-6)">${tagShape(tg.n, tg.c, 1.3)}</g><circle cx="-104" cy="108" r="22" fill="${K.ink}"/><circle cx="104" cy="88" r="22" fill="${K.ink}"/>
      <path d="M-170 0 l-26 -14 M-178 36 l-30 0 M170 0 l26 -14 M178 36 l30 0" stroke="${K.ink}" stroke-width="6" stroke-linecap="round"/>`; }
  return s;
}
function front(expr, tag) { return bodyFront(expr, tag) + headFront(expr); }
function side() {
  let s = `<defs><clipPath id="bodyclip2-side"><ellipse cx="0" cy="${BY}" rx="108" ry="${BRY}"/></clipPath>${beltClip('side')}</defs>`;
  s += `<ellipse cx="-24" cy="228" rx="58" ry="34" fill="${K.ink}"/><ellipse cx="34" cy="234" rx="54" ry="30" fill="${K.ink}"/>`;
  s += `<ellipse cx="0" cy="${BY}" rx="108" ry="${BRY}" fill="${K.fur}" ${ol()}/><path d="M-130 -12 Q0 -58 130 -8 L130 46 Q0 4 -130 44 Z" fill="${K.ink}" clip-path="url(#bodyclip2-side)"/>`;
  s += beltOn('side') + `<ellipse cx="24" cy="72" rx="36" ry="78" fill="${K.ink}" transform="rotate(-12 24 72)"/>`;
  s += `<circle cx="-40" cy="-232" r="40" fill="${K.ink}"/><circle cx="-40" cy="-232" r="18" fill="#3C4150"/>`;
  s += `<ellipse cx="-4" cy="${HY}" rx="118" ry="${HRY}" fill="${K.fur}" ${ol()}/><path d="M100 -112 Q140 -100 128 -74 Q112 -56 82 -62 Z" fill="${K.fur}" ${ol()}/>`;
  { const hw = 118 * Math.sqrt(1 - Math.pow((GY - HY) / HRY, 2)); s += `<rect x="${-4 - hw + 2}" y="${GY - 10}" width="${hw + 52}" height="20" fill="${K.teal}" ${ol('stroke-width="5"')}/>`; }
  s += `<ellipse cx="64" cy="${GY}" rx="13" ry="28" fill="${K.tealL}" fill-opacity=".55" stroke="${K.brass}" stroke-width="10" transform="rotate(-20 64 ${GY})"/><ellipse cx="64" cy="${GY}" rx="20" ry="35" fill="none" stroke="${K.ink}" stroke-width="${SW}" transform="rotate(-20 64 ${GY})"/>`;
  s += `<ellipse cx="66" cy="-134" rx="27" ry="40" fill="${K.ink}" transform="rotate(-18 66 -134)"/>` + eyeV2(72, -138, 'neutral', 1);
  s += `<circle cx="88" cy="-88" r="13" fill="${K.blush}"/><path d="M126 -100 q11 -2 11 9 q-4 9 -13 5 Z" fill="${K.ink}"/><path d="M110 -70 q9 7 20 -2" fill="none" stroke="${K.ink}" stroke-width="5" stroke-linecap="round"/>`;
  return s;
}
function back() {
  let s = `<defs><clipPath id="bodyclip2-back"><ellipse cx="0" cy="${BY}" rx="${BRX}" ry="${BRY}"/></clipPath>${beltClip('back')}</defs>`;
  s += `<ellipse cx="-62" cy="228" rx="50" ry="34" fill="${K.ink}"/><ellipse cx="62" cy="228" rx="50" ry="34" fill="${K.ink}"/>`;
  s += `<ellipse cx="0" cy="${BY}" rx="${BRX}" ry="${BRY}" fill="${K.fur}" ${ol()}/><path d="M-140 -10 Q0 -60 140 -10 L140 44 Q0 0 -140 44 Z" fill="${K.ink}" clip-path="url(#bodyclip2-back)"/>`;
  s += beltOn('back') + `<circle cx="0" cy="206" r="18" fill="${K.fur}" ${ol()}/>`;
  s += `<ellipse cx="-122" cy="70" rx="36" ry="78" fill="${K.ink}" transform="rotate(16 -122 70)"/><ellipse cx="122" cy="70" rx="36" ry="78" fill="${K.ink}" transform="rotate(-16 122 70)"/>`;
  s += `<circle cx="-100" cy="-228" r="40" fill="${K.ink}"/><circle cx="100" cy="-228" r="40" fill="${K.ink}"/>`;
  s += `<ellipse cx="0" cy="${HY}" rx="${HRX}" ry="${HRY}" fill="${K.fur}" ${ol()}/>`;
  const hw = HRX * Math.sqrt(1 - Math.pow((GY - HY) / HRY, 2));
  s += `<rect x="${-hw}" y="${GY - 10}" width="${hw * 2}" height="20" fill="${K.teal}" ${ol('stroke-width="5"')}/><rect x="-14" y="${GY - 13}" width="28" height="26" rx="6" fill="${K.brass}" ${ol('stroke-width="5"')}/>`;
  return s;
}

function panda(o = {}) { const v = o.view || 'front'; return v === 'side' ? side() : v === 'back' ? back() : front(o.expr || 'neutral', o.tag); }
function pandaSVG(o = {}, w = 400, h = 600, vb = '-200 -330 400 600') { return `<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="${vb}">${panda(o)}</svg>`; }
if (typeof module !== 'undefined') module.exports = { panda, pandaSVG, K, tagShape, goggleRing };
