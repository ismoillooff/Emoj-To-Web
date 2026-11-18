"""python-telegram-bot (PTB) bilan premium emoji.

    pip install "python-telegram-bot>=22.7"
    BOT_TOKEN=123:ABC python ptb_bot.py
"""

from __future__ import annotations

import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes

from premium_emoji import EmojiCatalog, tg_emoji

cat = EmojiCatalog.load()
STAR = cat.first("⭐️", pack="tgiosicons")
GIFT = cat.first("🎁", pack="tgiosicons")
HEART = cat.first("❤️", pack="RestrictedEmoji")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("Premium olish", callback_data="buy",
                              icon_custom_emoji_id=STAR.id, style="primary")],
        [InlineKeyboardButton("Sovg'a qilish", callback_data="gift",
                              icon_custom_emoji_id=GIFT.id, style="success")],
    ])
    await update.message.reply_text(
        f"PTB orqali premium emoji {tg_emoji(HEART.id, HEART.emoji)}",
        parse_mode=ParseMode.HTML,
        reply_markup=keyboard,
    )


def main() -> None:
    app = Application.builder().token(os.environ["BOT_TOKEN"]).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()


if __name__ == "__main__":
    main()
