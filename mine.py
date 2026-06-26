from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8920299263:AAEkoouqY3f0poCJ7yc9pbNEPS35x6b_27Q"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📸 Instagram", url="https://instagram.com/coding.boy17")],
        [InlineKeyboardButton("💻 GitHub", url="https://github.com/otabek-codings")],
        [InlineKeyboardButton("📢 Telegram kanal", url="https://t.me/+jgqFcBJm5J5jZmUy")],
        [InlineKeyboardButton("🌐 Saytim", url="https://exquisite-lollipop-1498f0.netlify.app")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Kerakli bo'limni tanlang:",
        reply_markup=reply_markup
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot ishga tushdi...")
app.run_polling()

# test