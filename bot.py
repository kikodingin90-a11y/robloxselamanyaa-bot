import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    teks = (
        "🎮 SELAMAT DATANG DI ROBLOX SELAMANYAA!\n\n"
        "Menu utama:\n"
        "/harga - Lihat informasi harga\n"
        "/beli - Informasi pembelian resmi\n"
        "/admin - Hubungi admin\n\n"
        "Terima kasih sudah berkunjung!"
    )
    bot.reply_to(message, teks)

@bot.message_handler(commands=['harga'])
def harga(message):
    bot.reply_to(message, "Silakan cek harga pembelian melalui kanal resmi Roblox.")

@bot.message_handler(commands=['beli'])
def beli(message):
    bot.reply_to(message, "Untuk pembelian Robux, gunakan kanal resmi Roblox.")

@bot.message_handler(commands=['admin'])
def admin(message):
    bot.reply_to(message, "Admin: @robloxselamanyaa")

@bot.message_handler(func=lambda message: True)
def otomatis(message):
    bot.reply_to(message, "Pesan diterima! Ketik /start untuk melihat menu.")

bot.infinity_polling()
