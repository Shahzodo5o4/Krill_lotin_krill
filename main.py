"""

20/02/2023

Kirill-lotin, lotin-kirill transliterator
TELEGRAM_BOT

Creator: Shahzod Bahronov

"""


from kiril_lotin import to_cyrillic, to_latin
import telebot

TOKEN = '6272274822:AAHJy9Ex9gXWUW0tlxNr8eqJg_09Nr0FOPU'
bot = telebot.TeleBot(TOKEN, parse_mode=None )

@bot.message_handler(commands=['start'])
def send_welcome(message):
    answer = "Assalomu alaykum, Xush kelibsiz !"
    answer += "\nBotdan foydalanish uchun kirill yoki lotin tilida matn kiriting: "
    bot.reply_to(message, answer )
    
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    letter = message.text
    if letter.isascii():
        answer2 = to_cyrillic(letter)
    else:
        answer2 = to_latin(letter)   
    bot.reply_to(message, answer2)

bot.polling()

