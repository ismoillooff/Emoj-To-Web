"""aiogram 3 bilan premium emoji: matnda, tugmada va kelgan emoji ID'sini aniqlash.

    pip install "aiogram>=3.31"
    BOT_TOKEN=123:ABC python aiogram_bot.py

/start  — premium emoji'li xabar va rangli, ikonkali tugmalar
istalgan premium emoji yuboring — bot uning ID'si va tayyor HTML kodini qaytaradi
"""

from __future__ import annotations

import asyncio
import html
import os

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

from premium_emoji import EmojiCatalog, extract_custom_emoji_ids, tg_emoji

cat = EmojiCatalog.load()
E = {
    "wave": cat.first("👋", pack="RestrictedEmoji"),
    "fire": cat.first("🔥", pack="RestrictedEmoji"),
    "ok": cat.first("✅", pack="tgiosicons"),
    "no": cat.first("❌", pack="tgiosicons"),
    "gear": cat.first("⚙️", pack="tgiosicons"),
    "user": cat.first("👤", pack="tgiosicons"),
}

dp = Dispatcher()


def e(key: str) -> str:
    item = E[key]
    return tg_emoji(item.id, item.emoji)


def main_menu() -> InlineKeyboardMarkup:
    # icon_custom_emoji_id va style — Bot API 9.4+ (aiogram 3.31+)
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Tasdiqlash", callback_data="ok",
                                 icon_custom_emoji_id=E["ok"].id, style="success"),
            InlineKeyboardButton(text="Bekor qilish", callback_data="no",
                                 icon_custom_emoji_id=E["no"].id, style="danger"),
        ],
        [
            InlineKeyboardButton(text="Profil", callback_data="profile",
                                 icon_custom_emoji_id=E["user"].id, style="primary"),
            InlineKeyboardButton(text="Sozlamalar", callback_data="settings",
                                 icon_custom_emoji_id=E["gear"].id),
        ],
    ])


@dp.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer(
        f"{e('wave')} <b>Assalomu alaykum, {html.escape(message.from_user.full_name)}!</b>\n\n"
        f"Bu xabardagi emoji'lar premium {e('fire')}\n"
        f"Menga istalgan premium emoji yuboring, ID'sini aytaman.",
        reply_markup=main_menu(),
    )


@dp.message(F.entities)
async def detect(message: Message) -> None:
    entities = [ent.model_dump() for ent in message.entities]
    found = extract_custom_emoji_ids(message.text, entities)
    if not found:
        return
    lines = []
    for emoji_id, emoji in found:
        known = cat.get(emoji_id)
        where = f" · <code>{known.pack}</code> #{known.n}" if known else ""
        lines.append(
            f"{tg_emoji(emoji_id, emoji)} <code>{emoji_id}</code>{where}\n"
            f"<code>{html.escape(tg_emoji(emoji_id, emoji))}</code>"
        )
    await message.answer("\n\n".join(lines))


@dp.callback_query()
async def on_button(call: CallbackQuery) -> None:
    await call.answer(f"Bosildi: {call.data}")


async def main() -> None:
    bot = Bot(os.environ["BOT_TOKEN"], default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
