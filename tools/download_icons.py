#!/usr/bin/env python3
"""Premium emoji fayllarini (ikonkalarni) Telegram Bot API orqali yuklab oladi.

    BOT_TOKEN=123:ABC python tools/download_icons.py                 # hamma pack
    BOT_TOKEN=123:ABC python tools/download_icons.py tgiosicons      # bitta pack
    BOT_TOKEN=123:ABC python tools/download_icons.py --thumb         # faqat kichik WEBP preview

Natija: icons/<pack>/<custom_emoji_id>.<ext> va icons/manifest.json

Fayl turlari (Telegram qaytarganidek):
  .webp — statik emoji          → <img>
  .tgs  — animatsiya (gzip Lottie) → lottie-web
  .webm — video emoji           → <video autoplay loop muted playsinline>

Istalgan bot token ishlaydi: getCustomEmojiStickers uchun Premium shart emas.
Telegram dizaynlari mualliflariga tegishli: fayllarni o'z loyihangizda ishlatishdan oldin
pack egasi shartlarini tekshiring. icons/ papkasi .gitignore'da.
"""

from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKEN = os.environ.get("BOT_TOKEN") or sys.exit("BOT_TOKEN muhit o'zgaruvchisini bering")
API = f"https://api.telegram.org/bot{TOKEN}"
FILE_API = f"https://api.telegram.org/file/bot{TOKEN}"
BATCH = 200  # getCustomEmojiStickers bir so'rovda ko'pi bilan 200 ta ID qabul qiladi


def api(method: str, **params) -> dict:
    req = urllib.request.Request(
        f"{API}/{method}", data=json.dumps(params).encode(), headers={"Content-Type": "application/json"}
    )
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = json.load(r)
        except urllib.error.HTTPError as e:
            data = json.load(e)
        if data.get("ok"):
            return data["result"]
        retry = data.get("parameters", {}).get("retry_after")
        if retry:  # 429 Too Many Requests
            time.sleep(retry + 1)
            continue
        raise RuntimeError(f"{method}: {data.get('description')}")
    raise RuntimeError(f"{method}: juda ko'p urinish")


def download(file_id: str, dest_stem: Path) -> str:
    info = api("getFile", file_id=file_id)
    path = info["file_path"]
    dest = dest_stem.with_suffix(Path(path).suffix or ".bin")
    if not dest.exists():
        with urllib.request.urlopen(f"{FILE_API}/{path}", timeout=120) as r:
            dest.write_bytes(r.read())
    return dest.relative_to(ROOT).as_posix()


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    thumb_only = "--thumb" in sys.argv
    data = json.loads((ROOT / "data" / "all.json").read_text(encoding="utf-8"))
    packs = [p for p in data["packs"] if not args or p["set_name"] in args]

    manifest_path = ROOT / "icons" / "manifest.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}

    for pack in packs:
        out = ROOT / "icons" / pack["set_name"]
        out.mkdir(parents=True, exist_ok=True)
        ids = [e["id"] for e in pack["emojis"]]
        print(f"{pack['set_name']}: {len(ids)} ta")
        for i in range(0, len(ids), BATCH):
            for st in api("getCustomEmojiStickers", custom_emoji_ids=ids[i:i + BATCH]):
                cid = st["custom_emoji_id"]
                kind = "video" if st.get("is_video") else "animated" if st.get("is_animated") else "static"
                entry = {"pack": pack["set_name"], "emoji": st.get("emoji"), "type": kind,
                         "needs_repainting": st.get("needs_repainting", False)}
                if thumb_only:
                    if st.get("thumbnail"):
                        entry["thumb"] = download(st["thumbnail"]["file_id"], out / f"{cid}.thumb")
                else:
                    entry["file"] = download(st["file_id"], out / cid)
                manifest[cid] = entry
                print(f"  {cid} {kind}", end="\r")
            manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=1))
        print()
    print(f"Tayyor: {manifest_path.relative_to(ROOT)} ({len(manifest)} ta yozuv)")


if __name__ == "__main__":
    main()
