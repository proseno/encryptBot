import telebot
import config
import base64
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands='encode_bs64')
def encode_bs64(message):
    bot.reply_to(message, base64.encodebytes(bytes(message.text[13:], 'utf-8')))


@bot.message_handler(commands='decode_bs64')
def encode_bs64(message):
    bot.reply_to(message, base64.decodebytes(bytes(message.text[13:], 'utf-8')))


@bot.message_handler(commands='help_command')
def help_command(message):
    text = '''List of commands:
/encode_bs64 - encode symbols after command to base 64
/decode_bs64 - encode base 64 code after command to string
    '''
    bot.send_message(message.chat.id, text)


bot.polling()
