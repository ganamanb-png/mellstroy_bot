from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# 🔑 ВСТАВЬ СЮДА СВОЙ НОВЫЙ ТОКЕН ОТ BotFather
TOKEN = "8210670027:AAEyP1FHNUv1M6VU56lNsawRsJC--Z4qYRQ"

# 🌐 Ссылка на игру
GAME_URL = "https://mellstroy-game.netlify.app"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'play'])
async def start_game(msg: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(
        text="🎮 Играть", web_app=types.WebAppInfo(url=GAME_URL)
    ))
    await msg.answer("Добро пожаловать в Mellstroy Game! Жми, чтобы играть 👇", reply_markup=keyboard)

if __name__ == "__main__":
    print("✅ Mellstroy Game Bot запущен")
    executor.start_polling(dp)
