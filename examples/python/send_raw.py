"""Bot API'ga to'g'ridan-to'g'ri HTTP so'rov (faqat standart kutubxona).

    BOT_TOKEN=123:ABC CHAT_ID=123456789 python send_raw.py

Uch xil usul ko'rsatilgan:
  1) parse_mode="HTML"        — <tg-emoji>
  2) parse_mode="MarkdownV2"  — ![👍](tg://emoji?id=...)
  3) entities                 — custom_emoji entity (offset/length UTF-16 da)
va tugmalarda icon_custom_emoji_id + style.
"""

from __future__ import annotations

import json
import os
import urllib.request

from premium_emoji import EmojiCatalog, EntityTextBuilder, inline_button, md_emoji, tg_emoji

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]
API = f"https://api.telegram.org/bot{TOKEN}"


def call(method: str, **params) -> dict:
    req = urllib.request.Request(
        f"{API}/{method}",
        data=json.dumps(params).encode(),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:   # Telegram xatoni JSON'da qaytaradi
        return json.load(e)


def main() -> None:
    cat = EmojiCatalog.load()
    like = cat.first("👍", pack="RestrictedEmoji")
    fire = cat.first("🔥", pack="RestrictedEmoji")
    uz = cat.first("🇺🇿")
    ok = cat.first("✅", pack="tgiosicons")
    no = cat.first("❌", pack="tgiosicons")
    gear = cat.first("⚙️", pack="tgiosicons")

    # 1) HTML
    r = call(
        "sendMessage",
        chat_id=CHAT_ID,
        parse_mode="HTML",
        text=f"<b>Salom!</b> {tg_emoji(uz.id, uz.emoji)} Premium emoji ishlayapti {tg_emoji(fire.id, fire.emoji)}",
        reply_markup={
            "inline_keyboard": [
                [
                    inline_button("Tasdiqlash", "ok", icon_id=ok.id, style="success"),
                    inline_button("Bekor qilish", "no", icon_id=no.id, style="danger"),
                ],
                [inline_button("Sozlamalar", "settings", icon_id=gear.id, style="primary")],
            ]
        },
    )
    print("HTML:", r.get("ok"), r.get("description", ""))

    # 2) MarkdownV2 (! . - kabi belgilar \ bilan ekranlanadi)
    r = call(
        "sendMessage",
        chat_id=CHAT_ID,
        parse_mode="MarkdownV2",
        text=f"*MarkdownV2* {md_emoji(like.id, like.emoji)} ham ishlaydi\\!",
    )
    print("MarkdownV2:", r.get("ok"), r.get("description", ""))

    # 3) entities (parse_mode ishlatilmaydi)
    text, entities = (
        EntityTextBuilder().text("Entities orqali ").emoji(like.id, like.emoji).text(" tayyor").build()
    )
    r = call("sendMessage", chat_id=CHAT_ID, text=text, entities=entities)
    print("entities:", r.get("ok"), r.get("description", ""))

    # Natijani tekshirish: Telegram premium emoji'ni rad etsa, javobdagi
    # entities ichida custom_emoji bo'lmaydi (oddiy emoji bo'lib qoladi).
    sent = r.get("result", {})
    kept = any(e.get("type") == "custom_emoji" for e in sent.get("entities", []))
    print("Premium emoji saqlandimi:", kept)


if __name__ == "__main__":
    main()
