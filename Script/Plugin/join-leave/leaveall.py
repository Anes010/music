import asyncio
from pyrogram import Client, filters
from Script.Config import OWNER_ID
from Script.assistant.TgCalls.Clients import abhi


@Client.on_message(filters.command(["غادر", "leaveall"]) & filters.user(OWNER_ID))
async def leaveall(client, message):
    if message.from_user.id not in OWNER_ID:
        return

    left = 0
    failed = 0
    lol = await message.reply("غادر كل المجموعات")
    async for dialog in abhi.iter_dialogs():
        try:
            await abhi.leave_chat(dialog.chat.id)
            left += 1
            await lol.edit(
                f"يتم المغادره... \n\nLeft: {left} chats. Failed: {failed} chats."
            )
        except:
            failed += 1
            await lol.edit(f"يتم المغادره... Left: {left} chats. Failed: {failed} chats.")
        await asyncio.sleep(0.7)
    await client.send_message(message.chat.id, f"Left {left} chats. Failed {failed} chats.")
