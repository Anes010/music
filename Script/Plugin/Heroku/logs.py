from pyrogram import Client, filters
from Script.Plugin.Helpers.Heroku import _check_heroku
from Script.Config import (
    OWNER_ID,
    HEROKU_APP_NAME,
)
from Script.Plugin.Helpers.Heroku import edit_or_send_as_file
from pyrogram.types import Message


@Client.on_message(filters.command(["سجلات"]) & filters.user(OWNER_ID))
@_check_heroku
async def logs(client: Client, message: Message, happ):
    msg = await message.reply_text("`please wait for a moment!`")
    logs = happ.get_log()
    capt = f"Heroku logs of `{HEROKU_APP_NAME}`"
    await edit_or_send_as_file(logs, msg, client, capt, "سجلات")
