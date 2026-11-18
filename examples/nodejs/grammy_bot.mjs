// grammY bilan premium emoji: matn, tugma ikonkasi va kelgan emoji ID'sini aniqlash.
//   npm i grammy
//   BOT_TOKEN=123:ABC node grammy_bot.mjs

import { Bot } from 'grammy';
import { extractCustomEmoji, loadCatalog, tgEmoji } from './premiumEmoji.mjs';

const cat = await loadCatalog();
const wave = cat.first('👋', 'RestrictedEmoji');
const gear = cat.first('⚙️', 'tgiosicons');
const user = cat.first('👤', 'tgiosicons');

const bot = new Bot(process.env.BOT_TOKEN);

bot.command('start', (ctx) =>
  ctx.reply(`${tgEmoji(wave.id, wave.emoji)} <b>Salom!</b> Menga premium emoji yuboring.`, {
    parse_mode: 'HTML',
    // Xom JSON — grammY reply_markup'ni o'zgartirmasdan Telegram'ga yuboradi
    reply_markup: {
      inline_keyboard: [[
        { text: 'Profil', callback_data: 'profile', icon_custom_emoji_id: user.id, style: 'primary' },
        { text: 'Sozlamalar', callback_data: 'settings', icon_custom_emoji_id: gear.id },
      ]],
    },
  }),
);

bot.on('message:entities:custom_emoji', (ctx) => {
  const found = extractCustomEmoji(ctx.message.text, ctx.message.entities);
  const lines = found.map(({ id, emoji }) => {
    const known = cat.get(id);
    return `${tgEmoji(id, emoji)} <code>${id}</code>${known ? ` · <code>${known.pack}</code> #${known.n}` : ''}`;
  });
  return ctx.reply(lines.join('\n'), { parse_mode: 'HTML' });
});

bot.on('callback_query:data', (ctx) => ctx.answerCallbackQuery(`Bosildi: ${ctx.callbackQuery.data}`));

bot.start();
