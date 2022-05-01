from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup 


@Client.on_message(filters.command("start"))
async def start(client, m: Message):
   if m.chat.type == 'private':
       await m.reply(f"**Hey I am GodEyeMusic \n\n** \n`Add bot to your Group and Make it Admin \n2) **Commands** : \n`/play` song name",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                     InlineKeyboardButton(
                                            "Support", url="t.me/GodEyeSupport")
                                    ]]
                            ))
   else:
      await m.reply(f"**Hey I Am Alive Baby ✨**")
