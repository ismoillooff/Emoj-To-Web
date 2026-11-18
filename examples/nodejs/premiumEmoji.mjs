// Telegram premium (custom) emoji uchun yordamchi modul (Node.js 18+, tashqi kutubxonasiz).
//
//   import { loadCatalog, tgEmoji } from './premiumEmoji.mjs';
//   const cat = await loadCatalog();
//   const fire = cat.first('🔥', 'RestrictedEmoji');
//   tgEmoji(fire.id, fire.emoji);   // <tg-emoji emoji-id="...">🔥</tg-emoji>

import { readFile } from 'node:fs/promises';

const DEFAULT_DATA = new URL('../../data/all.json', import.meta.url);
const stripVs = (s) => s.replaceAll('️', '');

export async function loadCatalog(path = DEFAULT_DATA) {
  const data = JSON.parse(await readFile(path, 'utf8'));
  const items = data.packs.flatMap((p) =>
    p.emojis.map((e) => ({ id: e.id, emoji: e.emoji, pack: p.set_name, n: e.n })),
  );
  const byId = new Map(items.map((e) => [e.id, e]));
  return {
    items,
    get: (id) => byId.get(String(id)),
    find: (emoji, pack) =>
      items.filter((e) => stripVs(e.emoji) === stripVs(emoji) && (!pack || e.pack === pack)),
    first(emoji, pack) {
      const found = this.find(emoji, pack);
      if (!found.length) throw new Error(`Topilmadi: ${emoji}`);
      return found[0];
    },
  };
}

const escapeHtml = (s) => s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]);

// ID'ni hech qachon Number'ga o'girmang: 19 xonali son JS'da aniqligini yo'qotadi.
export const tgEmoji = (id, fallback) => `<tg-emoji emoji-id="${id}">${escapeHtml(fallback)}</tg-emoji>`;
export const mdEmoji = (id, fallback) => `![${fallback}](tg://emoji?id=${id})`;

// JS string.length allaqachon UTF-16 kod birliklarini sanaydi — Telegram ham shunday sanaydi.
export function entityText(parts) {
  let text = '';
  const entities = [];
  for (const part of parts) {
    if (typeof part === 'string') {
      text += part;
    } else {
      entities.push({ type: 'custom_emoji', offset: text.length, length: part.emoji.length, custom_emoji_id: String(part.id) });
      text += part.emoji;
    }
  }
  return { text, entities };
}

export function extractCustomEmoji(text = '', entities = []) {
  return entities
    .filter((e) => e.type === 'custom_emoji')
    .map((e) => ({ id: e.custom_emoji_id, emoji: text.slice(e.offset, e.offset + e.length) }));
}

export function button(text, callback_data, iconId, style) {
  const b = { text, callback_data };
  if (iconId) b.icon_custom_emoji_id = String(iconId);
  if (style) b.style = style; // 'primary' | 'success' | 'danger'
  return b;
}
