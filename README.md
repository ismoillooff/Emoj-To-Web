<div align="center">

# ✨ Telegram Premium Emoji

### Telegram bot va saytlar uchun 1 645 ta premium (custom) emoji ID'si va tayyor kod namunalari

[![Bot API](https://img.shields.io/badge/Bot%20API-9.4%2B-2AABEE?logo=telegram&logoColor=white)](https://core.telegram.org/bots/api)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](examples/python)
[![PHP](https://img.shields.io/badge/PHP-8.1%2B-777BB4?logo=php&logoColor=white)](examples/php)
[![Java](https://img.shields.io/badge/Java-17%2B-ED8B00?logo=openjdk&logoColor=white)](examples/java)
[![Node.js](https://img.shields.io/badge/Node.js-18%2B-339933?logo=nodedotjs&logoColor=white)](examples/nodejs)
[![Go](https://img.shields.io/badge/Go-1.21%2B-00ADD8?logo=go&logoColor=white)](examples/go)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**4 ta pack · JSON / CSV / Markdown · HTML, MarkdownV2, entities · tugma ikonkalari · sayt uchun katalog**

</div>

---

## 📌 Loyiha haqida

Bu repoda to'rtta Telegram custom emoji pack'idagi **barcha emoji'larning `custom_emoji_id`** ro'yxati va ularni ishlatish bo'yicha to'liq qo'llanma bor:

- bot xabarida premium emoji yuborish (**HTML**, **MarkdownV2**, **entities**);
- inline va reply tugmalarga emoji **ikonka** qo'yish (`icon_custom_emoji_id`) va tugma **rangi** (`style`);
- foydalanuvchi yuborgan premium emoji'ning ID'sini aniqlash;
- emoji fayllarini (WEBP / TGS / WEBM) yuklab olib, **saytda** ko'rsatish.

Namunalar **Python** (aiogram, python-telegram-bot, oddiy HTTP), **PHP**, **Java**, **Node.js** (fetch, grammY), **Go**, **cURL** va **HTML/JS**'da yozilgan. Yordamchi modullar tashqi kutubxonasiz ishlaydi.

> [!IMPORTANT]
> Bot premium emoji'ni ko'rsata olishi uchun **ikki shartdan biri** bajarilishi kerak (Bot API 9.4, 2026-yil fevral):
> 1. bot **Fragment'da qo'shimcha username** sotib olgan bo'lsa — hamma joyda ishlaydi;
> 2. bot **egasida Telegram Premium** bo'lsa — faqat bot **shaxsiy chat, guruh va superguruhga** to'g'ridan-to'g'ri yuborgan xabarlarda ishlaydi (kanal postlarida ishlamaydi).
>
> Shart bajarilmasa, foydalanuvchi premium emoji o'rniga uning ichidagi **oddiy emoji**'ni ko'radi.

## 📚 Mundarija

- [Pack'lar](#-packlar)
- [Ko'p ishlatiladigan emoji'lar](#-kop-ishlatiladigan-emojilar)
- [Loyiha tuzilishi](#-loyiha-tuzilishi)
- [Asosiy qoidalar](#-asosiy-qoidalar)
- [Xabarda premium emoji: 3 usul](#-xabarda-premium-emoji-3-usul)
- [Tugmalarda ikonka va rang](#-tugmalarda-ikonka-va-rang)
- [Kelgan emoji ID'sini aniqlash](#-kelgan-emoji-idsini-aniqlash)
- [Tillar bo'yicha namunalar](#-tillar-boyicha-namunalar)
- [Saytda foydalanish](#-saytda-foydalanish)
- [Ma'lumot formatlari](#-malumot-formatlari)
- [Muammolar va yechimlar](#-muammolar-va-yechimlar)
- [Manbalar](#-manbalar)
- [Litsenziya](#-litsenziya)

---

## 📦 Pack'lar

| Pack (`set_name`) | Nomi | Soni | To'liq jadval | Telegram'ga qo'shish |
|---|---|---:|---|---|
| `tgiosicons` | Telegram iOS Icons | 399 | [docs/packs/tgiosicons.md](docs/packs/tgiosicons.md) | [t.me/addemoji/tgiosicons](https://t.me/addemoji/tgiosicons) |
| `RestrictedEmoji` | Animated Emoji | 997 | [docs/packs/RestrictedEmoji.md](docs/packs/RestrictedEmoji.md) | [t.me/addemoji/RestrictedEmoji](https://t.me/addemoji/RestrictedEmoji) |
| `AdaptiveStatus` | 𝖲𝗍𝖺𝗍𝗎𝗌 - @OrderEmoji | 171 | [docs/packs/AdaptiveStatus.md](docs/packs/AdaptiveStatus.md) | [t.me/addemoji/AdaptiveStatus](https://t.me/addemoji/AdaptiveStatus) |
| `Fl0rkHDMaydroid` | Flork HD - @TelemojisMaydroid | 78 | [docs/packs/Fl0rkHDMaydroid.md](docs/packs/Fl0rkHDMaydroid.md) | [t.me/addemoji/Fl0rkHDMaydroid](https://t.me/addemoji/Fl0rkHDMaydroid) |
| | **Jami** | **1 645** | | |

- **tgiosicons** — Telegram iOS ilovasi uslubidagi interfeys ikonkalari: sozlamalar, papka, qulf, strelkalar va boshqalar. Tugma ikonkalari uchun eng qulay pack.
- **RestrictedEmoji** — standart emoji'larning animatsiyali versiyalari: yuzlar, qo'llar, hayvonlar, ovqat, bayroqlar (🇺🇿 ham bor).
- **AdaptiveStatus** — status uslubidagi ixcham ikonkalar va 0️⃣–9️⃣ raqamlar.
- **Fl0rkHDMaydroid** — Flork personaji bilan stiker uslubidagi emoji'lar.

Bitta oddiy emoji'ga bir nechta premium variant to'g'ri kelishi mumkin (masalan, `tgiosicons`'da 6 ta ⚙️ bor). Qaysi biri kerakligini [veb-katalog](#-saytda-foydalanish)da yoki Telegram'da pack'ni ochib tanlang.

## ⭐ Ko'p ishlatiladigan emoji'lar

| Emoji | Vazifasi | `custom_emoji_id` | Pack |
|:---:|---|---|---|
| ✅ | Tasdiqlash | `5774022692642492953` | `tgiosicons` |
| ❌ | Bekor qilish | `6030757850274336631` | `tgiosicons` |
| ⚙️ | Sozlamalar | `5904258298764334001` | `tgiosicons` |
| 👤 | Profil | `6032994772321309200` | `tgiosicons` |
| 🔔 | Bildirishnoma | `6039486778597970865` | `tgiosicons` |
| 🔒 | Xavfsizlik | `6037249452824072506` | `tgiosicons` |
| 🛡 | Himoya | `6030537007350944596` | `tgiosicons` |
| 💎 | Premium | `5776023601941582822` | `tgiosicons` |
| ⭐️ | Yulduz | `6028338546736107668` | `tgiosicons` |
| 🎁 | Sovg'a | `5773677501825945508` | `tgiosicons` |
| 📍 | Manzil | `6030399199030284183` | `tgiosicons` |
| 💬 | Chat | `6030784887093464891` | `tgiosicons` |
| 🔎 | Qidiruv | `6032850693348399258` | `tgiosicons` |
| 🗑 | O'chirish | `6039522349517115015` | `tgiosicons` |
| 👍 | Like | `5469770542288478598` | `RestrictedEmoji` |
| 🔥 | Olov | `5420315771991497307` | `RestrictedEmoji` |
| 🎉 | Tabrik | `5436040291507247633` | `RestrictedEmoji` |
| ❤️ | Yurak | `5449505950283078474` | `RestrictedEmoji` |
| 🇺🇿 | O'zbekiston | `5449829434334912605` | `RestrictedEmoji` |
| 😂 | Flork kulgi | `4920369071792325179` | `Fl0rkHDMaydroid` |
| 🚀 | Raketa | `5316571734604790521` | `AdaptiveStatus` |

## 🗂 Loyiha tuzilishi

```text
Emoj-To-Web/
├── data/
│   ├── raw/                 # asl jadvallar (.txt)
│   ├── json/<pack>.json     # har bir pack alohida
│   ├── csv/<pack>.csv
│   ├── all.json             # hammasi bitta faylda (namunalar shuni o'qiydi)
│   ├── all.csv
│   └── packs.json           # pack'lar ro'yxati: nom, soni, havola
├── docs/packs/<pack>.md     # GitHub'da ko'rish uchun to'liq jadvallar
├── examples/
│   ├── python/              # premium_emoji.py, send_raw.py, aiogram_bot.py, ptb_bot.py
│   ├── php/                 # PremiumEmoji.php, send.php, webhook.php
│   ├── java/                # PremiumEmojiBot.java
│   ├── nodejs/              # premiumEmoji.mjs, send.mjs, grammy_bot.mjs
│   ├── go/                  # main.go
│   ├── curl/                # examples.sh
│   └── web/                 # index.html — qidiruvli emoji katalogi
└── tools/
    ├── build_data.py        # data/raw → json, csv, docs
    └── download_icons.py    # emoji fayllarini Bot API orqali yuklab olish
```

## 📏 Asosiy qoidalar

1. **ID'ni doim satr (string) sifatida saqlang.** `custom_emoji_id` 19 xonali son. JavaScript `Number`, PHP 32-bit `int` yoki JSON'ni sonli parse qilish uni buzadi: `5420315771991497307` → `5420315771991498000`.
2. **Premium emoji ichida oddiy emoji bo'lishi shart.** `<tg-emoji emoji-id="…">🔥</tg-emoji>` ichidagi 🔥 — zaxira (fallback). Premium ko'rinmasa, shu chiqadi. Jadvaldagi `emoji` ustuni aynan shu belgi.
3. **Entity `offset` va `length` UTF-16 kod birliklarida.** 👍 = 2 birlik, 🇺🇿 = 4 birlik, ⚙️ = 2 birlik. Java va JavaScript'da `string.length` allaqachon UTF-16. Python, PHP va Go'da alohida hisoblash kerak (namunalarda `utf16_len` bor).
4. **Tugma ikonkasi** — `icon_custom_emoji_id` maydoni, ikonka tugma matnidan oldin chiqadi. Tugma matniga emoji yozish shart emas.
5. **Tugma rangi** — `style`: `"primary"` (ko'k), `"success"` (yashil), `"danger"` (qizil). Berilmasa, ilovaning standart rangi ishlatiladi.
6. **Premium ko'rindimi, tekshiring.** `sendMessage` javobidagi `result.entities` ichida `custom_emoji` bo'lmasa, Telegram uni oddiy emoji'ga aylantirgan.

## 💬 Xabarda premium emoji: 3 usul

### 1. HTML (`parse_mode: "HTML"`)

```html
Salom <tg-emoji emoji-id="5449829434334912605">🇺🇿</tg-emoji> premium <tg-emoji emoji-id="5420315771991497307">🔥</tg-emoji>
```

### 2. MarkdownV2 (`parse_mode: "MarkdownV2"`)

```text
Salom ![🇺🇿](tg://emoji?id=5449829434334912605) premium ![🔥](tg://emoji?id=5420315771991497307)\!
```

> [!NOTE]
> MarkdownV2'da ``_ * [ ] ( ) ~ ` > # + - = | { } . !`` belgilari `\` bilan ekranlanadi.

### 3. Entities (`parse_mode`siz)

```json
{
  "chat_id": 123456789,
  "text": "Entities: 👍",
  "entities": [
    { "type": "custom_emoji", "offset": 10, "length": 2, "custom_emoji_id": "5469770542288478598" }
  ]
}
```

Matnni kod orqali yig'ganda, foydalanuvchi kiritgan matnni ekranlash bilan ovora bo'lmaslik uchun eng ishonchli usul shu.

## 🎛 Tugmalarda ikonka va rang

**Inline tugma:**

```json
{
  "inline_keyboard": [[
    { "text": "Tasdiqlash",   "callback_data": "ok", "icon_custom_emoji_id": "5774022692642492953", "style": "success" },
    { "text": "Bekor qilish", "callback_data": "no", "icon_custom_emoji_id": "6030757850274336631", "style": "danger" }
  ]]
}
```

**Reply (pastki) klaviatura:**

```json
{
  "resize_keyboard": true,
  "keyboard": [[
    { "text": "Profil",     "icon_custom_emoji_id": "6032994772321309200" },
    { "text": "Sozlamalar", "icon_custom_emoji_id": "5904258298764334001", "style": "primary" }
  ]]
}
```

Reply tugma bosilganda botga faqat `text` keladi, ikonka kelmaydi.

## 🔍 Kelgan emoji ID'sini aniqlash

Foydalanuvchi premium emoji yuborsa, `message.entities` ichida shunday yozuv keladi:

```json
{ "type": "custom_emoji", "offset": 0, "length": 2, "custom_emoji_id": "5420315771991497307" }
```

Emoji haqida batafsil ma'lumot (`set_name`, fayl, animatsiya turi) olish uchun:

```bash
curl -s "https://api.telegram.org/bot$BOT_TOKEN/getCustomEmojiStickers" \
  -H 'Content-Type: application/json' \
  -d '{"custom_emoji_ids": ["5420315771991497307"]}'
```

Bir so'rovda ko'pi bilan **200 ta** ID yuborish mumkin. Javobdagi `set_name` orqali `getStickerSet` bilan butun pack'ni olasiz.

Tayyor handler'lar: [`aiogram_bot.py`](examples/python/aiogram_bot.py), [`webhook.php`](examples/php/webhook.php), [`grammy_bot.mjs`](examples/nodejs/grammy_bot.mjs). Ular yuborilgan emoji'ning ID'sini, pack'ini va tayyor HTML kodini qaytaradi.

## 🧑‍💻 Tillar bo'yicha namunalar

Hamma namunalar `BOT_TOKEN` va `CHAT_ID` muhit o'zgaruvchilarini o'qiydi va emoji'larni `data/all.json` (Java'da `data/all.csv`) dan nomi bo'yicha topadi. ID'larni qo'lda ko'chirish shart emas.

<details open>
<summary><b>🐍 Python</b> — <a href="examples/python">examples/python</a></summary>

```python
from premium_emoji import EmojiCatalog, tg_emoji, md_emoji, EntityTextBuilder, inline_button

cat  = EmojiCatalog.load()
fire = cat.first("🔥", pack="RestrictedEmoji")
ok   = cat.first("✅", pack="tgiosicons")

text = f"Salom {tg_emoji(fire.id, fire.emoji)}"                # HTML
md   = f"Salom {md_emoji(fire.id, fire.emoji)}"                # MarkdownV2
plain, entities = EntityTextBuilder().text("Salom ").emoji(fire.id, fire.emoji).build()
button = inline_button("Tasdiqlash", "ok", icon_id=ok.id, style="success")
```

**aiogram 3:**

```python
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="Tasdiqlash", callback_data="ok",
                         icon_custom_emoji_id="5774022692642492953", style="success"),
]])
await message.answer('Tayyor <tg-emoji emoji-id="5420315771991497307">🔥</tg-emoji>',
                     parse_mode="HTML", reply_markup=kb)
```

**python-telegram-bot (22.7+):**

```python
InlineKeyboardButton("Premium", callback_data="buy",
                     icon_custom_emoji_id="6028338546736107668", style="primary")
```

```bash
cd examples/python
BOT_TOKEN=123:ABC CHAT_ID=123456789 python send_raw.py     # kutubxonasiz
pip install -r requirements.txt
BOT_TOKEN=123:ABC python aiogram_bot.py                    # /start va emoji ID aniqlash
```

</details>

<details>
<summary><b>🐘 PHP</b> — <a href="examples/php">examples/php</a></summary>

```php
require 'PremiumEmoji.php';

$cat  = PremiumEmoji::load();
$fire = $cat->first('🔥', 'RestrictedEmoji');
$ok   = $cat->first('✅', 'tgiosicons');

$params = [
    'chat_id'      => $chatId,
    'parse_mode'   => 'HTML',
    'text'         => 'Salom ' . PremiumEmoji::html($fire['id'], $fire['emoji']),
    'reply_markup' => ['inline_keyboard' => [[
        PremiumEmoji::button('Tasdiqlash', 'ok', $ok['id'], 'success'),
    ]]],
];
```

```bash
cd examples/php
BOT_TOKEN=123:ABC CHAT_ID=123456789 php send.php
```

`webhook.php` — webhook rejimidagi bot: premium emoji yuborilsa, ID'sini qaytaradi.

</details>

<details>
<summary><b>☕ Java</b> — <a href="examples/java">examples/java</a></summary>

```java
String html = "<tg-emoji emoji-id=\"" + fire.id() + "\">" + fire.emoji() + "</tg-emoji>";

// entity: Java'da String.length() UTF-16 sanaydi
String prefix = "Entities: ";
int offset = prefix.length();
int length = like.emoji().length();
```

```bash
cd examples/java
javac PremiumEmojiBot.java
BOT_TOKEN=123:ABC CHAT_ID=123456789 java -Dstdout.encoding=UTF-8 PremiumEmojiBot
```

[TelegramBots](https://github.com/rubenlagus/TelegramBots) kutubxonasida maydon odatda shu nom bilan builder'da bo'ladi: `InlineKeyboardButton.builder().text("...").callbackData("...").iconCustomEmojiId("...")`. Kutubxona versiyangiz Bot API 9.4'ni qo'llab-quvvatlashini tekshiring.

</details>

<details>
<summary><b>🟩 Node.js</b> — <a href="examples/nodejs">examples/nodejs</a></summary>

```js
import { loadCatalog, tgEmoji, entityText, button } from './premiumEmoji.mjs';

const cat  = await loadCatalog();
const fire = cat.first('🔥', 'RestrictedEmoji');
const ok   = cat.first('✅', 'tgiosicons');

await call('sendMessage', {
  chat_id: CHAT_ID,
  parse_mode: 'HTML',
  text: `Salom ${tgEmoji(fire.id, fire.emoji)}`,
  reply_markup: { inline_keyboard: [[button('Tasdiqlash', 'ok', ok.id, 'success')]] },
});

await call('sendMessage', { chat_id: CHAT_ID, ...entityText(['Salom ', fire]) });
```

```bash
cd examples/nodejs
BOT_TOKEN=123:ABC CHAT_ID=123456789 node send.mjs
npm install && BOT_TOKEN=123:ABC node grammy_bot.mjs
```

</details>

<details>
<summary><b>🐹 Go</b> — <a href="examples/go">examples/go</a></summary>

```go
type Button struct {
    Text              string `json:"text"`
    CallbackData      string `json:"callback_data"`
    IconCustomEmojiID string `json:"icon_custom_emoji_id,omitempty"`
    Style             string `json:"style,omitempty"`
}

func UTF16Len(s string) int { return len(utf16.Encode([]rune(s))) }
```

```bash
cd examples/go
BOT_TOKEN=123:ABC CHAT_ID=123456789 go run .
```

</details>

<details>
<summary><b>🌀 cURL</b> — <a href="examples/curl/examples.sh">examples/curl/examples.sh</a></summary>

```bash
curl -s "https://api.telegram.org/bot$BOT_TOKEN/sendMessage" \
  -H 'Content-Type: application/json' \
  -d '{"chat_id":"'"$CHAT_ID"'","parse_mode":"HTML",
       "text":"Salom <tg-emoji emoji-id=\"5420315771991497307\">🔥</tg-emoji>"}'
```

Skriptda HTML, MarkdownV2, entities, reply klaviatura va `getCustomEmojiStickers` namunalari bor.

</details>

## 🌐 Saytda foydalanish

### Emoji katalogi

[`examples/web/index.html`](examples/web/index.html) — barcha 1 645 ta emoji'ni ko'rsatadigan sahifa. Pack bo'yicha filtr, emoji yoki ID bo'yicha qidiruv bor. Emoji bosilsa, ID, HTML, MarkdownV2, tugma JSON va Python kodini bitta tugma bilan nusxalash mumkin.

```bash
python -m http.server 8000
# brauzerda: http://localhost:8000/examples/web/
```

Sahifa avval lokal `data/all.json`'ni o'qiydi, topilmasa GitHub'dagi nusxasini oladi.

### Haqiqiy premium ikonkalarni ko'rsatish

Brauzer `custom_emoji_id` orqali rasmni o'zi chiqara olmaydi, faylni avval Bot API orqali yuklab olish kerak:

```bash
BOT_TOKEN=123:ABC python tools/download_icons.py              # hamma pack
BOT_TOKEN=123:ABC python tools/download_icons.py tgiosicons   # bitta pack
BOT_TOKEN=123:ABC python tools/download_icons.py --thumb      # faqat kichik WEBP preview
```

Fayllar `icons/<pack>/<id>.<ext>` ga, ro'yxat `icons/manifest.json` ga yoziladi. Katalog sahifasi manifest'ni topsa, oddiy emoji o'rniga haqiqiy ikonkalarni ko'rsatadi. Istalgan bot token yetadi, Premium shart emas.

| Fayl | Turi | Saytda qanday ko'rsatiladi |
|---|---|---|
| `.webp` | statik | `<img src="…" width="24" height="24">` |
| `.webm` | video | `<video src="…" autoplay loop muted playsinline>` |
| `.tgs` | Lottie animatsiya (gzip) | [lottie-web](https://github.com/airbnb/lottie-web) bilan |

**TGS'ni lottie-web bilan ko'rsatish:**

```html
<div id="anim" style="width:48px;height:48px"></div>
<script src="https://cdn.jsdelivr.net/npm/lottie-web@5.12.2/build/player/lottie_light.min.js"></script>
<script>
  // .tgs = gzip qilingan Lottie JSON, brauzerning o'zi ochadi
  fetch('icons/RestrictedEmoji/5420315771991497307.tgs')
    .then((r) => new Response(r.body.pipeThrough(new DecompressionStream('gzip'))).json())
    .then((data) => lottie.loadAnimation({
      container: document.getElementById('anim'), renderer: 'svg', loop: true, autoplay: true, animationData: data,
    }));
</script>
```

> [!TIP]
> Saytda ko'p ikonka bo'lsa, `--thumb` bilan olingan kichik WEBP preview'larni ishlating: yengil va hamma brauzerda ishlaydi. Animatsiyani faqat foydalanuvchi ko'rib turgan joyda yoqing.

> [!WARNING]
> Emoji dizaynlari pack mualliflariga tegishli. Yuklab olingan fayllarni tijorat saytida ishlatishdan oldin pack egasining shartlarini tekshiring. `icons/` papkasi `.gitignore`'da, shuning uchun repoga tushmaydi.

## 🧾 Ma'lumot formatlari

**`data/all.json`:**

```json
{
  "total": 1645,
  "packs": [
    {
      "set_name": "tgiosicons",
      "title": "Telegram iOS Icons",
      "count": 399,
      "url": "https://t.me/addemoji/tgiosicons",
      "emojis": [
        { "n": 1, "id": "6028346797368283073", "emoji": "✈️" }
      ]
    }
  ]
}
```

**`data/all.csv`:**

```csv
set_name,n,custom_emoji_id,emoji
tgiosicons,1,6028346797368283073,✈️
```

**Yangi pack qo'shish:** jadvalni `data/raw/<set_name>.txt` ga qo'ying (mavjud fayllar formatida) va quyidagini ishga tushiring:

```bash
python tools/build_data.py
```

Skript qatorlar sonini sarlavhadagi son bilan solishtiradi, tartib raqamlari uzilmaganini va pack'lar orasida takroriy ID yo'qligini tekshiradi, keyin JSON, CSV va `docs/packs/*.md` fayllarini qayta yaratadi.

## 🛠 Muammolar va yechimlar

| Muammo | Sabab va yechim |
|---|---|
| Premium o'rniga oddiy emoji chiqyapti | Bot egasida Telegram Premium yo'q yoki bot Fragment username sotib olmagan. Yoki xabar kanalga yuborilgan: Premium egasi yo'li faqat shaxsiy chat, guruh va superguruhda ishlaydi. |
| Tugmada ikonka ko'rinmayapti | Shart yuqoridagi bilan bir xil. Telegram mijozingiz (ilova versiyasi) ham yangi bo'lishi kerak. |
| `Bad Request: can't parse entities` | HTML'da `<`, `>`, `&` ekranlanmagan yoki MarkdownV2'da `.` `!` `-` kabi belgilar `\` bilan ekranlanmagan. |
| Emoji noto'g'ri joyga tushdi yoki matn qirqildi | `offset`/`length` baytlarda yoki Unicode belgilarda hisoblangan. UTF-16 kod birliklarida hisoblang. |
| ID oxiri `000` bo'lib qoldi | ID son sifatida parse qilingan. Uni satr sifatida saqlang. |
| `getCustomEmojiStickers` bo'sh ro'yxat qaytardi | ID noto'g'ri yoki pack o'chirilgan. ID'ni `data/all.json` bilan solishtiring. |
| `Too Many Requests: retry after N` | Juda tez so'rov yuborilgan. `download_icons.py` buni o'zi kutib, qayta urinadi. |

## 🔗 Manbalar

- [Telegram Bot API](https://core.telegram.org/bots/api): `MessageEntity`, `InlineKeyboardButton`, `KeyboardButton`, `getCustomEmojiStickers`
- [Bot API changelog — 9.4](https://core.telegram.org/bots/api-changelog): custom emoji va tugma ikonkalari uchun yangi qoidalar
- [Formatting options](https://core.telegram.org/bots/api#formatting-options): HTML va MarkdownV2 sintaksisi
- [Custom emoji (MTProto)](https://core.telegram.org/api/custom-emoji)

## 📄 Litsenziya

Kod va ma'lumot fayllari [MIT](LICENSE) litsenziyasi ostida. Emoji dizaynlari va pack'lar ularning mualliflariga tegishli. Bu repo faqat ularning ochiq `custom_emoji_id` ro'yxatini va ishlatish namunalarini o'z ichiga oladi.

<div align="center">

**Muallif:** [Hayotbek Ismoilov](https://github.com/ismoillooff)

</div>
