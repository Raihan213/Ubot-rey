import asyncio
import os

from gc import get_objects
from time import time
from pyrogram import Client, filters
from pyrogram.errors import RPCError
from pyrogram.types import *
from pyrogram import *
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                            InlineQueryResultArticle, InputTextMessageContent)

from PyroUbot import *

async def nyolongnih(client, message):
    await message.edit("Procesing...")
    link = get_arg(message)
    msg_id = int(link.split("/")[-1])
    if "t.me/c/" in link:
        try:
            chat = int("-100" + str(link.split("/")[-2]))
            dia = await client.get_messages(chat, msg_id)
        except RPCError:
            await message.edit("Looks like an error occurred")
    else:
        try:
            chat = str(link.split("/")[-2])
            dia = await client.get_messages(chat, msg_id)
        except RPCError:
            await message.edit("Looks like an error occurred")
    anjing = dia.caption or None
    if dia.text:
        await dia.copy(message.chat.id)
        await message.delete()
    if dia.photo:
        anu = await client.download_media(dia)
        await client.send_photo(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.video:
        anu = await client.download_media(dia)
        await client.send_video(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.audio:
        anu = await client.download_media(dia)
        await client.send_audio(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.voice:
        anu = await client.download_media(dia)
        await client.send_voice(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)

    if dia.document:
        anu = await client.download_media(dia)
        await client.send_document(message.chat.id, anu, anjing)
        await message.delete()
        os.remove(anu)
    else:
        await message.edit("Looks like an error occurred")
