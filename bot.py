import telebot
bot = telebot.TeleBot('1483404579:AAHAlTiVOAGYNRfTxtdCGVjIr-BNfvLkqIU')
@bot.message_handler(commands=[ "c" , "ac", "club" ])
def send_sms(message):
        if message.chat.id != (-1001238978826):
                Chatid1 = "-1001238978826"
                bot.reply_to(message, "В работе!")
                message.text = message.text.replace('/club ', ' ')
                message.text = message.text.replace('/ac ', ' ')
                message.text = message.text.replace('/c ', ' ')
                bot.send_message(Chatid1, message.text, message.chat.id)
bot.polling(none_stop=True, interval=0)