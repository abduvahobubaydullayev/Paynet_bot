"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
from config import *
from buttons import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import CallbackQuery

go_back = ''
# Configure logging
logging.basicConfig(level=logging.INFO)

login = ''
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    print(message.chat.id)
    if message.chat.id == 5297643424:
        await message.answer(text='Assalomu aleykum! Admin', reply_markup=admin_buttons)
    else:
        await message.answer(text="Congratulations! You subscribed to Paynet bot ga."
                                  "\n\nUse /off to pause your subscription.", )
        await message.answer(text="Want to create your own bot? \nGo to @Manybot", reply_markup=header_menu1)


@dp.message_handler(text='Kanallar')
async def kanallar(message: types.Message):
    await message.answer(text='Kanallar holatini bilish!!', reply_markup=kanllar_buttons)


@dp.message_handler(text='Kanal')
async def kanal(message: types.Message):
    await message.answer(text='Kanal holati!!', reply_markup=kanal_buttons)


@dp.message_handler(text='Kanal qo`shish')
async def add_canal(message: types.Message):
    global login
    login = message.text
    print(login)
    await message.answer(text="Yangi kanal havolasini kiriitng: \n Misol uchun : https://t.me/paynetbot kabi")


@dp.message_handler(text='https://t.me/%')
async def add_canal(message: types.Message):
    print(True)
    if login == 'Kanal qo`shish':
        await message.answer(text='Yangi kanal qo`shildi!', reply_markup=kanal_buttons)


@dp.message_handler(text='O`chirish')
async def Delete(message: types.Message):
    await message.answer(text='O`chirildi..!')


@dp.message_handler(text='O`zgartrish')
async def Update(message: types.Message):
    await message.answer(text='*** malumotni o`zgartirish! \n uchun yangi holatni ko`rsating!')


@dp.message_handler(text='🤑 Pul ishlash')
async def pul_ishlash(message: types.Message):
    global go_back
    go_back = message.text
    await message.answer(text='Pul ishlash 🤑', reply_markup=pul_ishlash_buttons)


@dp.message_handler(text='💰 Balans')
async def balance(message: types.Message):
    global go_back
    go_back = message.text
    await message.answer(text='Balans 🤑')
    await message.answer(text='💰Sizning hisobingizda: **** so\'m mavjud\n💵 Umumiy ishlagan '
                              'pullaringiz: **** so\'m \n💸 Yechib oldingiz: **** so\'m \n'
                              '💳 Sizning karta raqamingiz: karta raqam\n📞 Paynet uchun '
                              'tel nomeringiz: tel nomer', reply_markup=balance_buttons)


@dp.message_handler(text='📤 Pulni yechib olish')
async def pul_yechish(message: types.Message):
    global go_back
    go_back = message.text
    await message.answer(text='👇 To\'lov turini tanlang', reply_markup=pul_yechish_buttons)


@dp.message_handler(text='👤 Shaxsiy Kabinet')
async def pul_yechish(message: types.Message):
    global go_back
    go_back = message.text
    await message.answer(
        text='👤 Shaxsiy KabinetAssalomu alaykum (Foydalanuvchi niki) \n\n✅ Ismingiz: Ism \n✅ Jinsingiz: Jins\n'
             '✅ Yoshingiz: Yosh \n✅ Manzil: Manzil\n✅ Tel nomeringiz: nomer\n\n👥 Do\'stlaringiz: **** ta'
             '\n📎 Shaxsiy referal linkingiz: https://t.me/paynetbot?reflink216274368')


@dp.message_handler(text='📋 Qoidalar')
async def qoidalar(message: types.Message):
    global go_back
    go_back = message.text
    await message.answer(text='👮‍♂ Qoidalar')


#
@dp.message_handler(text='👨🏻‍💻 Bog\'lanish')
async def qoidalar(message: types.Message):
    global go_back
    go_back = message.text
    await message.answer(text='📞 Kontakt')


@dp.message_handler(text='⚙️ Sozlash')
async def qoidalar(message: types.Message):
    global go_back
    go_back = message.text
    await message.answer(text='⚙️ Sozlash', reply_markup=setting_buttons)


@dp.message_handler(text='🇺🇿 Tilni tanlash')
async def qoidalar(message: types.Message):
    global go_back
    go_back = message.text
    await message.answer(text='🇺🇿 Tilni tanlash')


@dp.message_handler(text='💳 Hisob raqamni almashtirish')
async def qoidalar(message: types.Message):
    global go_back
    go_back = message.text
    await message.answer(text='💳 Hisob raqamni almashtirish', reply_markup=change_click_buttons)


@dp.message_handler(text='💳 Click raqamini o\'zgartirish')
async def qoidalar(message: types.Message):
    if message.chat.id == admin:
        pass
    else:
        global go_back
        go_back = message.text
        await message.answer(text='Yangi click raqamini kiriting:')


@dp.message_handler(text='📞 Tel nomerni o\'zgartirish')
async def qoidalar(message: types.Message):
    if message.chat.id == admin:
        pass
    else:
        global go_back
        go_back = message.text
        await message.answer(text='📞 Yangi tel nomer kiriting:')


@dp.message_handler(text='👤 Shaxsiy ma\'lumotlarni o\'zgartirish')
async def qoidalar(message: types.Message):
    global go_back
    go_back = message.text
    await message.answer(text='👤 Shaxsiy ma\'lumotlarni o\'zgartirish')


@dp.message_handler(text='👥 Do\'stlarni taklif qilish')
async def qoidalar(message: types.Message):
    global go_back
    go_back = message.text
    await message.answer(
        text='📎 Ushbu referal linkini do\'stlaringizga yuboring \n👉 https://t.me/paynetbot?refllink216294947 '
             '\n🤖 Botdan har bir ro\'yxatdan o\'tgan do\'stingiz uchun sizga: 250 so\'m to\'lanadi \n'
             '💸 Pullaringizni paynet orqali yoki karta raqamingizga yechib olishingiz mumkin')


@dp.message_handler(text='📲 Vazifa bajarish')
async def qoidalar(message: types.Message):
    global go_back
    go_back = message.text
    await message.answer(text='📲 Internetda vazifa bajarib pul ishlash')


@dp.message_handler(text='💳 Click')
async def qoidalar(message: types.Message):
    global go_back
    go_back = message.text
    await message.answer(
        text='Click raqamingiz: 0000 0000 0000 0000 \nAgar boshqa kartaga pul yechmoqchi bo\'lsangiz /sozlash bo\'limidan '
             'karta raqamini o\'zgartiring')


@dp.message_handler(text='🟢 Paynet')
async def qoidalar(message: types.Message):
    global go_back
    go_back = message.text
    await message.answer(
        text='Paynet uchun tel nomeringiz: +998***** \nAgar boshqa nomerga pul yechmoqchi bo\'lsangiz /sozlash bo\'limidan '
             'nomerni o\'zgartiring')


@dp.message_handler(text='Go Back')
async def go_back(message: types.Message):
    if message.chat.id == admin:
        pass
    else:
        global go_back
        if go_back in ['🤑 Pul ishlash', '👥 Do\'stlarni taklif qilish', '📲 Vazifa bajarish',
                       '💰 Balans', '📤 Pulni yechib olish', '⚙️ Sozlash', '🇺🇿 Tilni tanlash',
                       '👤 Shaxsiy ma\'lumotlarni o\'zgartirish', ]:
            await message.answer(text='Main Menu', reply_markup=header_menu1)
        elif go_back in ['💳 Click', '🟢 Paynet']:
            go_back = '💰 Balans'
            await message.answer(text='Balans 🤑')
            await message.answer(text='💰Sizning hisobingizda: **** so\'m mavjud\n💵 Umumiy ishlagan '
                                      'pullaringiz:<br> **** so\'m 💸 Yechib oldingiz: **** so\'m </br>'
                                      '💳 Sizning karta raqamingiz: karta raqam📞 Paynet uchun '
                                      'tel nomeringiz: tel nomer', reply_markup=balance_buttons)
        elif go_back in ['💳 Hisob raqamni almashtirish', '💳 Click raqamini o\'zgartirish',
                         '📞 Tel nomerni o\'zgartirish']:
            go_back = '⚙️ Sozlash'
            await message.answer(text='⚙️ Sozlash', reply_markup=setting_buttons)


@dp.message_handler(text='Statistika')
async def statistika(message: types.Message):
    if message.chat.id == admin:
        await message.answer('Statistika!!!', reply_markup=statistika_buttons)


@dp.message_handler()
async def send_welcome(message: types.Message):
    if message.chat.id == admin:
        await message.answer("Congratulations! You subscribed to Paynet bot ga."
                             " Use /off to pause your subscription.", reply_markup=admin_buttons)
    else:
        await message.answer("Congratulations! You subscribed to Paynet bot ga."
                             " Use /off to pause your subscription.", reply_markup=header_menu1)


@dp.message_handler(text='+998%')
async def create_number(message: types.Message):
    pass


#
# @dp.callback_query_handler(text="uz")
# async def menu_tanlash(call: CallbackQuery):
#     print(call)
#     await call.message.answer(f'<b>Assalomu aleykum!!!</b>', parse_mode='HTML')
#     print(call)
#
#
# @dp.message_handler()
# async def create(message: types.Message):
#     print(message)
#     await message.answer(message)
#
#
# #
# # @dp.message_handler()
# # async def echo(message: types.Message):
# #     print(message.text)
# #     # old style:
# #     # await bot.send_message(message.chat.id, message.text)
# #
# #     await message.answer(message.text)
# #

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
