import telebot

API_KEY = '2139263734:AAFPS2uGit79Wr6HsmsR669Na7z8Vu6HKdA'

bot = telebot.TeleBot(API_KEY)

bot.polling()

@bot.message_handler(commands=['link' or 'Link'])
def link(message):
    bot.reply_to(message, "Added to the playlist!")

