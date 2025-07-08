from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
BOT_TOKEN = 'token'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands='start'))
async def start_command(message: Message):
    await message.answer('Привет! \n Я Эхо-бот! \n Напиши мне что-нибудь')

@dp.message(Command(commands='help'))
async def help_command(message: Message):
    await message.answer(
        'Отправь мне любое сообщение, текст, фото, смайлик или стикер '   
        'А я буду повторять за тобой :)'
    )

@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(
            'Данный тип не поддерживается'
        )

if __name__ == '__main__':
    dp.run_polling(bot)