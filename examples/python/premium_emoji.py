"""Telegram premium (custom) emoji uchun kichik yordamchi modul.

Tashqi kutubxonasiz ishlaydi. Har qanday bot kutubxonasi bilan birga ishlatish mumkin:
aiogram, python-telegram-bot, pyTelegramBotAPI yoki oddiy HTTP so'rovlar.

    from premium_emoji import EmojiCatalog, tg_emoji

    catalog = EmojiCatalog.load()                 # data/all.json
    like = catalog.first("👍", pack="RestrictedEmoji")
    text = f"Rahmat {tg_emoji(like.id, like.emoji)}"   # parse_mode="HTML"
"""

from __future__ import annotations

import html
import json
from dataclasses import dataclass
from pathlib import Path

DEFAULT_DATA = Path(__file__).resolve().parents[2] / "data" / "all.json"


@dataclass(frozen=True)
class PremiumEmoji:
    id: str          # custom_emoji_id (doim satr sifatida saqlang: 19 xonali son)
    emoji: str       # oddiy emoji — premium ko'rinmasa shu chiqadi
    pack: str        # sticker set nomi (t.me/addemoji/<pack>)
    n: int           # pack ichidagi tartib raqami


class EmojiCatalog:
    def __init__(self, items: list[PremiumEmoji]):
        self.items = items
        self._by_id = {e.id: e for e in items}

    @classmethod
    def load(cls, path: str | Path = DEFAULT_DATA) -> "EmojiCatalog":
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        items = [
            PremiumEmoji(id=e["id"], emoji=e["emoji"], pack=p["set_name"], n=e["n"])
            for p in data["packs"]
            for e in p["emojis"]
        ]
        return cls(items)

    def get(self, emoji_id: str | int) -> PremiumEmoji | None:
        return self._by_id.get(str(emoji_id))

    def find(self, emoji: str, pack: str | None = None) -> list[PremiumEmoji]:
        """Oddiy emoji bo'yicha qidiradi (⭐ va ⭐️ bir xil hisoblanadi)."""
        key = _strip_vs(emoji)
        return [
            e for e in self.items
            if _strip_vs(e.emoji) == key and (pack is None or e.pack == pack)
        ]

    def first(self, emoji: str, pack: str | None = None) -> PremiumEmoji:
        found = self.find(emoji, pack)
        if not found:
            raise KeyError(f"{emoji!r} topilmadi (pack={pack})")
        return found[0]

    def by_pack(self, pack: str) -> list[PremiumEmoji]:
        return [e for e in self.items if e.pack == pack]


def _strip_vs(s: str) -> str:
    """U+FE0F (variation selector) ni olib tashlaydi: '⭐️' == '⭐'."""
    return s.replace("️", "")


# --- Matn formatlari -------------------------------------------------------

def tg_emoji(emoji_id: str | int, fallback: str) -> str:
    """parse_mode='HTML' uchun: <tg-emoji emoji-id="...">👍</tg-emoji>.

    Ichidagi `fallback` bitta oddiy emoji bo'lishi shart. Premium ko'rsatilmasa
    (masalan, bot egasida Premium yo'q bo'lsa) foydalanuvchi aynan shuni ko'radi.
    """
    return f'<tg-emoji emoji-id="{int(emoji_id)}">{html.escape(fallback)}</tg-emoji>'


def md_emoji(emoji_id: str | int, fallback: str) -> str:
    """parse_mode='MarkdownV2' uchun: ![👍](tg://emoji?id=...)."""
    return f"![{fallback}](tg://emoji?id={int(emoji_id)})"


def utf16_len(s: str) -> int:
    """Telegram entity offset/length UTF-16 kod birliklarida hisoblanadi."""
    return len(s.encode("utf-16-le")) // 2


class EntityTextBuilder:
    """parse_mode'siz, entities bilan xabar yig'ish.

    b = EntityTextBuilder()
    b.text("Salom ").emoji("5469770542288478598", "👍")
    text, entities = b.build()
    bot.send_message(chat_id, text, entities=entities)   # dict ro'yxat
    """

    def __init__(self) -> None:
        self._parts: list[str] = []
        self._entities: list[dict] = []
        self._offset = 0

    def text(self, s: str) -> "EntityTextBuilder":
        self._parts.append(s)
        self._offset += utf16_len(s)
        return self

    def emoji(self, emoji_id: str | int, fallback: str) -> "EntityTextBuilder":
        length = utf16_len(fallback)
        self._entities.append({
            "type": "custom_emoji",
            "offset": self._offset,
            "length": length,
            "custom_emoji_id": str(emoji_id),
        })
        self._parts.append(fallback)
        self._offset += length
        return self

    def build(self) -> tuple[str, list[dict]]:
        return "".join(self._parts), list(self._entities)


def extract_custom_emoji_ids(text: str | None, entities: list[dict] | None) -> list[tuple[str, str]]:
    """Kelgan xabardagi premium emoji'larni (id, emoji) ro'yxatiga ajratadi.

    `entities` — Bot API'dan kelgan dict'lar (aiogram/PTB obyektlarida .model_dump()/.to_dict()).
    """
    if not text or not entities:
        return []
    raw = text.encode("utf-16-le")
    out = []
    for ent in entities:
        if ent.get("type") != "custom_emoji":
            continue
        start, length = ent["offset"] * 2, ent["length"] * 2
        out.append((ent["custom_emoji_id"], raw[start:start + length].decode("utf-16-le")))
    return out


# --- Tugmalar --------------------------------------------------------------

def inline_button(text: str, callback_data: str, icon_id: str | int | None = None,
                  style: str | None = None) -> dict:
    """InlineKeyboardButton JSON. style: 'primary' | 'success' | 'danger' | None."""
    btn: dict = {"text": text, "callback_data": callback_data}
    if icon_id is not None:
        btn["icon_custom_emoji_id"] = str(icon_id)
    if style is not None:
        if style not in ("primary", "success", "danger"):
            raise ValueError("style faqat 'primary', 'success' yoki 'danger' bo'ladi")
        btn["style"] = style
    return btn


if __name__ == "__main__":
    cat = EmojiCatalog.load()
    print(len(cat.items), "ta emoji yuklandi")
    fire = cat.first("🔥", pack="RestrictedEmoji")
    print(tg_emoji(fire.id, fire.emoji))
    print(md_emoji(fire.id, fire.emoji))
    print(EntityTextBuilder().text("Salom 🇺🇿 ").emoji(fire.id, fire.emoji).build())
