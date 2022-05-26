import asyncio
import os
from Script.Plugin.Database import db
from Script.Config import LOG_CHANNEL
import datetime
import time

async def user_start(bot, indian):
    chat_id = indian.chat.id
    if not await db.is_user_exist(chat_id):
        await db.add_user(chat_id)
        await bot.send_message(
            LOG_CHANNEL,
            f"**📣 bot notification.** \n\n#NEW_USER **start use your bot!** \n\n🏷 name: `{indian.from_user.first_name}` \n📮 user id: `{indian.from_user.id}` \n🧝🏻‍♂️ profile: [{indian.from_user.first_name}](tg://user?id={indian.from_user.id})",
        )

    ban_status = await db.get_ban_status(chat_id)
    if ban_status["is_banned"]:
        if (
            datetime.date.today() - datetime.date.fromisoformat(ban_status["حظر"])
        ).days > ban_status["احظر"]:
            await db.remove_ban(chat_id)
        else:
            await indian.reply_text(
                f"اسف, انت محظور, اسال هنا @N_B_1 اذا كنت تعتقد ان هذا بالخطأ.",
                quote=True,
            )
            return
    await indian.continue_propagation()
