'''
Content types:
text, audio, document, photo, sticker, video, voice.
'''

import telebot

TOKEN = "5905968257:AAHAStEFpMPZXmEJC_9-1H16NKS--U2GSKc"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def repeat(message: telebot.types.Message):
    bot.reply_to(message, f'Приветствую,{message.chat.username}')


@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass

bot.polling(none_stop=True)