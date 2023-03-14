import logging

import wikipedia
from aiogram import Bot, Dispatcher, executor, types
wikipedia.set_lang('uz')
API_TOKEN = '6296909515:AAEzyKFh0hTM0B-cQjlRm3EmP191d6QVQm4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")



@dp.message_handler()
async def sendWiki(message: types.Message):
     try:
         respond = wikipedia.summary(message.text)
         await message.answer(respond)
     except:
         await message.answer('Bu mavzuga oid maqola topilmadi uzur qaytattan to`g`ri kiriting!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)