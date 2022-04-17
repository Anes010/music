import glob
import json
import logging
import asyncio

from pytgcalls.types import Update
from pyrogram.raw.base import Update

from pytgcalls.types.stream import StreamAudioEnded, StreamVideoEnded
from pyrogram import filters, Client
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
from pyrogram.types import Message
from Script.Plugin.Helpers.Player import QUEUE, add_to_queue, get_queue, clear_queue, pop_an_item, remove_queue
from Script.Cache.admin_check import *
from Script.assistant.TgCalls.Clients import bot, user, abhi



    
LIVE_CHATS = []

@Client.on_message(command("call") & other_filters)
@authorized_users_only
async def start_group_call(c: Client, m: Message):
    chat_id = m.chat.id
    msg = await c.send_message(chat_id, "`starting...`")
    try:
        peer = await user.resolve_peer(chat_id)
        await user.send(
            CreateGroupCall(
                peer=InputPeerChannel(
                    channel_id=peer.channel_id,
                    access_hash=peer.access_hash,
                ),
                random_id=user.rnd_id() // 9000000000,
            )
        )
        await msg.edit_text("✅ Group call started !")
    except ChatAdminRequired:
        await msg.edit_text(
            "The userbot is not admin in this chat. To start the Group call you must promote the userbot as admin first with permission:\n\n» ❌ manage_video_chats"
        )
# Bot Call End System


@Client.on_message(command("endcall") & other_filters)
@authorized_users_only
async def stop_group_call(c: Client, m: Message):
    chat_id = m.chat.id
    msg = await c.send_message(chat_id, "`stopping...`")
    try:
        if not (
            group_call := (
                await get_calls(m, err_msg="group call not active")
            )
        ):
            await msg.edit_text("❌ The group call already ended")
            return
        await user.send(
            DiscardGroupCall(
                call=group_call
            )
        )
        await msg.edit_text("✅ Group call has ended\n Try /call to turn it On Again!")
    except Exception as e:
        if "GROUPCALL_FORBIDDEN" in str(e):
            await msg.edit_text(
                "The userbot is not admin in this chat. To stop the Group call you must promote the userbot as admin first with permission:\n\n» ❌ manage_video_chats"
            )
