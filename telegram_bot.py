import logging
from telegram.ext.filters import Filtersfrom telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from queue import Queue

update_queue = Queue()
logging.basicConfig(level=logging.INFO)

TOKEN = 'TOKEN'  # Replace with your bot token

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Привет! Я буду перенаправлять ваши сообщения моему создателю, можете задать свой вопрос в этом чате!')

def forward_message(update, context):
    context.bot.forward_message(chat_id=TOKEN,  # Replace with your chat ID
                                from_chat_id=update.effective_chat.id,
                                message_id=update.message.message_id)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, forward_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()