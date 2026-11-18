<?php
/**
 * Webhook bot: foydalanuvchi premium emoji yuborsa, ID'sini va tayyor HTML kodini qaytaradi.
 *
 * O'rnatish:
 *   https://api.telegram.org/bot<TOKEN>/setWebhook?url=https://example.uz/webhook.php
 * Serverda BOT_TOKEN muhit o'zgaruvchisini bering (yoki pastdagi qatorni o'zgartiring).
 */

declare(strict_types=1);

require __DIR__ . '/PremiumEmoji.php';

$token  = getenv('BOT_TOKEN') ?: 'PUT_TOKEN_HERE';
$update = json_decode((string) file_get_contents('php://input'), true);
$msg    = $update['message'] ?? null;
if (!$msg || empty($msg['entities'])) {
    exit;
}

$cat   = PremiumEmoji::load();
$found = PremiumEmoji::extract($msg['text'] ?? '', $msg['entities']);
if (!$found) {
    exit;
}

$lines = [];
foreach ($found as [$id, $emoji]) {
    $known = $cat->get($id);
    $where = $known ? " · <code>{$known['pack']}</code> #{$known['n']}" : '';
    $lines[] = PremiumEmoji::html($id, $emoji) . " <code>$id</code>$where\n<code>"
             . htmlspecialchars(PremiumEmoji::html($id, $emoji)) . '</code>';
}

// Webhook javobida metodni to'g'ridan-to'g'ri qaytarish mumkin (alohida so'rovsiz)
header('Content-Type: application/json');
echo json_encode([
    'method'     => 'sendMessage',
    'chat_id'    => $msg['chat']['id'],
    'parse_mode' => 'HTML',
    'text'       => implode("\n\n", $lines),
], JSON_UNESCAPED_UNICODE);
