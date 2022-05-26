from Script.assistant.TgCalls.Clients import bot, user
from pyrogram import filters
from Script.Cache.admin_check import *
import asyncio
from Script.Plugin.Helpers.Player import skip_current_song, skip_item
from Script.Plugin.Helpers.Player import QUEUE 
from Script.Config import OWNER_ID


@bot.on_message(filters.command("اعبر") & filters.group & filters.user(OWNER_ID))
@is_admin
async def skip(_, message):
    await message.delete()
    chat_id = message.chat.id
    if len(message.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await message.reply_text("❗️Nothing in the queue to skip.")
        elif op == 1:
            await message.reply_text("❗️Empty queue, stopped streaming.")
    else:
        skip = message.text.split(None, 1)[1]
        out = "🗑 <b>Removed the following song(s) from the queue:</b> \n"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        out = out + "\n" + f"<b>#️⃣ {x}</b> - {hm}"
            await message.reply_text(out)

