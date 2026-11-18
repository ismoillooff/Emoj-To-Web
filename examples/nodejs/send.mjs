// Bot API'ga fetch bilan so'rov (Node.js 18+).
//   BOT_TOKEN=123:ABC CHAT_ID=123456789 node send.mjs

import { button, entityText, loadCatalog, mdEmoji, tgEmoji } from './premiumEmoji.mjs';

const { BOT_TOKEN, CHAT_ID } = process.env;
if (!BOT_TOKEN || !CHAT_ID) throw new Error('BOT_TOKEN va CHAT_ID kerak');

async function call(method, params) {
  const res = await fetch(`https://api.telegram.org/bot${BOT_TOKEN}/${method}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(params),
  });
  return res.json();
}

const cat = await loadCatalog();
const fire = cat.first('🔥', 'RestrictedEmoji');
const like = cat.first('👍', 'RestrictedEmoji');
const ok = cat.first('✅', 'tgiosicons');
const no = cat.first('❌', 'tgiosicons');

// 1) HTML + tugmalar
let r = await call('sendMessage', {
  chat_id: CHAT_ID,
  parse_mode: 'HTML',
  text: `<b>Node.js</b> premium emoji ${tgEmoji(fire.id, fire.emoji)}`,
  reply_markup: {
    inline_keyboard: [[button('Ha', 'yes', ok.id, 'success'), button("Yo'q", 'no', no.id, 'danger')]],
  },
});
console.log('HTML:', r.ok, r.description ?? '');

// 2) MarkdownV2
r = await call('sendMessage', {
  chat_id: CHAT_ID,
  parse_mode: 'MarkdownV2',
  text: `*MarkdownV2* ${mdEmoji(like.id, like.emoji)} ishlaydi\\!`,
});
console.log('MarkdownV2:', r.ok, r.description ?? '');

// 3) entities
r = await call('sendMessage', { chat_id: CHAT_ID, ...entityText(['Entities: ', like, ' tayyor']) });
console.log('entities:', r.ok, r.description ?? '');
