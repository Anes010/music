# main Kang With Credit
import asyncio
from Script.assistant.TgCalls.Clients import bot, user, abhi
from Script.Config import INDIAN_BOT as semx
from pytgcalls import idle
from Script.assistant.Keyboard.Connect import LOGGER


async def start_bot():
    await bot.start()
    LOGGER.info("[INFO]: BOT & USERBOT CLIENT STARTED !!")
    await user.start()
    LOGGER.info("[INFO]: PY-TGCALLS CLIENT STARTED !!")
    await abhi.join_chat("TheeDeCoDe")
    await abhi.join_chat("OffiCialDeCoDe")
    await abhi.send_message(f"{semx}", "/play")
    await idle()
    LOGGER.info("[INFO]: BOT & USERBOT STOPPED !!")
    await bot.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
