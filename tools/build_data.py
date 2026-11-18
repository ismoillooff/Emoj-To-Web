#!/usr/bin/env python3
"""data/raw/*.txt jadvallarini JSON va CSV formatlariga o'giradi.

Ishlatish:
    python tools/build_data.py

Natija:
    data/json/<pack>.json   — bitta pack
    data/csv/<pack>.csv     — bitta pack
    data/all.json           — barcha pack'lar bitta faylda
    data/all.csv            — barcha emoji'lar bitta jadvalda
    data/packs.json         — pack'lar ro'yxati (nom, soni, havola)

Tashqi kutubxona kerak emas (faqat Python 3.9+ standart kutubxonasi).
"""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
ROW_RE = re.compile(r"^\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(.+?)\s*$")


def parse_table(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()
    title = lines[0].strip()
    declared = int(re.match(r"\s*(\d+)", lines[1]).group(1))
    emojis = []
    for line in lines[2:]:
        m = ROW_RE.match(line)
        if not m:
            continue
        number, emoji_id, emoji = m.groups()
        emojis.append({"n": int(number), "id": emoji_id, "emoji": emoji})

    if len(emojis) != declared:
        sys.exit(f"{path.name}: sarlavhada {declared} ta, jadvalda {len(emojis)} ta qator")
    if [e["n"] for e in emojis] != list(range(1, declared + 1)):
        sys.exit(f"{path.name}: tartib raqamlari uzilgan")

    set_name = path.stem
    suffix = f"({set_name})"
    if title.endswith(suffix):
        title = title[: -len(suffix)].strip()
    return {
        "set_name": set_name,
        "title": title,
        "count": len(emojis),
        "url": f"https://t.me/addemoji/{set_name}",
        "emojis": emojis,
    }


def write_markdown(packs: list[dict]) -> None:
    """docs/packs/<pack>.md — GitHub'da ko'rish uchun to'liq jadval."""
    out = ROOT / "docs" / "packs"
    out.mkdir(parents=True, exist_ok=True)
    for pack in packs:
        name = pack["set_name"]
        lines = [
            f"# {pack['title']} — `{name}`",
            "",
            f"**{pack['count']} ta custom emoji** · Pack'ni Telegram'ga qo'shish: <{pack['url']}>",
            "",
            f"Mashina o'qiydigan format: [`data/json/{name}.json`](../../data/json/{name}.json) · "
            f"[`data/csv/{name}.csv`](../../data/csv/{name}.csv)",
            "",
            "Bot xabarida: `<tg-emoji emoji-id=\"ID\">EMOJI</tg-emoji>` (HTML) yoki "
            "`![EMOJI](tg://emoji?id=ID)` (MarkdownV2). Tugmada: `icon_custom_emoji_id`.",
            "",
            "[⬅️ README](../../README.md)",
            "",
            "| № | Emoji | custom_emoji_id |",
            "|---:|:---:|---|",
        ]
        for e in pack["emojis"]:
            lines.append(f"| {e['n']} | {e['emoji']} | `{e['id']}` |")
        (out / f"{name}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    packs = [parse_table(p) for p in sorted(RAW.glob("*.txt"), key=lambda p: p.stem.lower())]

    seen: dict[str, str] = {}
    for pack in packs:
        for e in pack["emojis"]:
            if e["id"] in seen:
                sys.exit(f"Takroriy ID {e['id']}: {seen[e['id']]} va {pack['set_name']}")
            seen[e["id"]] = pack["set_name"]

    (ROOT / "data" / "json").mkdir(parents=True, exist_ok=True)
    (ROOT / "data" / "csv").mkdir(parents=True, exist_ok=True)

    for pack in packs:
        name = pack["set_name"]
        (ROOT / "data" / "json" / f"{name}.json").write_text(
            json.dumps(pack, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        with open(ROOT / "data" / "csv" / f"{name}.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f, lineterminator="\n")
            w.writerow(["n", "custom_emoji_id", "emoji"])
            for e in pack["emojis"]:
                w.writerow([e["n"], e["id"], e["emoji"]])

    (ROOT / "data" / "all.json").write_text(
        json.dumps({"total": len(seen), "packs": packs}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    with open(ROOT / "data" / "all.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["set_name", "n", "custom_emoji_id", "emoji"])
        for pack in packs:
            for e in pack["emojis"]:
                w.writerow([pack["set_name"], e["n"], e["id"], e["emoji"]])

    write_markdown(packs)

    summary = [{k: p[k] for k in ("set_name", "title", "count", "url")} for p in packs]
    (ROOT / "data" / "packs.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    for p in summary:
        print(f"{p['set_name']:<18} {p['count']:>4}  {p['title']}")
    print(f"{'Jami':<18} {len(seen):>4}")


if __name__ == "__main__":
    main()
