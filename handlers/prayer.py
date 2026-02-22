from loader import bot
from services.prayer import get_prayer_times

@bot.message_handler(commands=['prayer'])
def prayer_command(message):
    bot.send_message(
        message.chat.id,
        "Send city and country like:\nSeoul, South Korea"
    )
@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, "Assalamu Alaikum 🤲\n if you want to search pray times \n just click this /prayer")
@bot.message_handler(func=lambda m: m.text and "," in m.text)
def handle_city(message):
    try:
        city, country = message.text.split(",")
        result = get_prayer_times(city.strip(), country.strip())

        if not result:
            bot.send_message(message.chat.id, "City not found ❌")
            return

        text = (
            f"🕌 Prayer Times for {city.strip()}\n\n"
            f"Fajr: {result['Fajr']}\n"
            f"Dhuhr: {result['Dhuhr']}\n"
            f"Asr: {result['Asr']}\n"
            f"Maghrib: {result['Maghrib']}\n"
            f"Isha: {result['Isha']}\n"
            "if you want other cities's \n"
            "just click /prayer"
        )

        bot.send_message(message.chat.id, text)

    except:
        bot.send_message(message.chat.id, "Wrong format ❌")