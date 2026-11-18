// Premium emoji'li xabar va ikonkali tugmalar (Go, faqat standart kutubxona).
//
//	go run . -data ../../data/all.json
//	BOT_TOKEN=123:ABC CHAT_ID=123456789 go run .
package main

import (
	"bytes"
	"encoding/json"
	"flag"
	"fmt"
	"html"
	"log"
	"net/http"
	"os"
	"strings"
	"unicode/utf16"
)

type Emoji struct {
	N     int    `json:"n"`
	ID    string `json:"id"` // ID'ni string saqlang
	Emoji string `json:"emoji"`
	Pack  string `json:"-"`
}

type catalog struct {
	Packs []struct {
		SetName string  `json:"set_name"`
		Emojis  []Emoji `json:"emojis"`
	} `json:"packs"`
}

func loadCatalog(path string) ([]Emoji, error) {
	raw, err := os.ReadFile(path)
	if err != nil {
		return nil, err
	}
	var c catalog
	if err := json.Unmarshal(raw, &c); err != nil {
		return nil, err
	}
	var all []Emoji
	for _, p := range c.Packs {
		for _, e := range p.Emojis {
			e.Pack = p.SetName
			all = append(all, e)
		}
	}
	return all, nil
}

func first(all []Emoji, emoji, pack string) Emoji {
	key := strings.ReplaceAll(emoji, "️", "")
	for _, e := range all {
		if strings.ReplaceAll(e.Emoji, "️", "") == key && (pack == "" || e.Pack == pack) {
			return e
		}
	}
	log.Fatalf("topilmadi: %s", emoji)
	return Emoji{}
}

// TgEmoji — parse_mode=HTML uchun.
func TgEmoji(e Emoji) string {
	return fmt.Sprintf(`<tg-emoji emoji-id="%s">%s</tg-emoji>`, e.ID, html.EscapeString(e.Emoji))
}

// MdEmoji — parse_mode=MarkdownV2 uchun.
func MdEmoji(e Emoji) string {
	return fmt.Sprintf("![%s](tg://emoji?id=%s)", e.Emoji, e.ID)
}

// UTF16Len — Telegram entity offset/length UTF-16 kod birliklarida.
func UTF16Len(s string) int { return len(utf16.Encode([]rune(s))) }

type Button struct {
	Text              string `json:"text"`
	CallbackData      string `json:"callback_data"`
	IconCustomEmojiID string `json:"icon_custom_emoji_id,omitempty"`
	Style             string `json:"style,omitempty"` // primary | success | danger
}

type Entity struct {
	Type          string `json:"type"`
	Offset        int    `json:"offset"`
	Length        int    `json:"length"`
	CustomEmojiID string `json:"custom_emoji_id"`
}

func call(token, method string, params any) {
	body, _ := json.Marshal(params)
	resp, err := http.Post("https://api.telegram.org/bot"+token+"/"+method, "application/json", bytes.NewReader(body))
	if err != nil {
		log.Println(method, err)
		return
	}
	defer resp.Body.Close()
	var r struct {
		OK          bool   `json:"ok"`
		Description string `json:"description"`
	}
	_ = json.NewDecoder(resp.Body).Decode(&r)
	fmt.Println(method, r.OK, r.Description)
}

func main() {
	dataPath := flag.String("data", "../../data/all.json", "data/all.json yo'li")
	flag.Parse()

	all, err := loadCatalog(*dataPath)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(len(all), "ta emoji yuklandi")

	fire := first(all, "🔥", "RestrictedEmoji")
	like := first(all, "👍", "RestrictedEmoji")
	ok := first(all, "✅", "tgiosicons")
	no := first(all, "❌", "tgiosicons")
	fmt.Println(TgEmoji(fire))
	fmt.Println(MdEmoji(like))

	token, chatID := os.Getenv("BOT_TOKEN"), os.Getenv("CHAT_ID")
	if token == "" || chatID == "" {
		fmt.Println("Xabar yuborish uchun BOT_TOKEN va CHAT_ID bering.")
		return
	}

	// 1) HTML + tugmalar
	call(token, "sendMessage", map[string]any{
		"chat_id":    chatID,
		"parse_mode": "HTML",
		"text":       "<b>Go</b> premium emoji " + TgEmoji(fire),
		"reply_markup": map[string]any{
			"inline_keyboard": [][]Button{{
				{Text: "Ha", CallbackData: "yes", IconCustomEmojiID: ok.ID, Style: "success"},
				{Text: "Yo'q", CallbackData: "no", IconCustomEmojiID: no.ID, Style: "danger"},
			}},
		},
	})

	// 2) entities
	prefix := "Entities: "
	call(token, "sendMessage", map[string]any{
		"chat_id": chatID,
		"text":    prefix + like.Emoji,
		"entities": []Entity{{
			Type: "custom_emoji", Offset: UTF16Len(prefix), Length: UTF16Len(like.Emoji), CustomEmojiID: like.ID,
		}},
	})
}
