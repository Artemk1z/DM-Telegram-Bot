from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Твой chat ID
ADMIN_CHAT_ID = 'YOUR_CHAT_ID'

async def start(update: Update, context):
    await update.message.reply_text('Привет! Задай мне вопрос.')

async def handle_message(update: Update, context):
    user_question = update.message.text
    user = update.message.from_user

    # Отправка вопроса тебе (администратору)
    admin_message = f"Вопрос от @{user.username or user.first_name} (ID: {user.id}): {user_question}"
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=admin_message)

    # Ответ пользователю
    await update.message.reply_text('Спасибо за вопрос! Я отправлю его администратору.')

async def main():
    app = ApplicationBuilder().token('YOUR_TOKEN').build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    await app.start()
    await app.idle()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
