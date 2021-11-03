import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from parsing import get_news
from cats import get_cats
from db import get_info, set_user

# Объект бота
bot = Bot(token="")
# Диспетчер для бота
dp = Dispatcher(bot)
# Вывод в консоль
logging.basicConfig(level=logging.INFO)


@dp.message_handler(Text(equals="Бизнес"))
async def news_reply(message: types.Message):
    # Вызывается get_news (ответ пользователю на смс)
    await message.reply(get_news(message.from_user.id, 'biznes'))


@dp.message_handler(Text(equals="Животные"))
async def news_reply(message: types.Message):
    await message.reply(get_news(message.from_user.id, 'zhivotnye'))


@dp.message_handler(Text(equals="История"))
async def news_reply(message: types.Message):
    await message.reply(get_news(message.from_user.id, 'istoriya'))


@dp.message_handler(Text(equals="Культура"))
async def news_reply(message: types.Message):
    await message.reply(get_news(message.from_user.id, 'kultura'))


@dp.message_handler(Text(equals="Наука"))
async def news_reply(message: types.Message):
    await message.reply(get_news(message.from_user.id, 'nauka'))


@dp.message_handler(Text(equals="Новые технологии"))
async def news_reply(message: types.Message):
    await message.reply(get_news(message.from_user.id, 'novye-tehnologii'))


@dp.message_handler(Text(equals="Позитивные истории"))
async def news_reply(message: types.Message):
    await message.reply(get_news(message.from_user.id, 'pozitivnye-istorii'))


@dp.message_handler(Text(equals="Просто хорошие новости"))
async def news_reply(message: types.Message):
    await message.reply(get_news(message.from_user.id, 'prosto-horoshie-novosti'))


@dp.message_handler(Text(equals="Хорошие новости в мире"))
async def news_reply(message: types.Message):
    await message.reply(get_news(message.from_user.id, 'horoshie-novosti-v-mire'))


@dp.message_handler(Text(equals="Случайный котик"))
async def news_reply(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id, photo=get_cats())


def get_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Бизнес", "Животные", "История", "Культура", "Наука", "Новые технологии", "Позитивные истории",
               "Просто хорошие новости", "Хорошие новости в мире", 'Случайный котик']
    keyboard.add(*buttons)
    return keyboard


@dp.message_handler(commands="info")
async def cmd_start(message: types.Message):
    await message.answer(get_info(message.from_user.id), reply_markup=get_keyboard())


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    set_user(message.from_user.id)
    await message.answer("Привет, это бот с позитивнми новостями. Выбери категорию "
                         "или введи команду info для получения информации",
                         reply_markup=get_keyboard())


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
