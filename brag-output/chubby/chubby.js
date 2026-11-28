// Chubby: the @wierd_stuff_i_make mascot. A round, sitting panda inventor in a soft painted style.
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
function tagShape(n, c, s = 1) {
  const dark = c === K.ink || c === '#3D4FE0';
  return `<g transform="scale(${s})"><path d="M-70 -30 L70 -30 L70 30 L-70 30 L-92 8 L-92 -8 Z" fill="${c}" ${ol()}/><circle cx="-74" cy="0" r="7" fill="${K.paper}" ${ol('stroke-width="4"')}/>
    <text x="8" y="12" text-anchor="middle" font-family="DM Mono" font-weight="500" font-size="34" fill="${dark ? '#fff' : K.ink}">${n}</text></g>`;
}

// ---------- v3: soft painted style. A round, sitting panda: pear body, feet out with paw pads, droopy patches,
// closed happy eyes with lashes, warm key light from the left, fuzzy fur edges, no hard outline. Chubby keeps its gear.
const F = { fur: '#FBF8F2', furS: '#E2D9CC', dark: '#2E2A28', darkS: '#1A1716', darkL: '#4A433F', pad: '#B98868', padL: '#D2A586', pink: 'rgba(255,150,150,.45)' };
let UID = 0;
function defs3(u) {
  return `<defs>
  <filter id="fz${u}" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence type="fractalNoise" baseFrequency="0.22" numOctaves="2" seed="4" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="3.2" xChannelSelector="R" yChannelSelector="G" result="d"/><feGaussianBlur in="d" stdDeviation="0.7"/></filter>
  <filter id="soft${u}" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="14"/></filter>
  <radialGradient id="fw${u}" cx="38%" cy="32%" r="75%"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".55" stop-color="${F.fur}"/><stop offset="1" stop-color="${F.furS}"/></radialGradient>
  <radialGradient id="dk${u}" cx="35%" cy="30%" r="80%"><stop offset="0" stop-color="${F.darkL}"/><stop offset=".5" stop-color="${F.dark}"/><stop offset="1" stop-color="${F.darkS}"/></radialGradient>
  <radialGradient id="pd${u}" cx="40%" cy="35%" r="70%"><stop offset="0" stop-color="${F.padL}"/><stop offset="1" stop-color="${F.pad}"/></radialGradient>
  <radialGradient id="bl${u}"><stop offset="0" stop-color="rgba(255,140,140,.55)"/><stop offset="1" stop-color="rgba(255,140,140,0)"/></radialGradient>
  <linearGradient id="sh${u}" x1="0" x2="1" y1="0" y2=".3"><stop offset=".45" stop-color="rgba(60,40,30,0)"/><stop offset="1" stop-color="rgba(60,40,30,.22)"/></linearGradient>
  <linearGradient id="tl${u}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#22BFB0"/><stop offset="1" stop-color="#128F82"/></linearGradient>
  <radialGradient id="br${u}" cx="35%" cy="30%" r="80%"><stop offset="0" stop-color="#E6C470"/><stop offset="1" stop-color="#9C7A2C"/></radialGradient>
  </defs>`;
}
// a furry shape: the fill, a shade from the right, all through the fuzz filter
const fur = (u, d, kind = 'w') => `<g filter="url(#fz${u})"><path d="${d}" fill="url(#${kind === 'w' ? 'fw' : 'dk'}${u})"/><path d="${d}" fill="url(#sh${u})"/></g>`;
const ell = (cx, cy, rx, ry, rot = 0) => { const r = rot * Math.PI / 180, c = Math.cos(r), s = Math.sin(r), pts = [];
  for (let i = 0; i <= 48; i++) { const a = i / 48 * 2 * Math.PI, x = rx * Math.cos(a), y = ry * Math.sin(a); pts.push(`${(cx + x * c - y * s).toFixed(1)},${(cy + x * s + y * c).toFixed(1)}`); }
  return 'M' + pts.join(' L') + 'Z'; };
function paw(u, x, y, rot, flip) {   // a foot seen from the sole: dark foot, big pad, four toe beans
  return `<g transform="translate(${x},${y}) rotate(${rot})">${fur(u, ell(0, 0, 72, 60), 'd')}
    <ellipse cx="${flip * 4}" cy="14" rx="34" ry="28" fill="url(#pd${u})"/>${[[-36, -22], [-14, -36], [12, -38], [34, -24]].map(([a, b]) => `<ellipse cx="${a * flip}" cy="${b}" rx="10" ry="12" fill="url(#pd${u})"/>`).join('')}
    <ellipse cx="${flip * -6}" cy="6" rx="14" ry="8" fill="rgba(255,255,255,.18)"/></g>`;
}
function goggles3(u, y, s = 1) {
  const ring = (x) => `<circle cx="${x}" cy="${y}" r="${25 * s}" fill="rgba(160,235,225,.55)" stroke="url(#br${u})" stroke-width="${9 * s}"/><circle cx="${x}" cy="${y}" r="${30 * s}" fill="none" stroke="rgba(40,25,10,.35)" stroke-width="2"/>
    <path d="M${x - 12 * s} ${y - 8 * s} q6 -9 15 -10" stroke="#fff" stroke-width="${4 * s}" fill="none" stroke-linecap="round" opacity=".9"/>`;
  return `<rect x="-14" y="${y - 6}" width="28" height="11" rx="5" fill="url(#br${u})"/>` + ring(-40 * s) + ring(40 * s);
}
function face3(u, expr, cy) {
  // droopy patches, sloping down and out
  let s = `<path d="${ell(-60, cy + 6, 44, 34, 30)}" fill="url(#dk${u})" filter="url(#fz${u})"/><path d="${ell(60, cy + 6, 44, 34, -30)}" fill="url(#dk${u})" filter="url(#fz${u})"/>`;
  const lashes = (x, sd) => [0, 1, 2].map((i) => `<path d="M${x + sd * (22 + i * 2)} ${cy - 2 + i * 7} l${sd * 9} ${-3 + i * 3}" stroke="#F3EEE6" stroke-width="2.6" stroke-linecap="round"/>`).join('');
  const closed = (x, sd) => `<path d="M${x - 18} ${cy + 4} Q${x} ${cy - 12} ${x + 18} ${cy + 4}" fill="none" stroke="#F3EEE6" stroke-width="5" stroke-linecap="round"/>` + lashes(x, sd);
  const open = (x, sd, big) => { const r = big ? 17 : 14, pr = big ? 8 : 11; return `<ellipse cx="${x}" cy="${cy}" rx="${r}" ry="${r + 2}" fill="#fff"/><circle cx="${x + sd * 2}" cy="${cy + 2}" r="${pr}" fill="#1A1514"/><circle cx="${x - 3}" cy="${cy - 4}" r="${big ? 3 : 4.5}" fill="#fff"/><circle cx="${x + 4}" cy="${cy + 5}" r="2" fill="#fff"/>` + lashes(x, sd); };
  const half = (x, sd) => `<ellipse cx="${x}" cy="${cy + 3}" rx="15" ry="11" fill="#fff"/><circle cx="${x + 3}" cy="${cy + 5}" r="9" fill="#1A1514"/><circle cx="${x}" cy="${cy + 2}" r="3" fill="#fff"/><path d="M${x - 19} ${cy - 1} Q${x} ${cy - 6} ${x + 19} ${cy - 1}" stroke="#F3EEE6" stroke-width="4" fill="none" stroke-linecap="round"/>` + lashes(x, sd);
  const E = { neutral: closed, proud: closed, focused: half, oops: (x, sd) => open(x, sd, true), curious: (x, sd) => open(x, sd, false) }[expr] || closed;
  s += E(-60, -1) + E(60, 1);
  // brows: soft dark strokes on the fur, moving with the mood
  const bt = { neutral: 0, proud: -6, focused: 10, oops: -12, curious: -4 }[expr] ?? 0;
  s += [-1, 1].map((sd) => `<path d="M${sd * 44} ${cy - 46 + (expr === 'focused' ? 4 : 0)} q${sd * 16} ${-8} ${sd * 32} ${-2}" transform="rotate(${sd * -bt} ${sd * 60} ${cy - 48})" stroke="rgba(46,42,40,.75)" stroke-width="6" fill="none" stroke-linecap="round"/>`).join('');
  // blush, nose, mouth
  s += `<ellipse cx="-98" cy="${cy + 44}" rx="26" ry="16" fill="url(#bl${u})"/><ellipse cx="98" cy="${cy + 44}" rx="26" ry="16" fill="url(#bl${u})"/>`;
  s += `<path d="M-13 ${cy + 30} Q0 ${cy + 24} 13 ${cy + 30} Q12 ${cy + 40} 0 ${cy + 44} Q-12 ${cy + 40} -13 ${cy + 30} Z" fill="#1A1514"/><ellipse cx="-4" cy="${cy + 30}" rx="5" ry="2.5" fill="rgba(255,255,255,.55)"/>`;
  const my = cy + 52;
  if (expr === 'proud') s += `<path d="M-20 ${my - 2} Q0 ${my + 26} 20 ${my - 2} Z" fill="#3A1E1E"/><path d="M-10 ${my + 10} Q0 ${my + 18} 10 ${my + 10} Q0 ${my + 6} -10 ${my + 10} Z" fill="#FF8FA3"/>`;
  else if (expr === 'oops') s += `<path d="M-16 ${my + 4} q4 -6 8 0 q4 6 8 0 q4 -6 8 0 q4 6 8 0" stroke="#1A1514" stroke-width="3.5" fill="none" stroke-linecap="round" transform="translate(-0,0)"/><path d="M118 ${cy - 74} q10 16 0 24 q-10 -8 0 -24 Z" fill="#9EE6DC" stroke="#4FB3A7" stroke-width="2"/>`;
  else s += `<path d="M0 ${my - 8} v6 M-14 ${my} q7 8 14 0 q7 8 14 0" stroke="#1A1514" stroke-width="3.5" fill="none" stroke-linecap="round"/>` + (expr === 'focused' ? `<path d="M6 ${my + 3} q6 12 15 2 q-3 -7 -15 -2 Z" fill="#FF8FA3"/>` : '');
  return s;
}
function belt3(u, y = 128, view = 'front') {
  let s = `<g clip-path="url(#bc${u})"><rect x="-200" y="${y}" width="400" height="30" fill="url(#tl${u})"/><rect x="-200" y="${y}" width="400" height="5" fill="rgba(255,255,255,.25)"/></g>`;
  if (view === 'back') return s + `<g transform="translate(-30,${y + 16})"><circle r="19" fill="#E9E4DA"/><circle r="8" fill="#CFC6B8"/></g>`;
  if (view === 'front') s += `<rect x="-18" y="${y - 4}" width="36" height="38" rx="7" fill="url(#br${u})"/><rect x="-7" y="${y + 7}" width="14" height="16" rx="3" fill="rgba(60,40,10,.45)"/>
    <g transform="translate(-92,${y + 4})"><rect x="2" y="-52" width="12" height="58" rx="2" fill="#F2C14E"/><path d="M2 -52 L8 -68 L14 -52 Z" fill="#E9C9A0"/><path d="M6 -63 L8 -68 L10 -63 Z" fill="#2E2A28"/>
      <rect x="17" y="-42" width="14" height="50" rx="2" fill="#F3EBD8"/>${[0, 1, 2, 3].map((i) => `<path d="M17 ${-34 + i * 10} h6" stroke="#8A7F70" stroke-width="2.5"/>`).join('')}
      <rect x="-6" y="0" width="44" height="44" rx="10" fill="#0E6B61"/><rect x="-6" y="0" width="44" height="8" rx="4" fill="rgba(255,255,255,.15)"/></g>
    <g transform="translate(-40,${y + 30}) rotate(10)"><path d="M0 0 L-6 30 M0 0 L6 30" stroke="#A9AFBC" stroke-width="6" stroke-linecap="round"/><circle cx="-8" cy="-9" r="8" fill="none" stroke="#18A999" stroke-width="5"/><circle cx="8" cy="-9" r="8" fill="none" stroke="#18A999" stroke-width="5"/></g>`;
  s += `<g transform="translate(${view === 'side' ? 30 : 84},${y + 8})">${[[-15, -10], [2, -17], [16, -8]].map(([x, yy]) => `<g transform="translate(${x},${yy})"><circle r="12" fill="#9EE6DC" stroke="#4FB3A7" stroke-width="2.5"/><text y="4.5" text-anchor="middle" font-family="DM Mono" font-weight="500" font-size="11" fill="#0E6B61">AI</text></g>`).join('')}
    <path d="M-28 -2 Q-31 40 0 44 Q31 40 28 -2 Z" fill="url(#tl${u})"/><path d="M-28 -2 Q0 10 28 -2" fill="none" stroke="rgba(0,0,0,.25)" stroke-width="3"/><circle cx="0" cy="20" r="7" fill="url(#br${u})"/></g>`;
  if (view === 'front') s += `<g transform="translate(140,${y + 12})"><circle r="18" fill="#E9E4DA"/><circle r="7" fill="#CFC6B8"/></g>`;
  return s;
}
function hands(u, expr, tag) {
  // arms come from the shoulders and meet at the chest
  const armL = 'M-138 -6 C-160 40 -130 110 -60 112 C-20 112 -4 86 -4 60 C-6 30 -40 10 -70 -10 Z';
  const armR = 'M138 -6 C160 40 130 110 60 112 C20 112 4 86 4 60 C6 30 40 10 70 -10 Z';
  let s = '';
  if (expr === 'neutral') return s + fur(u, armL, 'd') + fur(u, armR, 'd') + fur(u, 'M-22 70 C-26 40 -14 4 0 -4 C14 4 26 40 22 70 C14 80 -14 80 -22 70 Z', 'd');   // paws together, like the reference
  if (expr === 'focused') s += `<g transform="translate(0,64) rotate(-8)"><rect x="-56" y="-30" width="112" height="66" rx="10" fill="#F6F1E8"/><rect x="-56" y="-30" width="112" height="66" rx="10" fill="url(#sh${u})"/><path d="M-36 -10 h48 M-36 8 h70" stroke="#B9B0A2" stroke-width="5" stroke-linecap="round"/>
      <g transform="translate(40,-46) rotate(35)"><rect x="-6" y="-42" width="12" height="64" rx="2" fill="#F2C14E"/><path d="M-6 22 L0 38 L6 22 Z" fill="#E9C9A0"/></g></g>`;
  if (expr === 'oops') s += `<g transform="translate(0,58)"><rect x="-50" y="-22" width="58" height="52" rx="7" fill="url(#tl${u})"/><path d="M8 -22 L24 -10 L15 4 L28 16 L8 30" fill="#0E6B61"/>
      <path d="M32 -2 c10 -10 18 6 28 -4 c10 -10 16 6 24 -2" fill="none" stroke="#5A524C" stroke-width="4" stroke-linecap="round"/><path d="M-6 -44 l10 -14 l2 10 l12 -12" fill="none" stroke="#FF8A3D" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
      ${[[-36, -76, 22], [-8, -98, 27], [24, -82, 19]].map(([x, y, r]) => `<circle cx="${x}" cy="${y}" r="${r}" fill="#C9CED8" opacity=".95" filter="url(#fz${u})"/>`).join('')}</g>`;
  if (expr === 'proud') { const tg = tag || { n: '#000', c: '#18A999' }; s += `<g transform="translate(0,70) rotate(-6)">${tagShape(tg.n, tg.c, 1.3)}</g>`;
    return fur(u, 'M-120 -6 C-160 30 -170 80 -130 96 C-110 100 -100 80 -108 60 C-112 40 -90 14 -80 -10 Z', 'd') + fur(u, 'M120 -6 C160 30 166 60 126 74 C106 78 98 60 104 42 C108 24 90 8 80 -10 Z', 'd') + s + `<circle cx="-122" cy="86" r="24" fill="url(#dk${u})" filter="url(#fz${u})"/><circle cx="118" cy="62" r="24" fill="url(#dk${u})" filter="url(#fz${u})"/>`; }
  return fur(u, armL, 'd') + fur(u, armR, 'd') + s + `<circle cx="${expr === 'proud' ? -122 : -58}" cy="${expr === 'proud' ? 84 : 92}" r="24" fill="url(#dk${u})" filter="url(#fz${u})"/><circle cx="${expr === 'proud' ? 118 : 58}" cy="${expr === 'proud' ? 60 : 70}" r="24" fill="url(#dk${u})" filter="url(#fz${u})"/>`;
}
function front(expr, tag) {
  const u = ++UID; const HCY = -118;
  let s = defs3(u) + `<defs><clipPath id="bc${u}"><path d="${ell(0, 112, 150, 140)}"/></clipPath></defs>`;
  s += `<ellipse cx="0" cy="262" rx="190" ry="24" fill="rgba(60,40,30,.22)" filter="url(#soft${u})"/>`;
  s += fur(u, 'M-112 24 C-118 -14 -66 -32 0 -32 C66 -32 118 -14 112 24 C150 84 172 176 146 226 C118 262 -118 262 -146 226 C-172 176 -150 84 -112 24 Z');          // the pear body
  s += `<g filter="url(#fz${u})"><path d="M-118 22 C-84 -34 84 -34 118 22 C128 56 104 78 80 64 C40 44 -40 44 -80 64 C-104 78 -128 56 -118 22 Z" fill="url(#dk${u})"/></g>`;    // shoulders
  s += `<ellipse cx="-20" cy="170" rx="90" ry="60" fill="rgba(255,255,255,.35)" filter="url(#soft${u})"/>`;
  s += belt3(u, 140) + paw(u, -118, 222, -18, -1) + paw(u, 118, 222, 18, 1);
  s += hands(u, expr, tag);
  // head
  s += `<g filter="url(#fz${u})"><circle cx="-108" cy="${HCY - 104}" r="36" fill="url(#dk${u})"/><circle cx="108" cy="${HCY - 104}" r="36" fill="url(#dk${u})"/></g><circle cx="-108" cy="${HCY - 104}" r="15" fill="${F.darkL}" opacity=".7"/><circle cx="108" cy="${HCY - 104}" r="15" fill="${F.darkL}" opacity=".7"/>`;
  s += fur(u, ell(0, HCY, 150, 128));
  s += `<ellipse cx="-50" cy="${HCY - 60}" rx="70" ry="40" fill="rgba(255,255,255,.5)" filter="url(#soft${u})"/>`;
  s += `<g>${goggles3(u, HCY - 96)}</g><path d="M-138 ${HCY - 96} Q-100 ${HCY - 112} -68 ${HCY - 100} M68 ${HCY - 100} Q100 ${HCY - 112} 138 ${HCY - 96}" stroke="url(#tl${u})" stroke-width="13" fill="none" stroke-linecap="round"/>`;
  s += face3(u, expr, HCY + 6);
  return s;
}
function side() {
  const u = ++UID; const HCY = -118;
  let s = defs3(u) + `<defs><clipPath id="bc${u}"><path d="${ell(0, 112, 130, 140)}"/></clipPath></defs>`;
  s += `<ellipse cx="0" cy="262" rx="170" ry="22" fill="rgba(60,40,30,.22)" filter="url(#soft${u})"/>`;
  s += fur(u, 'M-120 110 C-128 10 -90 -20 0 -24 C90 -20 128 10 124 110 C120 200 80 250 0 252 C-80 250 -118 200 -120 110 Z');
  s += `<g filter="url(#fz${u})"><path d="M-124 60 C-100 -10 110 -10 126 60 L126 20 C90 -40 -90 -40 -124 20 Z" fill="url(#dk${u})"/></g>`;
  s += belt3(u, 140, 'side');
  s += `<g transform="translate(80,226) rotate(8)">${fur(u, ell(0, 0, 86, 42), 'd')}<ellipse cx="62" cy="0" rx="14" ry="30" fill="url(#pd${u})"/></g>`;
  s += fur(u, 'M30 -10 C70 20 70 90 40 110 C10 120 -10 96 0 60 C8 30 0 10 30 -10 Z', 'd');
  s += `<circle cx="-50" cy="${HCY - 104}" r="36" fill="url(#dk${u})" filter="url(#fz${u})"/>`;
  s += fur(u, ell(0, HCY, 134, 126)) + fur(u, ell(124, HCY + 34, 40, 30));
  s += `<path d="M-120 ${HCY - 98} Q0 ${HCY - 124} 80 ${HCY - 100}" stroke="url(#tl${u})" stroke-width="13" fill="none" stroke-linecap="round"/><ellipse cx="78" cy="${HCY - 100}" rx="12" ry="24" fill="rgba(160,235,225,.55)" stroke="url(#br${u})" stroke-width="8" transform="rotate(-20 78 ${HCY - 100})"/>`;
  s += `<path d="${ell(76, HCY + 10, 40, 30, -26)}" fill="url(#dk${u})" filter="url(#fz${u})"/><path d="M62 ${HCY + 14} Q78 ${HCY} 94 ${HCY + 12}" fill="none" stroke="#F3EEE6" stroke-width="5" stroke-linecap="round"/>`;
  s += `<ellipse cx="96" cy="${HCY + 52}" rx="20" ry="12" fill="url(#bl${u})"/><path d="M152 ${HCY + 26} q10 0 10 9 q-4 8 -12 4 Z" fill="#1A1514"/><path d="M134 ${HCY + 54} q9 6 18 -2" stroke="#1A1514" stroke-width="3.5" fill="none" stroke-linecap="round"/>`;
  return s;
}
function back() {
  const u = ++UID; const HCY = -118;
  let s = defs3(u) + `<defs><clipPath id="bc${u}"><path d="${ell(0, 112, 150, 140)}"/></clipPath></defs>`;
  s += `<ellipse cx="0" cy="262" rx="190" ry="24" fill="rgba(60,40,30,.22)" filter="url(#soft${u})"/>`;
  s += `<g transform="translate(-120,236)">${fur(u, ell(0, 0, 60, 30), 'd')}</g><g transform="translate(120,236)">${fur(u, ell(0, 0, 60, 30), 'd')}</g>`;
  s += fur(u, 'M-112 24 C-118 -14 -66 -32 0 -32 C66 -32 118 -14 112 24 C150 84 172 176 146 226 C118 262 -118 262 -146 226 C-172 176 -150 84 -112 24 Z');
  s += `<g filter="url(#fz${u})"><path d="M-118 22 C-84 -34 84 -34 118 22 C128 56 104 78 80 64 C40 44 -40 44 -80 64 C-104 78 -128 56 -118 22 Z" fill="url(#dk${u})"/></g>`;
  s += belt3(u, 140, 'back') + `<circle cx="0" cy="226" r="20" fill="url(#fw${u})" filter="url(#fz${u})"/>`;
  s += fur(u, 'M-138 -6 C-168 40 -150 120 -112 130 C-96 100 -100 40 -84 0 Z', 'd') + fur(u, 'M138 -6 C168 40 150 120 112 130 C96 100 100 40 84 0 Z', 'd');
  s += `<g filter="url(#fz${u})"><circle cx="-108" cy="${HCY - 104}" r="36" fill="url(#dk${u})"/><circle cx="108" cy="${HCY - 104}" r="36" fill="url(#dk${u})"/></g>`;
  s += fur(u, ell(0, HCY, 150, 128));
  s += `<path d="M-142 ${HCY - 90} Q0 ${HCY - 120} 142 ${HCY - 90}" stroke="url(#tl${u})" stroke-width="14" fill="none" stroke-linecap="round"/><rect x="-14" y="${HCY - 120}" width="28" height="22" rx="6" fill="url(#br${u})"/>`;
  return s;
}

function panda(o = {}) { const v = o.view || 'front'; return v === 'side' ? side() : v === 'back' ? back() : front(o.expr || 'neutral', o.tag); }
function pandaSVG(o = {}, w = 400, h = 600, vb = '-200 -290 400 600') { return `<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="${vb}">${panda(o)}</svg>`; }
if (typeof module !== 'undefined') module.exports = { panda, pandaSVG, K, tagShape, goggleRing };
