import asyncio
from driver.core import calls, bot, user


async def start_bot():
    await bot.start()
    print("[INFO]: BOT & UBOT CLIENT STARTED !!")
    await calls.start()
    print("[INFO]: PY-TGCALLS CLIENT STARTED !!")
    await user.join_chat("TeamCodexun")
    await user.join_chat("Codexun")
    
loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
