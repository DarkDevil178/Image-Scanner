// Chubby: "Small Panda... Big Happiness!" A round, soft, sitting panda in a warm painted style.
// panda({ view: 'front'|'side'|'back'|'q34', face, arms, legs: 'sit'|'jump'|'lie', extras: [...], tilt }) -> SVG inner markup.
// Drawn around the origin: the ground line is y = 270, the box is -260..260 x -300..300.
const P = { black: '#2D2D2D', blackS: '#1C1C1C', blackL: '#4A4646', white: '#F8F8F8', whiteS: '#E6DED3', brown: '#A67C52', brownL: '#C9A27A', pink: '#F7C8C8', green: '#8BC34A', greenD: '#5E9A2E', heart: '#F0707E', gold: '#F2C14E', ink: '#5A3A22' };
let UID = 0;
const ell = (cx, cy, rx, ry, rot = 0) => { const r = rot * Math.PI / 180, c = Math.cos(r), s = Math.sin(r), p = [];
  for (let i = 0; i <= 48; i++) { const a = i / 48 * 2 * Math.PI, x = rx * Math.cos(a), y = ry * Math.sin(a); p.push(`${(cx + x * c - y * s).toFixed(1)},${(cy + x * s + y * c).toFixed(1)}`); }
  return 'M' + p.join(' L') + 'Z'; };
function defs(u) {
  return `<defs>
  <filter id="fz${u}" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence type="fractalNoise" baseFrequency="0.24" numOctaves="2" seed="7" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="3.4" xChannelSelector="R" yChannelSelector="G" result="d"/><feGaussianBlur in="d" stdDeviation="0.6"/></filter>
  <filter id="sf${u}" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="14"/></filter>
  <radialGradient id="w${u}" cx="38%" cy="30%" r="78%"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".55" stop-color="${P.white}"/><stop offset="1" stop-color="${P.whiteS}"/></radialGradient>
  <radialGradient id="k${u}" cx="34%" cy="28%" r="82%"><stop offset="0" stop-color="${P.blackL}"/><stop offset=".5" stop-color="${P.black}"/><stop offset="1" stop-color="${P.blackS}"/></radialGradient>
  <radialGradient id="pd${u}" cx="40%" cy="35%" r="70%"><stop offset="0" stop-color="${P.brownL}"/><stop offset="1" stop-color="${P.brown}"/></radialGradient>
  <radialGradient id="bl${u}"><stop offset="0" stop-color="rgba(247,160,170,.75)"/><stop offset="1" stop-color="rgba(247,160,170,0)"/></radialGradient>
  <linearGradient id="sh${u}" x1="0" x2="1" y1="0" y2=".35"><stop offset=".45" stop-color="rgba(120,80,40,0)"/><stop offset="1" stop-color="rgba(120,80,40,.2)"/></linearGradient>
  <radialGradient id="ir${u}" cx="45%" cy="38%" r="65%"><stop offset="0" stop-color="#6B4428"/><stop offset=".55" stop-color="#33200F"/><stop offset="1" stop-color="#120A05"/></radialGradient>
  </defs>`;
}
const fur = (u, d, k = 'w') => `<g filter="url(#fz${u})"><path d="${d}" fill="url(#${k}${u})"/><path d="${d}" fill="url(#sh${u})"/></g>`;
const blob = (u, cx, cy, rx, ry, rot = 0, k = 'k') => fur(u, ell(cx, cy, rx, ry, rot), k);

// ---------------- the face ----------------
function face(u, f, cx, cy, s = 1, look = 0) {   // f: calm happy excited wink thinking surprised sad shy sleep eat; look: horizontal shift for 3/4 and side
  const X = (x) => cx + x * s + look, Y = (y) => cy + y * s, S = (v) => v * s;
  let o = '';
  // droopy patches
  o += fur(u, ell(X(-56), Y(6), S(44), S(33), 30), 'k') + fur(u, ell(X(56), Y(6), S(44), S(33), -30), 'k');
  const arcUp = (x) => `<path d="M${X(x - 17)} ${Y(8)} Q${X(x)} ${Y(-9)} ${X(x + 17)} ${Y(8)}" fill="none" stroke="#FBF7F1" stroke-width="${S(5.5)}" stroke-linecap="round"/>`;
  const arcDown = (x) => `<path d="M${X(x - 16)} ${Y(0)} Q${X(x)} ${Y(12)} ${X(x + 16)} ${Y(0)}" fill="none" stroke="#FBF7F1" stroke-width="${S(5)}" stroke-linecap="round"/>`;
  const sadArc = (x, sd) => `<path d="M${X(x - 16)} ${Y(8 + sd * -4)} Q${X(x)} ${Y(-2)} ${X(x + 16)} ${Y(8 + sd * 4)}" fill="none" stroke="#FBF7F1" stroke-width="${S(5)}" stroke-linecap="round" transform="rotate(${sd * 14} ${X(x)} ${Y(4)})"/>`;
  const open = (x, dx = 0, dy = 0, big = 1) => { const rx = S(15 * big), ry = S(17 * big), ix = X(x + dx), iy = Y(4 + dy);
    return `<ellipse cx="${X(x)}" cy="${Y(4)}" rx="${rx}" ry="${ry}" fill="#FFFDF9"/><circle cx="${ix}" cy="${iy}" r="${S(11 * big)}" fill="url(#ir${u})"/><circle cx="${ix}" cy="${iy}" r="${S(5.5 * big)}" fill="#0A0504"/>
      <ellipse cx="${ix - S(4)}" cy="${iy - S(5)}" rx="${S(4.2)}" ry="${S(5)}" fill="#fff"/><circle cx="${ix + S(4.5)}" cy="${iy + S(4)}" r="${S(1.8)}" fill="#fff"/>`; };
  const E = {
    calm: () => arcDown(-56) + arcDown(56), happy: () => arcUp(-56) + arcUp(56), excited: () => arcUp(-56) + arcUp(56),
    wink: () => open(-56, 2, -1) + arcUp(56), thinking: () => open(-56, 5, -6) + open(56, 5, -6), surprised: () => open(-56, 0, 0, 1.12) + open(56, 0, 0, 1.12),
    sad: () => sadArc(-56, -1) + sadArc(56, 1), shy: () => arcUp(-56) + arcUp(56), sleep: () => arcDown(-56) + arcDown(56), eat: () => arcUp(-56) + arcUp(56),
  }[f] || (() => arcUp(-56) + arcUp(56));
  o += E();
  // blush (stronger when shy)
  const bl = f === 'shy' ? 1.4 : 1;
  o += `<ellipse cx="${X(-92)}" cy="${Y(44)}" rx="${S(26 * bl)}" ry="${S(15 * bl)}" fill="url(#bl${u})"/><ellipse cx="${X(92)}" cy="${Y(44)}" rx="${S(26 * bl)}" ry="${S(15 * bl)}" fill="url(#bl${u})"/>`;
  // nose
  o += `<path d="M${X(-12)} ${Y(28)} Q${X(0)} ${Y(22)} ${X(12)} ${Y(28)} Q${X(11)} ${Y(37)} ${X(0)} ${Y(41)} Q${X(-11)} ${Y(37)} ${X(-12)} ${Y(28)} Z" fill="#1E1A18"/><ellipse cx="${X(-3)}" cy="${Y(28)}" rx="${S(4.5)}" ry="${S(2.2)}" fill="rgba(255,255,255,.6)"/>`;
  // mouth
  const my = 50, st = `stroke="#3A2A20" stroke-width="${S(3.4)}" fill="none" stroke-linecap="round"`;
  const M = {
    excited: `<path d="M${X(-24)} ${Y(my - 4)} Q${X(0)} ${Y(my + 34)} ${X(24)} ${Y(my - 4)} Z" fill="#5A2A22"/><path d="M${X(-12)} ${Y(my + 12)} Q${X(0)} ${Y(my + 22)} ${X(12)} ${Y(my + 12)} Q${X(0)} ${Y(my + 7)} ${X(-12)} ${Y(my + 12)} Z" fill="#F28C9A"/>`,
    surprised: `<ellipse cx="${X(0)}" cy="${Y(my + 6)}" rx="${S(8)}" ry="${S(10)}" fill="#5A2A22"/>`,
    thinking: `<path d="M${X(-8)} ${Y(my + 4)} Q${X(2)} ${Y(my)} ${X(10)} ${Y(my + 4)}" ${st}/>`,
    sad: `<path d="M${X(-12)} ${Y(my + 8)} Q${X(0)} ${Y(my - 2)} ${X(12)} ${Y(my + 8)}" ${st}/>`,
    eat: `<path d="M${X(-14)} ${Y(my)} q${S(7)} ${S(8)} ${S(14)} 0 q${S(7)} ${S(8)} ${S(14)} 0" ${st}/><ellipse cx="${X(16)}" cy="${Y(my + 4)}" rx="${S(7)}" ry="${S(5)}" fill="${P.green}"/>`,
  }[f] || `<path d="M${X(0)} ${Y(my - 8)} v${S(5)} M${X(-14)} ${Y(my)} q${S(7)} ${S(8)} ${S(14)} 0 q${S(7)} ${S(8)} ${S(14)} 0" ${st}/>`;
  return o + M;
}
// ---------------- parts ----------------
function paw(u, x, y, rot, flip) {
  return `<g transform="translate(${x},${y}) rotate(${rot})">${blob(u, 0, 0, 70, 58)}
    <ellipse cx="${flip * 4}" cy="14" rx="33" ry="27" fill="url(#pd${u})"/>${[[-35, -21], [-13, -35], [12, -37], [33, -23]].map(([a, b]) => `<ellipse cx="${a * flip}" cy="${b}" rx="9.5" ry="11.5" fill="url(#pd${u})"/>`).join('')}</g>`;
}
const handPad = (u, x, y, r = 24) => blob(u, x, y, r, r * .95);
function headFront(u, f, hx, hy, q = 0) {   // q: 3/4 turn (0..1)
  let s = blob(u, hx - 112 + q * 26, hy - 100, 35, 34) + blob(u, hx + 112 + q * 8, hy - 100, 35, 34);
  s += `<circle cx="${hx - 112 + q * 26}" cy="${hy - 100}" r="14" fill="${P.blackL}" opacity=".6"/><circle cx="${hx + 112 + q * 8}" cy="${hy - 100}" r="14" fill="${P.blackL}" opacity=".6"/>`;
  s += fur(u, ell(hx, hy, 152, 128));
  s += `<ellipse cx="${hx - 46}" cy="${hy - 64}" rx="72" ry="40" fill="rgba(255,255,255,.55)" filter="url(#sf${u})"/>`;
  s += `<path d="M${hx - 10} ${hy - 124} q6 -14 14 -2 q6 -12 12 2" stroke="${P.whiteS}" stroke-width="5" fill="none" stroke-linecap="round"/>`;   // a little fluff tuft
  return s + face(u, f, hx, hy + 8, 1 - q * .08, q * 30);
}
const BODY = 'M-112 24 C-118 -14 -66 -32 0 -32 C66 -32 118 -14 112 24 C150 84 172 176 146 226 C118 262 -118 262 -146 226 C-172 176 -150 84 -112 24 Z';
const COLLAR = 'M-118 22 C-84 -34 84 -34 118 22 C128 56 104 78 80 64 C40 44 -40 44 -80 64 C-104 78 -128 56 -118 22 Z';
function arms(u, a) {
  const L = 'M-138 -6 C-160 40 -130 110 -60 112 C-20 112 -4 86 -4 60 C-6 30 -40 10 -70 -10 Z', R = 'M138 -6 C160 40 130 110 60 112 C20 112 4 86 4 60 C6 30 40 10 70 -10 Z';
  const prayPaws = 'M-24 72 C-28 40 -14 4 0 -6 C14 4 28 40 24 72 C14 82 -14 82 -24 72 Z';
  if (a === 'pray') return fur(u, L, 'k') + fur(u, R, 'k') + fur(u, prayPaws, 'k') + `<path d="M0 -2 L0 70" stroke="${P.blackS}" stroke-width="2.5" opacity=".6"/>`;
  if (a === 'up') return blob(u, -150, -50, 34, 78, 32) + blob(u, 150, -50, 34, 78, -32) + handPad(u, -184, -112) + handPad(u, 184, -112) +
      `<ellipse cx="-184" cy="-112" rx="12" ry="10" fill="url(#pd${u})"/><ellipse cx="184" cy="-112" rx="12" ry="10" fill="url(#pd${u})"/>`;
  if (a === 'cheeks') return blob(u, -112, 10, 36, 70, 10) + blob(u, 112, 10, 36, 70, -10) + '|||' + blob(u, -100, -40, 30, 54, 12) + blob(u, 100, -40, 30, 54, -12) + handPad(u, -90, -78, 28) + handPad(u, 90, -78, 28);
  if (a === 'chin') return fur(u, L, 'k') + blob(u, 96, 10, 34, 62, -20) + handPad(u, -30, 104, 24) + '|||' + blob(u, 66, -30, 28, 50, -40) + handPad(u, 34, -62, 25);
  if (a === 'wave') return fur(u, L, 'k') + handPad(u, -40, 100, 24) + blob(u, 150, -60, 34, 76, -24) + handPad(u, 176, -122, 26) + `<ellipse cx="176" cy="-122" rx="12" ry="10" fill="url(#pd${u})"/>` +
      `<path d="M212 -150 q14 10 10 26 M222 -176 q22 16 16 44" stroke="${P.gold}" stroke-width="6" fill="none" stroke-linecap="round"/>`;
  if (a === 'bamboo') return fur(u, L, 'k') + fur(u, R, 'k') + '|||' + `<g transform="translate(30,-30) rotate(24) scale(.8)"><rect x="-9" y="-70" width="18" height="170" rx="8" fill="${P.green}"/><rect x="-9" y="-12" width="18" height="6" fill="${P.greenD}"/><rect x="-9" y="48" width="18" height="6" fill="${P.greenD}"/>
      <path d="M0 -60 q-40 -16 -60 -6 q26 14 60 6 Z M6 -40 q40 -26 62 -16 q-26 20 -62 16 Z" fill="${P.green}"/></g>` + handPad(u, -24, 60, 25) + handPad(u, 30, 24, 25);
  if (a === 'hug') return fur(u, 'M-140 -8 C-162 74 -80 124 0 114 C80 124 162 74 140 -8 C110 -34 -110 -34 -140 -8 Z', 'k') + `<path d="M-110 60 Q0 96 110 60" stroke="${P.blackS}" stroke-width="3" fill="none" opacity=".6"/>` + handPad(u, -46, 96, 22) + handPad(u, 46, 96, 22);
  if (a === 'shy') return fur(u, L, 'k') + fur(u, R, 'k') + handPad(u, -20, 96, 24) + handPad(u, 20, 96, 24);
  return blob(u, -126, 70, 34, 76, 14) + blob(u, 126, 70, 34, 76, -14);
}
function extra(e, u) {
  if (e === 'heart') return `<path d="M150 -230 c-12 -18 -40 -6 -30 16 l30 28 l30 -28 c10 -22 -18 -34 -30 -16 Z" fill="${P.heart}"/>`;
  if (e === 'hearts') return `<path d="M120 -240 c-10 -15 -34 -5 -25 13 l25 23 l25 -23 c9 -18 -15 -28 -25 -13 Z" fill="${P.heart}"/><path d="M160 -270 c-6 -9 -20 -3 -15 8 l15 14 l15 -14 c5 -11 -9 -17 -15 -8 Z" fill="${P.heart}"/>`;
  if (e === 'q') return `<text x="160" y="-200" font-family="Fredoka" font-weight="600" font-size="88" fill="${P.ink}">?</text>`;
  if (e === 'bang') return `<text x="160" y="-200" font-family="Fredoka" font-weight="600" font-size="88" fill="#F28A3C">!</text>`;
  if (e === 'zzz') return `<text x="120" y="-170" font-family="Fredoka" font-weight="600" font-size="46" fill="#6A8FB8">z</text><text x="150" y="-210" font-family="Fredoka" font-weight="600" font-size="60" fill="#6A8FB8">z</text><text x="190" y="-258" font-family="Fredoka" font-weight="600" font-size="76" fill="#6A8FB8">z</text>`;
  if (e === 'spark') return `<path d="M-150 -250 l-14 -22 M-120 -270 l-4 -26 M150 -250 l14 -22 M120 -270 l4 -26 M180 -220 l24 -10" stroke="${P.gold}" stroke-width="7" stroke-linecap="round"/>`;
  if (e === 'sweat') return `<path d="M128 -190 q12 18 0 28 q-12 -10 0 -28 Z" fill="#A9D8F2"/>`;
  return '';
}
// ---------------- whole figures ----------------
function sitFront(u, o) {
  const q = o.view === 'q34' ? 1 : 0, hy = -112, jump = o.legs === 'jump';
  let s = `<ellipse cx="0" cy="266" rx="${jump ? 120 : 186}" ry="${jump ? 16 : 24}" fill="rgba(110,70,30,.2)" filter="url(#sf${u})"/>`;
  let fig = '';
  if (jump) fig += blob(u, -62, 236, 40, 58, 20) + blob(u, 72, 226, 40, 54, -34) + `<ellipse cx="-70" cy="276" rx="26" ry="15" fill="url(#pd${u})"/><ellipse cx="88" cy="262" rx="24" ry="14" fill="url(#pd${u})" transform="rotate(-30 88 262)"/>`;
  fig += fur(u, BODY) + fur(u, COLLAR, 'k') + `<ellipse cx="-22" cy="168" rx="90" ry="60" fill="rgba(255,255,255,.4)" filter="url(#sf${u})"/><ellipse cx="0" cy="226" rx="110" ry="30" fill="rgba(166,124,82,.14)" filter="url(#sf${u})"/>`;
  if (!jump) fig += paw(u, -118 + q * 10, 222, -18, -1) + paw(u, 118 + q * 14, 222, 18, 1);
  const [ab, af = ''] = arms(u, o.arms || 'pray').split('|||'); const qs = (x) => (q ? `<g transform="translate(18,0)">${x}</g>` : x);
  fig += qs(ab);
  fig += `<g transform="rotate(${o.tilt || 0} 0 -20)">${headFront(u, o.face || 'happy', q * 8, hy, q)}${qs(af)}${(o.extras || []).map((e) => extra(e, u)).join('')}</g>`;
  return s + `<g transform="translate(0,${jump ? -58 : 0})">${fig}</g>`;
}
function sitSide(u, o) {
  let s = `<ellipse cx="0" cy="266" rx="170" ry="22" fill="rgba(110,70,30,.2)" filter="url(#sf${u})"/>`;
  s += fur(u, 'M-120 110 C-128 10 -90 -24 0 -28 C90 -24 128 10 124 110 C120 200 80 252 0 254 C-80 252 -118 200 -120 110 Z');
  s += fur(u, 'M-124 30 C-100 -26 100 -26 124 30 C126 60 100 74 70 60 C20 46 -40 50 -80 62 C-110 70 -128 58 -124 30 Z', 'k');
  s += `<g transform="translate(70,226) rotate(6)">${blob(u, 0, 0, 84, 42)}<ellipse cx="64" cy="2" rx="15" ry="30" fill="url(#pd${u})"/></g>`;
  s += fur(u, 'M20 -10 C70 10 96 60 84 92 C74 110 50 104 52 80 C54 56 20 30 0 20 Z', 'k') + handPad(u, 84, 74, 24);
  s += blob(u, -46, -212, 35, 34) + fur(u, ell(0, -112, 136, 126)) + fur(u, ell(122, -78, 42, 32));
  s += `<ellipse cx="-30" cy="-160" rx="60" ry="36" fill="rgba(255,255,255,.5)" filter="url(#sf${u})"/>`;
  s += fur(u, ell(78, -100, 38, 30, -28), 'k') + `<path d="M64 -96 Q80 -110 96 -98" fill="none" stroke="#FBF7F1" stroke-width="5.5" stroke-linecap="round"/>`;
  s += `<ellipse cx="96" cy="-58" rx="22" ry="13" fill="url(#bl${u})"/><path d="M152 -86 q11 0 11 9 q-4 9 -13 5 Z" fill="#1E1A18"/><path d="M134 -56 q9 7 19 -2" stroke="#3A2A20" stroke-width="3.4" fill="none" stroke-linecap="round"/>`;
  return s;
}
function sitBack(u) {
  let s = `<ellipse cx="0" cy="266" rx="186" ry="24" fill="rgba(110,70,30,.2)" filter="url(#sf${u})"/>`;
  s += blob(u, -122, 238, 60, 30) + blob(u, 122, 238, 60, 30);
  s += fur(u, BODY) + fur(u, 'M-118 22 C-84 -34 84 -34 118 22 C130 70 120 120 100 128 C60 96 -60 96 -100 128 C-120 120 -130 70 -118 22 Z', 'k');
  s += blob(u, 0, 226, 24, 22);
  s += blob(u, -112, -212, 35, 34) + blob(u, 112, -212, 35, 34) + fur(u, ell(0, -112, 152, 128)) + `<ellipse cx="-46" cy="-170" rx="72" ry="40" fill="rgba(255,255,255,.5)" filter="url(#sf${u})"/>`;
  return s;
}
function lie(u, o) {   // relaxing / sleeping: lying on the tummy, chin on the paws
  const sleep = o.face === 'sleep';
  let s = `<ellipse cx="20" cy="266" rx="230" ry="22" fill="rgba(110,70,30,.2)" filter="url(#sf${u})"/>`;
  s += blob(u, 190, 226, 64, 46, -10);                                              // back leg
  s += fur(u, ell(50, 184, 200, 88));                                               // body
  s += fur(u, 'M-80 140 C-40 120 30 130 60 150 C70 190 50 250 10 262 C-40 268 -90 250 -100 210 Z', 'k');   // shoulders and front legs
  s += `<ellipse cx="200" cy="250" rx="30" ry="14" fill="url(#pd${u})"/>`;
  s += blob(u, -60, 248, 74, 26) + blob(u, 40, 250, 64, 24);                        // paws under the chin
  const hx = -112, hy = sleep ? 168 : 150;
  s += `<g transform="rotate(${sleep ? -10 : -6} ${hx} ${hy}) translate(${hx},${hy}) scale(.78) translate(${-hx},${-hy})">${headFront(u, o.face, hx, hy)}</g>`;
  return s + (o.extras || []).map((e) => `<g transform="translate(${e === 'zzz' ? 20 : -60},${sleep ? 260 : 220})">${extra(e, u)}</g>`).join('');
}
function panda(o = {}) {
  const u = ++UID; const v = o.view || 'front';
  const body = o.legs === 'lie' ? lie(u, o) : v === 'side' ? sitSide(u, o) : v === 'back' ? sitBack(u) : sitFront(u, o);
  return defs(u) + body;
}
function pandaSVG(o = {}, w = 520, h = 600, vb = '-260 -300 520 600') { return `<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="${vb}">${panda(o)}</svg>`; }
// the library: every named figure on the sheet
const LIB = {
  front: { arms: 'pray', face: 'calm' }, side: { view: 'side' }, back: { view: 'back' }, q34: { view: 'q34', arms: 'hug', face: 'happy' },
  happy: { arms: 'cheeks', face: 'happy', extras: ['spark'] }, excited: { arms: 'up', face: 'excited' }, wink: { arms: 'shy', face: 'wink', extras: ['heart'], tilt: -6 },
  thinking: { arms: 'chin', face: 'thinking', extras: ['q'], tilt: 6 }, surprised: { arms: 'cheeks', face: 'surprised', extras: ['bang'] }, sad: { arms: 'hug', face: 'sad', tilt: -4 },
  meditating: { arms: 'pray', face: 'calm' }, jump: { arms: 'up', face: 'excited', legs: 'jump', extras: ['spark'] }, shy: { arms: 'shy', face: 'shy', extras: ['hearts'], tilt: -8 },
  relaxing: { legs: 'lie', face: 'happy', extras: ['heart'] }, eating: { arms: 'bamboo', face: 'eat' }, waving: { arms: 'wave', face: 'excited' }, sleeping: { legs: 'lie', face: 'sleep', extras: ['zzz'] },
};
if (typeof module !== 'undefined') module.exports = { panda, pandaSVG, P, LIB };
