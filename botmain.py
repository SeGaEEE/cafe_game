import asyncio
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import commands_handler, messages_handler


async def main() -> None:
    print("Бот работает")
    config=load_config('C:\Py\cafe_game2\.env')
    bot_token = config.tg_bot.token
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()
    dp.include_router(messages_handler.router)
    dp.include_router(commands_handler.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
