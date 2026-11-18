<?php
/**
 * Premium emoji'li xabar va ikonkali tugmalar yuborish (cURL).
 *
 *   BOT_TOKEN=123:ABC CHAT_ID=123456789 php send.php
 */

declare(strict_types=1);

require __DIR__ . '/PremiumEmoji.php';

$token  = getenv('BOT_TOKEN') ?: exit("BOT_TOKEN kerak\n");
$chatId = getenv('CHAT_ID') ?: exit("CHAT_ID kerak\n");

function tg(string $token, string $method, array $params): array
{
    $ch = curl_init("https://api.telegram.org/bot$token/$method");
    curl_setopt_array($ch, [
        CURLOPT_POST           => true,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HTTPHEADER     => ['Content-Type: application/json'],
        // JSON_UNESCAPED_UNICODE — emoji \uXXXX bo'lib ketmasin (ikkalasi ham ishlaydi, bu o'qishga qulay)
        CURLOPT_POSTFIELDS     => json_encode($params, JSON_UNESCAPED_UNICODE),
    ]);
    $res = curl_exec($ch);
    curl_close($ch);
    return json_decode((string) $res, true) ?? [];
}

$cat  = PremiumEmoji::load();
$fire = $cat->first('🔥', 'RestrictedEmoji');
$uz   = $cat->first('🇺🇿');
$ok   = $cat->first('✅', 'tgiosicons');
$no   = $cat->first('❌', 'tgiosicons');
$like = $cat->first('👍', 'RestrictedEmoji');

// 1) HTML + rangli, ikonkali tugmalar
$r = tg($token, 'sendMessage', [
    'chat_id'      => $chatId,
    'parse_mode'   => 'HTML',
    'text'         => '<b>PHP</b> ' . PremiumEmoji::html($uz['id'], $uz['emoji'])
                    . ' premium emoji ' . PremiumEmoji::html($fire['id'], $fire['emoji']),
    'reply_markup' => [
        'inline_keyboard' => [[
            PremiumEmoji::button('Ha', 'yes', $ok['id'], 'success'),
            PremiumEmoji::button("Yo'q", 'no', $no['id'], 'danger'),
        ]],
    ],
]);
echo 'HTML: ', var_export($r['ok'] ?? false, true), ' ', $r['description'] ?? '', PHP_EOL;

// 2) MarkdownV2
$r = tg($token, 'sendMessage', [
    'chat_id'    => $chatId,
    'parse_mode' => 'MarkdownV2',
    'text'       => '*MarkdownV2* ' . PremiumEmoji::markdown($like['id'], $like['emoji']) . ' ishlaydi\\!',
]);
echo 'MarkdownV2: ', var_export($r['ok'] ?? false, true), ' ', $r['description'] ?? '', PHP_EOL;

// 3) entities
$prefix = 'Entities: ';
$r = tg($token, 'sendMessage', [
    'chat_id'  => $chatId,
    'text'     => $prefix . $like['emoji'],
    'entities' => [[
        'type'            => 'custom_emoji',
        'offset'          => PremiumEmoji::utf16Length($prefix),
        'length'          => PremiumEmoji::utf16Length($like['emoji']),
        'custom_emoji_id' => $like['id'],
    ]],
]);
echo 'entities: ', var_export($r['ok'] ?? false, true), ' ', $r['description'] ?? '', PHP_EOL;
