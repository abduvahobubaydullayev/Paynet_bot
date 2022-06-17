from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

language_buttons = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text='Uzbek', callback_data='uz'),
			InlineKeyboardButton(text='Russa', callback_data='ru'),
			InlineKeyboardButton(text='USA', callback_data='us'),
		]
	]
	)

lesson_buttons = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text='Rus tili', callback_data='lru'),
			InlineKeyboardButton(text='Ingliz tili', callback_data='lus'),
			InlineKeyboardButton(text='Arab tili', callback_data='lar'),
		]
	]
)

lesson_time_buttons = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text='1 - smena', callback_data='lus11'),
			InlineKeyboardButton(text='2 - smena', callback_data='lus12'),
		]
	]
)

registration_done = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text='Ha', callback_data='ha'),
			InlineKeyboardButton(text='Yo`q', callback_data='yoq'),
		]
	]
)

lesson_done_buttons = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text='Ha', callback_data='ha_lesson'),
			InlineKeyboardButton(text='Yo`q', callback_data='yoq_lesson'),
		]
	]
)