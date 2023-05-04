from aiogram import Bot, Dispatcher, executor, types
from api import API
import json

API_TOKEN = ''


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Initialize API
api = API()


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    '''Welcome'''
    await message.reply(
        "<b>Hi!\nI'm ToxicChecker by @vsecoder!</b>\nPowered by:\n - aiogram\n - <a href='https://github.com/vsecoder/ru-toxic-messages-classification'>API</a>.",
        parse_mode='HTML'
    )


@dp.message_handler()
async def check(message: types.Message):
    '''check toxic'''
    text = message.text if message.text else message.caption

    text = text.replace('<', '')
    text = text.replace('>', '')

    if len(text.split(" ")) < 3:
        await message.answer("Чем меньше текста, тем легче понять текст двусмысленно! Советуем больше 3х слов.")

    answer = json.dumps(
        api.check(text), 
        sort_keys=True, 
        indent=2
    )

    await message.reply(
        f'<code>{answer}</code>', # type: ignore
        parse_mode='HTML'
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
