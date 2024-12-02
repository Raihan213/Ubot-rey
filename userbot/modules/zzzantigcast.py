from pyrogram import Client, filters, idle
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
import re
import os

from pyrogram.types import EmojiStatus, MessageEntity
from pyrogram import types
from pyrogram.raw.types import ReactionCustomEmoji, ReactionEmoji, TextWithEntities
from pyrogram.enums import MessageEntityType, ChatType
from pyrogram.raw import functions
from pyrogram.errors.exceptions.bad_request_400 import ReactionInvalid, MessageTooLong

from pyrogram.raw.functions.messages import TranslateText
from userbot.core.database import mongo_client
from userbot import *

__MODULE__ = "antigcast"
__HELP__ = """
bantuan untuk antigcast

• perintah: <code>{0}on</code> [on atau off]
• penjelasan: untuk menghidupkan atau mematikan antigcast

• perintah: <code>{0}listuser</code>
• penjelasan: untuk melihat daftar pengguna yang di balcklist.

• perintah: <code>{0}adduser</code>
• penjelasan: untuk menambah pengguna ke dalam database antigcast

• perintah: <code>{0}rmuser</code>
• penjelasan: untuk menghapus pengguna di dalam database antigcast

• perintah: <code>{0}lihat</code>
• penjelasan: untuk melihat apakah antigcast telah di aktifkan

• perintah: <code>{0}addgp</code>
• penjelasan: untuk menambah grup sebagai antigcast

• perintah: <code>{0}listgp</code>
• penjelasan: untuk melihat grup antigcast

• perintah: <code>{0}at</code> balas ke pesan
• penjelasan: untuk menambah pesan antigcast

• perintah: <code>{0}strdb</code>
• penjelasan: untuk mengecek daftar kata yg di blacklist

• perintah: <code>{0}rmkat</code>
• penjelasan: untuk menghapus kata yang di blacklist

"""


db = mongo_client["DOR"]
user_collection = db["user_dia"]
gc = db["listgrup"]
psnz = db["msg_text"]

async def get_user_ids(client_id):
    user_ids = await user_collection.find_one({"_id": client_id})
    return user_ids["user_dia"] if user_ids else []

async def get_blacklist_status(client_id):
    blacklist_status = await db.settings.find_one({"_id": client_id})
    return blacklist_status["status"] if blacklist_status else False

async def set_blacklist_status(client_id, status):
    await db.settings.update_one({"_id": client_id}, {"$set": {"status": status}}, upsert=True)

async def get_chat_ids(client_id):
    chat_ids = await gc.find_one({"_id": client_id})
    return chat_ids["grup"] if chat_ids else []

async def get_msg_ids(client_id):
    msg_ids = await psnz.find_one({"_id": client_id})
    return msg_ids["msg_text"] if msg_ids else []

async def purge(message):
    await asyncio.sleep(0.5)
    await message.delete()

def get_message(message):
    msg = (
        message.reply_to_message
        if message.reply_to_message
        else ""
        if len(message.command) < 2
        else " ".join(message.command[1:])
    )
    return msg

def emoji(alias):
    emojis = {
        "bintang": "<emoji id=5931592939514892319>⭐</emoji>",
        "loading": "<emoji id=5801044672658805468>✨</emoji>",
        "proses": "<emoji id=6276248783525251352>🔄</emoji>",
        "gagal": "<emoji id=6278161560095426411>❌</emoji>",
        "done": "<emoji id=5852871561983299073>✅</emoji>",
        "upload": "<emoji id=5911100572508885928>♻️</emoji>",
        "roses": "<emoji id=5341312820698948923>🙃</emoji>",
        "selesai": "<emoji id=5341576484446283436>😎</emoji>",
        "on": "<emoji id=6275808772715710450>🎚️</emoji>",
        "off": "<emoji id=6276295366740543459>⛔</emoji>",
        "daftar": "<emoji id=5974045315391556490>📝</emoji>",
    }
    return emojis.get(alias, "Emoji tidak ditemukan.")

Q = emoji("bintang")
gagal = emoji("gagal")
prs = emoji("proses")
batal = emoji("gagal")
rs = emoji("roses")
sls = emoji("selesai")
dn = emoji("done")
on = emoji("on")
off = emoji("off")
dftr = emoji("daftar")

@CB.UBOT("adduser", sudo=True)
async def add_user_to_blacklist(c, m):
    if len(m.command) != 2 and not m.reply_to_message:
        await m.reply_text(f"{batal}**ɢᴜɴᴀᴋᴀɴ ғᴏʀᴍᴀᴛ** : `adduser` **ᴜsᴇʀ ɪᴅ ᴀᴛᴀᴜ ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ ᴜɴᴛᴜᴋ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ᴅᴀғᴛᴀʀ ᴀɴᴛɪɢᴄᴀsᴛ {Q}**", quote=True)
        return

    if m.reply_to_message:
        user_id = m.reply_to_message.from_user.id
    else:
        user_id = int(m.command[1])

    user_ids = await get_user_ids(c.me.id)
    if user_id not in user_ids:
        user_ids.append(user_id)
        await user_collection.update_one({"_id": c.me.id}, {"$set": {"user_dia": user_ids}}, upsert=True)
        await m.reply_text(f"{Q}**ᴜsᴇʀ ᴅᴇɴɢᴀɴ ɪᴅ** `{user_id}` **ᴛᴇʟᴀʜ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ᴅᴀғᴛᴀʀ ᴀɴᴛɪɢᴄᴀsᴛ** {dn}", quote=True)
    else:
        await m.reply_text(f"{dn}**ᴜsᴇʀ ᴛᴇʀsᴇʙᴜᴛ sᴜᴅᴀʜ ᴀᴅᴀ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ ᴀɴᴛɪɢᴄᴀsᴛ {Q}**", quote=True)

@CB.UBOT("listuser", sudo=True)
async def display_blacklist(client, message):
    user_ids = await get_user_ids(client.me.id)
    await message.reply_text(f"{dftr} ɪɴɪ ʜᴀsɪʟɴʏᴀ : `{user_ids}`\n", quote=True)

@CB.UBOT("rmuser", sudo=True)
async def remove_user_from_blacklist(c, m):
    if len(m.command) != 2 and not m.reply_to_message:
        await m.reply_text(f"{batal}**ɢᴜɴᴀᴋᴀɴ ғᴏʀᴍᴀᴛ** : `rmuser` **ᴜsᴇʀ ɪᴅ ᴀᴛᴀᴜ ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs ᴅᴀʀɪ ᴅᴀғᴛᴀʀ ᴀɴᴛɪɢᴄᴀsᴛ {Q}**", quote=True)
        return

    if m.reply_to_message:
        user_id = m.reply_to_message.from_user.id
    else:
        user_id = int(m.command[1])

    user_ids = await get_user_ids(c.me.id)
    if user_id in user_ids:
        user_ids.remove(user_id)
        await user_collection.update_one({"_id": c.me.id}, {"$set": {"user_dia": user_ids}}, upsert=True)
        await m.reply_text(f"{Q}**ᴜsᴇʀ ᴅᴇɴɢᴀɴ ɪᴅ** `{user_id}` **ᴛᴇʟᴀʜ ᴅɪʜᴀᴘᴜs ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ ᴀɴᴛɪɢᴄᴀsᴛ** {dn}", quote=True)
    else:
        await m.reply_text(f"{Q}**ᴜsᴇʀ ᴛᴇʀsᴇʙᴜᴛ ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ ᴀɴᴛɪɢᴄᴀsᴛ {gagal}**", quote=True)

@CB.UBOT("lihat", sudo=True)
async def checkstatus(client, message):
    cek = await get_blacklist_status(client.me.id)
    if cek == True:
        await message.reply_text(f"{Q}**ᴀɴᴅᴀ sᴜᴅᴀʜ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴀɴᴛɪɢᴄᴀsᴛ**{dn}", quote=True)
    else:
        await message.reply_text(f"{Q}**ᴀɴᴅᴀ ʙᴇʟᴜᴍ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴀɴᴛɪɢᴄᴀsᴛ**{gagal}", quote=True)        

@CB.UBOT("on", sudo=True)
async def enable_blacklist(c, m):
    await set_blacklist_status(c.me.id, True)
    await m.reply_text(f"{Q}**ᴀɴᴛɪɢᴄᴀsᴛ ᴜsᴇʀ ʙᴇʀʜᴀsɪʟ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ** {on}", quote=True)

@CB.UBOT("off", sudo=True)
async def disable_blacklist(c, m):
    await set_blacklist_status(c.me.id, False)
    await m.reply_text(f"{Q}**ᴀɴᴛɪɢᴄᴀsᴛ ᴜsᴇʀ ʙᴇʀʜᴀsɪʟ ᴅɪ ᴍᴀᴛɪᴋᴀɴ** {off}", quote=True)

@CB.UBOT("addgp", sudo=True)
async def add_group_to_antigcast(c, m):
    type = (ChatType.GROUP, ChatType.SUPERGROUP)

    if m.chat.type not in type:
        await m.reply_text(f"{gagal}ɢᴜɴᴀᴋᴀɴ ғɪᴛᴜʀ ɪɴɪ ᴅɪ ɢʀᴜᴘ!")
        return

    user_id = m.chat.id
    chat_ids = await get_chat_ids(c.me.id)
    if user_id not in chat_ids:
        chat_ids.append(user_id)
        await gc.update_one({"_id": c.me.id}, {"$set": {"grup": chat_ids}}, upsert=True)
        await m.reply_text(f"{Q}**ɢʀᴜᴘ ᴅᴇɴɢᴀɴ ɪᴅ** `{user_id}` **ᴛᴇʟᴀʜ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ᴅᴀғᴛᴀʀ ᴀɴᴛɪɢᴄᴀsᴛ** {dn}", quote=True)
    else:
        await m.reply_text(f"{dn}**ɢʀᴜᴘ ᴛᴇʀsᴇʙᴜᴛ sᴜᴅᴀʜ ᴀᴅᴀ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ ᴀɴᴛɪɢᴄᴀsᴛ {Q}**", quote=True)

@CB.UBOT("rmgp", sudo=True)
async def remove_group_from_antigcast(c, m):
    type = (ChatType.GROUP, ChatType.SUPERGROUP)
    if m.chat.type not in type:
        await m.reply_text(f"{gagal} Gunakan fitur ini di grup atau berikan ID grup", quote=True)
        return

    chat_id = None
    if len(m.command) >= 2:
        try:
            chat_id = int(m.command[1])
        except ValueError:
            await m.reply_text(f"{gagal} ID grup tidak valid", quote=True)
            return

    if not chat_id:
        chat_id = m.chat.id

    chat_ids = await get_chat_ids(c.me.id)
    if chat_id in chat_ids:
        chat_ids.remove(chat_id)
        await gc.update_one({"_id": c.me.id}, {"$set": {"grup": chat_ids}}, upsert=True)
        await m.reply_text(f"{Q} Grup dengan ID {chat_id} telah dihapus dari daftar antigcast {dn}", quote=True)
    else:
        await m.reply_text(f"{Q} Grup dengan ID {chat_id} tidak ada dalam daftar antigcast {gagal}", quote=True)


@CB.UBOT("listgp", sudo=False)
async def display_antigcast(c, m):
    user_ids = await get_chat_ids(c.me.id)
    await m.reply_text(f"{dftr}**ᴅᴀғᴛᴀʀ ɢʀᴜᴘ ᴀɴᴛɪɢᴄᴀsᴛ** : `{user_ids}` \n", quote=True)

@CB.UBOT("bl", sudo=True)
async def add_pesan(c, m):
    _rply = m.reply_to_message
    if not _rply:
        await m.reply(f"mohon balas ke pengguna")
        return    
    user_text = _rply.text
    msg_ids = await get_msg_ids(c.me.id)
    if user_text not in msg_ids:
        msg_ids.append(user_text)
        await psnz.update_one({"_id": c.me.id}, {"$set": {"msg_text": msg_ids}}, upsert=True)
        sukses = await m.reply_text(f"pesan {user_text} berhasil di tambahkan ke database{dn}", quote=True)
        await _rply.delete()
        await purge(m)
        await sukses.delete()
    else:
        x = await m.reply_text(f"pesan sudah ada di dalam database{gagal}", quote=True)
        await asyncio.sleep(0.5)
        await x.delete()

@CB.UBOT("strdb", sudo=False)
async def strdb(client, message):
    pesan = await get_msg_ids(client.me.id)
    try:
        await message.reply_text(pesan)
    except MessageTooLong:
        with open("db.txt", "a", encoding="utf-8") as file:
            file.write(f"{pesan}\n")
        kirim = await message.reply_document(db.txt)
        if kirim:
            os.remove("db.txt")

@CB.UBOT("rmkat", sudo=True)
async def remove_kata_from_blacklist(c, m):
    if len(m.command) != 2 and not m.reply_to_message:
        await m.reply_text(f"{batal}**ɢᴜɴᴀᴋᴀɴ ғᴏʀᴍᴀᴛ** : `rmkat` **ᴜsᴇʀ ɪᴅ ᴀᴛᴀᴜ ʙᴀʟᴀs ᴋᴇ ᴘᴇsᴀɴ ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs ᴅᴀʀɪ ᴅᴀғᴛᴀʀ ᴀɴᴛɪɢᴄᴀsᴛ {Q}**", quote=True)
        return

    if m.reply_to_message:
        user_id = m.reply_to_message.text
    else:
        user_id = " ".join(m.command[1:])

    user_ids = await get_msg_ids(c.me.id)
    if user_id in user_ids:
        user_ids.remove(user_id)
        await psnz.update_one({"_id": c.me.id}, {"$set": {"msg_text": user_ids}}, upsert=True)
        await m.reply_text(f"{Q}**ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢʜᴀᴘᴜs** `{user_id}` **ᴅᴀʀɪ ᴅᴀғᴛᴀʀ ᴋᴀᴛᴀ ᴀɴᴛɪɢᴄᴀsᴛ** {dn}", quote=True)
    else:
        await m.reply_text(f"{Q}**ᴋᴀᴛᴀ ᴛᴇʀsᴇʙᴜᴛ ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ ᴀɴᴛɪɢᴄᴀsᴛ {gagal}**", quote=True)


@ubot.on_message(filters.group & ~filters.private & ~filters.me)
async def delete_messages(client, message):
    chat_ids = await get_chat_ids(client.me.id)
    if message.chat.id not in chat_ids:
        return    
    blacklist_status = await get_blacklist_status(client.me.id)
    if blacklist_status:
        sys = client.me.id
        user_ids = await get_user_ids(sys)
        user_msg = await get_msg_ids(sys)
        if message.from_user.id in user_ids:
            await message.delete()
        else:
            try:
                for pattern in user_msg:
                    if re.search(pattern, message.text, re.IGNORECASE):
                        await message.delete()
                        break
            except:
                pass