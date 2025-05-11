import telebot
import random
import os
import requests
from telebot import types

# Directly set your bot token here
ttoken = "7718460876:AAGAmxccor5ReArhz7Mu3gok8voHDNdfJpY"
bot = telebot.TeleBot(ttoken)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    key = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton(text='Channel', url='https://t.me/Dazai_hoster_updates')
    b2 = types.InlineKeyboardButton(text='Group', url='https://t.me/Dazai_hoster_chat')
    first = message.chat.first_name

    key.add(b1)
    key.add(b2)

    bot.send_photo(
        message.chat.id,
        'https://t.me/MarvelXVenom',
        caption=f'Hi {first}.\nWelcome to our free python host bot\nMade By: @Plugin\n\nPlease see the photo!\n*Send your python file first!*\n\n/help\n *To get the help page*\n\n/pip + Library name\n *To install a Library*\n\n/run + Your file Id\n *To run your bot!*',
        parse_mode='markdown',
        reply_markup=key
    )

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "Bot is running.")

# Start the bot
bot.polling()
