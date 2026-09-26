import telebot
import requests
TOKEN = "8895354739:AAG8uiHMFnWwHA--NOsN4I0DEZdsFwI12DU"

bot = telebot.TeleBot(TOKEN) 
URL = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hi,I\'m SMile What Can I Do For You?")

@bot.message_handler(func=lambda m: True)
def show_price(message):
	symbol = message.text.upper()
	response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}")
	if response.status_code == 200:
		date = response.json()
		bot.reply_to(message,f"{date['symbol']} price is {date['price']}")
	else:	
		bot.reply_to(message,"something is wrong...")
bot.infinity_polling()	