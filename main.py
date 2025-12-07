from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ------------------ CONFIG ------------------
BOT_TOKEN = "8379136078:AAEiuwOIuTbiJE-4k3fbxdapqE5w11H7rkA"           # From BotFather
BTC_ADDRESS = "bc1q5je6vjlfxc5lv4r5fddrp2he7jmq7rvs0wmjlslyyw3hahhm62asfmzqv7"  # Where users send $50
VIDEO_LINK = "www.myvidfu.inv"         # Link to your video
ADMIN_ID = 5357220542        # Your Telegram numeric ID
PRICE_USD = 50
# --------------------------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text(
        f"💰 Welcome!\n\n"
        f"To access the video, please send **${PRICE_USD} in Bitcoin** to this address:\n\n"
        f"`{BTC_ADDRESS}`\n\n"
        "After sending payment, send me a screenshot.\n"
        "The system will verify it manually and grant access."
        , parse_mode="Markdown"
    )
    await update.message.reply_text(f"Your user ID is `{chat_id}` (use this when I approve you).", parse_mode="Markdown")

async def approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    if not context.args:
        await update.message.reply_text("Usage: /approve <user_id>")
        return

    user_id = context.args[0]
    try:
        await context.bot.send_message(chat_id=user_id, text=f"✅ Payment approved!\nHere is your video:\n{VIDEO_LINK}")
        await update.message.reply_text("User approved and video sent!")
    except Exception as e:
        await update.message.reply_text(f"Failed to send video: {e}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("approve", approve))
    app.run_polling()

if __name__ == "__main__":
    main()
  
