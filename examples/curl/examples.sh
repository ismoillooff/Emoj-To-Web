#!/usr/bin/env bash
# cURL bilan premium emoji. Ishlatish:
#   BOT_TOKEN=123:ABC CHAT_ID=123456789 bash examples.sh
set -euo pipefail
: "${BOT_TOKEN:?BOT_TOKEN kerak}" "${CHAT_ID:?CHAT_ID kerak}"
API="https://api.telegram.org/bot${BOT_TOKEN}"

# 1) HTML: <tg-emoji> + rangli, ikonkali tugmalar
curl -s "$API/sendMessage" -H 'Content-Type: application/json' -d @- <<JSON
{
  "chat_id": "${CHAT_ID}",
  "parse_mode": "HTML",
  "text": "<b>cURL</b> <tg-emoji emoji-id=\"5449829434334912605\">🇺🇿</tg-emoji> premium emoji <tg-emoji emoji-id=\"5420315771991497307\">🔥</tg-emoji>",
  "reply_markup": {
    "inline_keyboard": [[
      {"text": "Ha",   "callback_data": "yes", "icon_custom_emoji_id": "5774022692642492953", "style": "success"},
      {"text": "Yo'q", "callback_data": "no",  "icon_custom_emoji_id": "5774077015388852135", "style": "danger"}
    ]]
  }
}
JSON
echo

# 2) MarkdownV2
curl -s "$API/sendMessage" -H 'Content-Type: application/json' -d @- <<JSON
{
  "chat_id": "${CHAT_ID}",
  "parse_mode": "MarkdownV2",
  "text": "*MarkdownV2* ![👍](tg://emoji?id=5469770542288478598) ishlaydi\\\\!"
}
JSON
echo

# 3) entities ("Entities: " = 10 ta UTF-16 birlik, 👍 = 2 ta)
curl -s "$API/sendMessage" -H 'Content-Type: application/json' -d @- <<JSON
{
  "chat_id": "${CHAT_ID}",
  "text": "Entities: 👍",
  "entities": [{"type": "custom_emoji", "offset": 10, "length": 2, "custom_emoji_id": "5469770542288478598"}]
}
JSON
echo

# 4) Reply keyboard (pastki klaviatura) tugmasida ikonka
curl -s "$API/sendMessage" -H 'Content-Type: application/json' -d @- <<JSON
{
  "chat_id": "${CHAT_ID}",
  "text": "Pastki menyu",
  "reply_markup": {
    "resize_keyboard": true,
    "keyboard": [[
      {"text": "Profil",     "icon_custom_emoji_id": "6032994772321309200"},
      {"text": "Sozlamalar", "icon_custom_emoji_id": "5904258298764334001", "style": "primary"}
    ]]
  }
}
JSON
echo

# 5) Emoji haqida ma'lumot (fayl, set nomi, animatsiya turi)
curl -s "$API/getCustomEmojiStickers" -H 'Content-Type: application/json' \
  -d '{"custom_emoji_ids": ["5420315771991497307", "5774022692642492953"]}'
echo
