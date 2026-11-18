import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

/**
 * Premium emoji'li xabar va ikonkali tugmalar (Java 11+, tashqi kutubxonasiz).
 *
 *   javac PremiumEmojiBot.java
 *   BOT_TOKEN=123:ABC CHAT_ID=123456789 java -Dstdout.encoding=UTF-8 PremiumEmojiBot
 *
 * (-Dstdout.encoding=UTF-8 faqat konsolda emoji "?" bo'lib chiqmasligi uchun; Telegram'ga
 * yuborilayotgan JSON baribir UTF-8.)
 *
 * Java'da String.length() aynan UTF-16 kod birliklarini sanaydi,
 * shuning uchun entity offset/length uchun qo'shimcha hisob kerak emas.
 */
public class PremiumEmojiBot {

    /** data/all.csv dagi bitta qator. */
    record Emoji(String pack, int n, String id, String emoji) {}

    static List<Emoji> loadCatalog(Path csv) throws IOException {
        List<Emoji> out = new ArrayList<>();
        List<String> lines = Files.readAllLines(csv, StandardCharsets.UTF_8);
        for (String line : lines.subList(1, lines.size())) {
            String[] p = line.split(",", 4);          // set_name,n,custom_emoji_id,emoji
            out.add(new Emoji(p[0], Integer.parseInt(p[1]), p[2], p[3]));
        }
        return out;
    }

    static Emoji first(List<Emoji> all, String emoji, String pack) {
        String key = emoji.replace("️", "");
        return all.stream()
                .filter(e -> e.emoji().replace("️", "").equals(key))
                .filter(e -> pack == null || e.pack().equals(pack))
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("Topilmadi: " + emoji));
    }

    /** parse_mode=HTML uchun. */
    static String html(Emoji e) {
        return "<tg-emoji emoji-id=\"" + e.id() + "\">" + e.emoji() + "</tg-emoji>";
    }

    /** parse_mode=MarkdownV2 uchun. */
    static String markdown(Emoji e) {
        return "![" + e.emoji() + "](tg://emoji?id=" + e.id() + ")";
    }

    static String json(String s) {
        StringBuilder sb = new StringBuilder("\"");
        for (char c : s.toCharArray()) {
            switch (c) {
                case '"' -> sb.append("\\\"");
                case '\\' -> sb.append("\\\\");
                case '\n' -> sb.append("\\n");
                default -> sb.append(c);
            }
        }
        return sb.append('"').toString();
    }

    static String button(String text, String data, Emoji icon, String style) {
        return "{\"text\":" + json(text) + ",\"callback_data\":" + json(data)
                + (icon != null ? ",\"icon_custom_emoji_id\":" + json(icon.id()) : "")
                + (style != null ? ",\"style\":" + json(style) : "") + "}";
    }

    static String call(String token, String method, String body) throws Exception {
        HttpRequest req = HttpRequest.newBuilder(URI.create("https://api.telegram.org/bot" + token + "/" + method))
                .header("Content-Type", "application/json; charset=utf-8")
                .POST(HttpRequest.BodyPublishers.ofString(body, StandardCharsets.UTF_8))
                .build();
        return HttpClient.newHttpClient().send(req, HttpResponse.BodyHandlers.ofString()).body();
    }

    public static void main(String[] args) throws Exception {
        String token = System.getenv("BOT_TOKEN");
        String chatId = System.getenv("CHAT_ID");
        Path csv = Path.of(args.length > 0 ? args[0] : "../../data/all.csv");

        List<Emoji> all = loadCatalog(csv);
        System.out.println(all.size() + " ta emoji yuklandi");

        Emoji fire = first(all, "🔥", "RestrictedEmoji");
        Emoji like = first(all, "👍", "RestrictedEmoji");
        Emoji ok = first(all, "✅", "tgiosicons");
        Emoji no = first(all, "❌", "tgiosicons");
        System.out.println(html(fire));
        System.out.println(markdown(like));

        if (token == null || chatId == null) {
            System.out.println("Xabar yuborish uchun BOT_TOKEN va CHAT_ID bering.");
            return;
        }

        // 1) HTML + tugmalar
        String text = "<b>Java</b> premium emoji " + html(fire);
        String keyboard = "{\"inline_keyboard\":[[" + button("Ha", "yes", ok, "success") + ","
                + button("Yo'q", "no", no, "danger") + "]]}";
        System.out.println(call(token, "sendMessage",
                "{\"chat_id\":" + json(chatId) + ",\"parse_mode\":\"HTML\",\"text\":" + json(text)
                        + ",\"reply_markup\":" + keyboard + "}"));

        // 2) entities: offset = prefix.length() (Java'da UTF-16)
        String prefix = "Entities: ";
        String entities = "[{\"type\":\"custom_emoji\",\"offset\":" + prefix.length()
                + ",\"length\":" + like.emoji().length()
                + ",\"custom_emoji_id\":" + json(like.id()) + "}]";
        System.out.println(call(token, "sendMessage",
                "{\"chat_id\":" + json(chatId) + ",\"text\":" + json(prefix + like.emoji())
                        + ",\"entities\":" + entities + "}"));
    }
}
