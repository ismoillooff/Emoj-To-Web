<?php
/**
 * Telegram premium (custom) emoji uchun yordamchi klass. Tashqi kutubxona kerak emas.
 *
 *   require 'PremiumEmoji.php';
 *   $cat  = PremiumEmoji::load();                       // ../../data/all.json
 *   $fire = $cat->first('🔥', 'RestrictedEmoji');
 *   echo PremiumEmoji::html($fire['id'], $fire['emoji']);
 */

declare(strict_types=1);

final class PremiumEmoji
{
    /** @var array<int, array{id:string, emoji:string, pack:string, n:int}> */
    private array $items = [];

    public static function load(?string $path = null): self
    {
        $path ??= __DIR__ . '/../../data/all.json';
        $data = json_decode((string) file_get_contents($path), true, 512, JSON_THROW_ON_ERROR);
        $self = new self();
        foreach ($data['packs'] as $pack) {
            foreach ($pack['emojis'] as $e) {
                $self->items[] = ['id' => $e['id'], 'emoji' => $e['emoji'], 'pack' => $pack['set_name'], 'n' => $e['n']];
            }
        }
        return $self;
    }

    public function count(): int
    {
        return count($this->items);
    }

    public function get(string $id): ?array
    {
        foreach ($this->items as $e) {
            if ($e['id'] === $id) {
                return $e;
            }
        }
        return null;
    }

    /** Oddiy emoji bo'yicha birinchi mosini qaytaradi (⭐ va ⭐️ bir xil). */
    public function first(string $emoji, ?string $pack = null): array
    {
        $key = self::stripVs($emoji);
        foreach ($this->items as $e) {
            if (self::stripVs($e['emoji']) === $key && ($pack === null || $e['pack'] === $pack)) {
                return $e;
            }
        }
        throw new RuntimeException("Emoji topilmadi: $emoji");
    }

    private static function stripVs(string $s): string
    {
        return str_replace("\u{FE0F}", '', $s);
    }

    /** parse_mode=HTML uchun. ID har doim satr: PHP int'ga o'girmang (19 xonali). */
    public static function html(string $id, string $fallback): string
    {
        return '<tg-emoji emoji-id="' . $id . '">' . htmlspecialchars($fallback, ENT_QUOTES) . '</tg-emoji>';
    }

    /** parse_mode=MarkdownV2 uchun. */
    public static function markdown(string $id, string $fallback): string
    {
        return "![$fallback](tg://emoji?id=$id)";
    }

    /** UTF-16 kod birliklaridagi uzunlik (entity offset/length uchun). */
    public static function utf16Length(string $s): int
    {
        return intdiv(strlen(mb_convert_encoding($s, 'UTF-16LE', 'UTF-8')), 2);
    }

    /** Kelgan xabardagi custom emoji'larni [[id, emoji], ...] ko'rinishida qaytaradi. */
    public static function extract(string $text, array $entities): array
    {
        $raw = mb_convert_encoding($text, 'UTF-16LE', 'UTF-8');
        $out = [];
        foreach ($entities as $ent) {
            if (($ent['type'] ?? '') !== 'custom_emoji') {
                continue;
            }
            $chunk = substr($raw, $ent['offset'] * 2, $ent['length'] * 2);
            $out[] = [$ent['custom_emoji_id'], mb_convert_encoding($chunk, 'UTF-8', 'UTF-16LE')];
        }
        return $out;
    }

    /** InlineKeyboardButton massivi. $style: primary | success | danger | null */
    public static function button(string $text, string $callbackData, ?string $iconId = null, ?string $style = null): array
    {
        $btn = ['text' => $text, 'callback_data' => $callbackData];
        if ($iconId !== null) {
            $btn['icon_custom_emoji_id'] = $iconId;
        }
        if ($style !== null) {
            $btn['style'] = $style;
        }
        return $btn;
    }
}
