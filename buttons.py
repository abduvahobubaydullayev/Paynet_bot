from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

statistika_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Foydalanuvchilar', ),
        ],
        [
            KeyboardButton(text='Ishlangan pullar', ),
            KeyboardButton(text='To`plangan pullar', ),
        ],
        [
            KeyboardButton(text='Go Back', ),
        ],

    ],
    resize_keyboard=True
)
kanllar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Kanal', ),
            KeyboardButton(text='Kanal qo`shish', ),
        ],
        [
            KeyboardButton(text='Go Back', ),
        ],
    ],
    resize_keyboard=True
)
kanal_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='O`chirish', ),
            KeyboardButton(text='O`zgartrish', ),
        ],
        [
            KeyboardButton(text='Go Back', ),
        ],
    ],
    resize_keyboard=True
)
admin_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Kanallar', ),
            KeyboardButton(text='Statistika', ),
        ],
        [
            KeyboardButton(text='Vazifalar', ),
            KeyboardButton(text='Qoidalar', ),
        ],
        [
            KeyboardButton(text='Aloqa', ),
        ],
    ],
    resize_keyboard=True
)
header_menu1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🤑 Pul ishlash', ),
        ],
        [
            KeyboardButton(text='💰 Balans', ),
            KeyboardButton(text='👤 Shaxsiy Kabinet', ),
        ],
        [
            KeyboardButton(text='📋 Qoidalar', ),
            KeyboardButton(text='👨🏻‍💻 Bog\'lanish', ),
        ],
        [
            KeyboardButton(text='⚙️ Sozlash', ),
        ],
    ],
    resize_keyboard=True
)

pul_ishlash_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='👥 Do\'stlarni taklif qilish', ),
        ],
        [
            KeyboardButton(text='📲 Vazifa bajarish', ),
        ],
        [
            KeyboardButton(text='Go Back', ),
        ],
    ],
    resize_keyboard=True
)

balance_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📤 Pulni yechib olish', ),
        ],
        [
            KeyboardButton(text='Go Back', ),
        ],
    ],
    resize_keyboard=True
)
pul_yechish_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='💳 Click', ),
        ],
        [
            KeyboardButton(text='🟢 Paynet', ),
        ],
        [
            KeyboardButton(text='Go Back', ),
        ],
    ],
    resize_keyboard=True
)
setting_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🇺🇿 Tilni tanlash'),
        ],
        [
            KeyboardButton(text='💳 Hisob raqamni almashtirish', ),
        ],
        [
            KeyboardButton(text='👤 Shaxsiy ma\'lumotlarni o\'zgartirish', ),
        ],
        [
            KeyboardButton(text='Go Back', ),
        ],
    ],
    resize_keyboard=True
)

change_click_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='💳 Click raqamini o\'zgartirish', ),
        ],
        [
            KeyboardButton(text='📞 Tel nomerni o\'zgartirish', ),
        ],
        [
            KeyboardButton(text='Go Back', ),
        ],
    ],
    resize_keyboard=True
)
