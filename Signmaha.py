from sys import executable


from aiogram import Bot, Dispatcher, types
from aiogram.types import InputMediaVideo

TOKEN_API="7588050997:AAH8DBaJ3Mwo9Pg00guEqAW1i-s5tMyhFzM"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='<em>привет, забирай бесплатный видео-урок по гелю!</em>', parse_mode="HTML".upper())


@dp.message_handler(commands=['video'])
    async def video_command(message: types.Message):
        await bot.send_video(message.from_user.id,video='vNVLcQstils&si=BPr9fo5QCNDnlwDP')


@dp.message_handler(commands=['video'])
async def video_command(message: types.Message):
    await bot.send_video(message.from_user.id, video='')


@dp.message_handler(commands=['buy_course'])
async def photo_command(message: types.Message):
    await bot.send_photo(message.from_user.id, photo='vNVLcQstils&si=BPr9fo5QCNDnlwDP',text='в курсе вас ждет: подробный урок, четкий набор инструментов '



@dp.message_handler(commands=['buy'])
async def open_pay(message: types.Message):
        await message.answer(text="ссылка на покупку курса")
                            reply_markup=pay

if __name__ == '__main__':
    executable.start_polling(dp)

