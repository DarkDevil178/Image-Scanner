// The explainer's demo wardrobe: 14 real photographs cut out by Wardrobe's own Smart AI (fictional owner, no real data).
const fs = require('fs');
const DIR = __dirname + '/items/';
const now = Date.parse('2026-11-13T09:00:00');
const day = 864e5;
const I = (id, cat, type, colors, name, price, occasions, seasons, extra = {}) => ({ id, cat, type, colors, name, price, occasions, seasons, ...extra });
const ITEMS = [
  I('tee', 'tops', 'T-shirt', ['White'], 'White tee', 799, ['Casual', 'Travel'], ['All-season'], { fav: true, brand: 'Everyday' }),
  I('longsleeve', 'tops', 'T-shirt', ['Black', 'Grey'], 'Layered long-sleeve', 1299, ['Casual', 'Office'], ['Winter', 'Monsoon'], { brand: 'Northline' }),
  I('trousers', 'bottoms', 'Trousers', ['Brown'], 'Rust trousers', 1999, ['Office', 'Casual'], ['All-season'], { fav: true, brand: 'Atelier' }),
  I('skirt', 'bottoms', 'Skirt', ['Black'], 'Pleated skirt', 1799, ['Party', 'Office'], ['All-season'], { brand: 'Atelier' }),
  I('sneakers2', 'shoes', 'Sneakers', ['Grey', 'White'], 'Grey sneakers', 4999, ['Casual', 'Travel', 'Sports'], ['All-season'], { fav: true }),
  I('loafer', 'shoes', 'Formal', ['Brown'], 'Tan loafers', 3999, ['Office', 'Party'], ['All-season'], { brand: 'Atelier' }),
  I('formal', 'shoes', 'Formal', ['Black'], 'Black dress shoes', 2999, ['Office', 'Party'], ['All-season']),
  I('boots', 'shoes', 'Boots', ['Maroon'], 'Oxblood boots', 5999, ['Casual', 'Travel'], ['Winter', 'Monsoon'], { fav: true }),
  I('denim', 'jackets', 'Jacket', ['Blue'], 'Light denim jacket', 2999, ['Casual', 'Travel'], ['All-season'], { fav: true, brand: 'Everyday' }),
  I('workjacket', 'jackets', 'Jacket', ['Navy'], 'Indigo work jacket', 4499, ['Casual'], ['Winter'], { brand: 'Northline' }),
  I('hoodie', 'jackets', 'Hoodie', ['Black'], 'Graphic hoodie', 2499, ['Casual'], ['Winter'], { laundry: true }),
  I('briefcase', 'accessories', 'Bag', ['Black'], 'Black briefcase', 3499, ['Office'], ['All-season']),
  I('bag', 'accessories', 'Bag', ['Navy'], 'Weekend bag', 2499, ['Travel'], ['All-season']),
  I('scarf', 'accessories', 'Other', ['Sky'], 'Check scarf', 899, ['Casual', 'Travel'], ['Winter']),
];
const items = ITEMS.map((it, i) => ({
  brand: '', size: '', notes: '', fav: false, laundry: false, sizeCm: null, ...it,
  created: now - (20 - i) * day, updated: now - (20 - i) * day,
  img: 'data:image/png;base64,' + fs.readFileSync(DIR + it.id + '.png').toString('base64'),
}));
const O = (id, name, top, bottom, shoes, occ, fav = false) => ({ id, name, bg: 'Champagne', top, bottom, shoes, occasions: occ, fav, created: now - 9 * day, updated: now - 9 * day });
const outfits = [
  O('o-weekend', 'Weekend easy', 'tee', 'trousers', 'sneakers2', ['Casual'], true),
  O('o-office', 'Office day', 'longsleeve', 'trousers', 'loafer', ['Office']),
  O('o-night', 'Night out', 'tee', 'skirt', 'boots', ['Party'], true),
  O('o-cold', 'Cold morning', 'longsleeve', 'trousers', 'boots', ['Casual']),
  O('o-smart', 'Smart casual', 'tee', 'trousers', 'loafer', ['Office']),
];
const dk = (off) => { const d = new Date(now + off * day); return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`; };
const hist = ['o-office', 'o-weekend', 'o-cold', 'o-office', 'o-night', 'o-weekend', 'o-smart', 'o-office', 'o-cold', 'o-weekend', 'o-office', 'o-weekend', 'o-night', 'o-smart', 'o-office', 'o-cold', 'o-weekend', 'o-office'];
const plans = [];
hist.forEach((o, i) => { if (i % 6 !== 5) plans.push({ id: dk(-hist.length + i), outfitId: o, worn: true }); });
[['o-weekend', 0], ['o-office', 1], ['o-night', 2], ['o-cold', 4], ['o-smart', 5]].forEach(([o, k]) => plans.push({ id: dk(k), outfitId: o, worn: false }));
const sets = [
  { id: 's-trip', name: 'Lisbon weekend', kind: 'trip', items: ['tee', 'longsleeve', 'trousers', 'sneakers2', 'denim', 'bag', 'scarf'], packed: ['tee', 'trousers', 'bag'], from: dk(7), to: dk(9) },
  { id: 's-cap', name: 'Workweek capsule', kind: 'capsule', items: ['tee', 'longsleeve', 'trousers', 'skirt', 'loafer', 'formal', 'briefcase'], packed: [], from: '', to: '' },
];
const wish = [
  { id: 'w1', name: 'White oxford shirt', price: 2499, link: '', note: 'Slim fit' },
  { id: 'w2', name: 'Dark wash jeans', price: 3499, link: '', note: 'Straight leg' },
];
fs.writeFileSync(__dirname + '/seed-backup.json', JSON.stringify({ app: 'my-cupboard', version: 3, exported: new Date(now).toISOString(), items, outfits, plans, extras: { sets, wish, dislikes: [] } }));
console.log(items.length, 'items', outfits.length, 'outfits', plans.length, 'plans', (fs.statSync(__dirname + '/seed-backup.json').size / 1e6).toFixed(1), 'MB');
