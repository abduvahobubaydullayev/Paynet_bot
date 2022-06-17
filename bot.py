
import logging
from aiogram import Bot, Dispatcher, executor, types
from config import *
from buttons import *
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def sned_welcome(message:types.Message):
	await message.reply('Tilni tanlang!!!', reply_markup=language_buttons)

@dp.callback_quary_handler(text='uz')
async def registration(call:CallbackQuery):
	await.message.answer(f'Assalomu aleykum ')

	
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
