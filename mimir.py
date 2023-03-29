import telebot
from telebot import util
import os
from dotenv import load_dotenv
from reply import answer
from db import read_db, create_db, update_db

load_dotenv()

greeting = "Hi there! I'm Mimir, a bot designed to provide intelligent responses and chat with you. How can I help you today?"

bot = telebot.TeleBot(os.getenv("BOT_KEY"))
print("running already")


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    idd = message.chat.id
    check = read_db(idd)
    if check["code"] == 0:
        create = create_db(idd)
    bot.reply_to(message, greeting)


@bot.message_handler(content_types=["text"])
def echo_all(message):
    idd = message.chat.id
    check = read_db(idd)
    count = check["count"]
    su = check["su"]
    status = check["status"]
    if count == 5 and su == False:
        reply = "Hi there! Please note that you can use mimir up to five times. After that, please contact Simeon for pricing and get unlimited access. Thank you for using mimir"
        bot.reply_to(message, reply)
    elif status == True or su == True:
        reply = answer(message.text)
        bot.reply_to(message, reply)
        real_count = count + 1
        if count == 5:
            update_db(idd, real_count, False)
        else:
            update_db(idd, real_count)


bot.infinity_polling()
