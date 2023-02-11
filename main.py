import logging
from aiogram import Bot, Dispatcher, executor, types
import os

API_TOKEN = '6032451649:AAGzErz-p-U2ZajmKV9_zHxaoqpulrHJzL0'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def my_handler(message: types.Message):
    user = types.User.get_current()
    await message.reply(
        f'{user.full_name}, пришли мне аудио файл и я сконвертирую его в голосовое сообщение 😆\nДа я шалунишка')


@dp.message_handler(content_types=types.ContentType.AUDIO)
async def contents(ms: types.Message):
    file_id = ms.audio.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    await bot.download_file(file_path, "file.mp3")

    await bot.send_voice(ms.from_user.id, voice=(open('file.mp3', 'rb')))
    os.remove('file.mp3')


@dp.message_handler()
async def send_voice(message):
    # file_id = message.audio.file_id
    await message.reply('Дружище, извини но я могу только конвертировать аудио файлы😔😔😔')


executor.start_polling(dp, skip_updates=True)
