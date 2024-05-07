import logging, asyncio, sys

from loader import dp, bot
import handlers
from utils.notify_admins import on_startup_notify

async def main() -> None:    
    # botning adminlariga xabar yuborish 
    await on_startup_notify()

    # botnign boshlang'ich buyruqlarini o'rnatish
    
    # 
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())