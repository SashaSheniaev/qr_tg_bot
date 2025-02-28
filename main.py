import telebot
import qrcode
from io import BytesIO

TOKEN = '7605107280:AAGO6aVD3L4u430n4ZkyWq_ydwEHZlgCXNY'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,'відправте мені будь який текст я згенирую кюаркод !')

@bot.message_handler(func=lambda message: True)
def generate_qr(message):
    qr = qrcode.QRCode(
        version = 1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size = 1, 
        border = 4
    )
    qr.add_data(message.text)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color= 'white')

    bio = BytesIO()
    bio.name = 'qr.png'
    img.save(bio, 'PNG')
    img.seek(0)
    bot.send_photo(message.chat.id, bio)

if __name__ == "__main__":
    bot.polling(none_stop=True)