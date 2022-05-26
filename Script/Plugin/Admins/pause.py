from Script.assistant.TgCalls.Clients import bot, user

from pyrogram import filters
from Script.Config import OWNER_ID
import asyncio

from Script.Cache.admin_check import *

from Script.Plugin.Helpers.Player import QUEUE


@bot.on_message(filters.command("استئناف") & filters.group & filters.user(OWNER_ID))
@is_admin
async def pause(_, message):
    await message.delete()
    chat_id = message.chat.id
    if chat_id in QUEUE:
        try:
            await user.pause_stream(chat_id)
            await message.reply_text("⏸ Paused streaming.")
        except:
            await message.reply_text("❗Nothing is playing.")
    else:
        await message.reply_text("❗Nothing is playing.")
