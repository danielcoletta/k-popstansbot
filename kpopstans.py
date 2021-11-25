import telegram
import logging
from telegram import Updater

updater = Updater(token='2139263734:AAFPS2uGit79Wr6HsmsR669Na7z8Vu6HKdA', use_context = True)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

from telegram import Update
from telegram.ext import Callbackcontext

def start(update: Update, context: Callbackcontext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Talk to me, bitch")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()









#bot = telegram.bot(token = '2139263734:AAFPS2uGit79Wr6HsmsR669Na7z8Vu6HKdA')

#print(bot.get_me())
#    {"first_name": "K-Pop Stans Bot", "username": "kpopstans_bot"}

#updates = bot.get_updates()
#print(updates[0])
#{'update_id': 218946040, 'message': {'message_id': 23833, 'date': 1626017436, 'text': 'Hi!', 'chat': {'type': 'private', 'last_name': 'Doe', 'username': 'JohnDoe', 'id': 1234567890, 'first_name': 'John'}, 'from': {'last_name': 'Doe', 'username': 'JohnDoe', 'id': 1234567890, 'is_bot': False, 'language_code': 'de', 'first_name': 'John'}, ...}}


