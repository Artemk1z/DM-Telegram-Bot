from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

ADMIN_CHAT_ID = 'Admin Chat Token'

TOKEN = 'Bot Token'

async def start(update: Update, context):
    await update.message.reply_text('Привет! Задай мне вопрос.')

async def handle_message(update: Update, context):
    user_question = update.message.text
    user = update.message.from_user

    admin_message = f"Вопрос от @{user.username or user.first_name} (ID: {user.id}): {user_question}"
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=admin_message)

    await update.message.reply_text('Спасибо за вопрос! Я отправлю его администратору.')

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    await app.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
