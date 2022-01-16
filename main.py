from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='5063718803:AAFFXeZeNlXdt-a2KdnqG53mXt40PQpfyjk')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет! \nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что нибудь, а тебе отправлю это в ответ!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, "я не понял, что вы хотели. \n Напишите команду /help")


if __name__ == '__main__':
    print("Бот запушен")
    executor.start_polling(dp)
