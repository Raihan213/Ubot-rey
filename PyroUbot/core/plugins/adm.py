import asyncio

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import ChatPermissions, ChatPrivileges, Message
from pyrogram.errors import *
from pyrogram.types import *

from PyroUbot import *

BANNED_USERS = filters.user()            


async def global_banned(client, message):
    user_id = await extract_user(message)
    Tm = await eor(message, "<code>ᴍᴇᴍᴘʀᴏꜱᴇꜱ....</code>")
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        await Tm.edit(
            "<code>gban</code> [ᴜꜱᴇʀ_ɪᴅ/ᴜꜱᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ]"
        )
    elif len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
    try:
        user = await client.get_users(user_id)
    except PeerIdInvalid:
        await Tm.edit("ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴜꜱᴇʀ ᴛᴇʀꜱᴇʙᴜᴛ.")
        return
    iso = 0
    gagal = 0
    prik = user.id
    prok = await get_seles()
    gua = client.me.id
    udah = await is_banned_user(gua, prik)
    async for dialog in client.get_dialogs():
        chat_type = dialog.chat.type
        if chat_type in [
            ChatType.GROUP,
            ChatType.SUPERGROUP,
            ChatType.CHANNEL,
        ]:
            chat = dialog.chat.id
            
            if prik in DEVS:
                return await Tm.edit(
                    "ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪꜱᴀ ɢʙᴀɴ ᴅɪᴀ ᴋᴀʀᴇɴᴀ ᴅɪᴀ ᴘᴇᴍʙᴜᴀᴛ ꜱᴀʏᴀ."
                )
            elif prik in prok:
                return await Tm.edit(
                    "ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪꜱᴀ ɢʙᴀɴ ᴅɪᴀ, ᴋᴀʀɴᴀ ᴅɪᴀ ᴀᴅᴀʟᴀʜ ᴀᴅᴍɪɴ ᴜꜱᴇʀʙᴏᴛ ᴀɴᴅᴀ."
                )
            elif udah:
                return await Tm.edit(
                    "ᴘᴇɴɢɢᴜɴᴀ ɪɴɪ ꜱᴜᴅᴀʜ ᴅɪ ɢʙᴀɴ."
                )
            elif prik not in prok and prik not in DEVS:
                try:
                    await add_banned_user(gua, prik)
                    await client.ban_chat_member(chat, prik)
                    iso = iso + 1
                    await asyncio.sleep(0.1)
                except BaseException:
                    gagal = gagal + 1
                    await asyncio.sleep(0.1)
    return await Tm.edit(
        f"""
<b>ɢʟᴏʙᴀʟ ʙᴀɴɴᴇᴅ</b>

<b>ʙᴇʀʜᴀꜱɪʟ ʙᴀɴɴᴇᴅ: {iso} Chat</b>
<b>ɢᴀɢᴀʟ ʙᴀɴɴᴇᴅ: {gagal} Chat</b>
<b>ᴜꜱᴇʀ: <a href='tg://user?id={prik}'>{user.first_name}</a></b>
"""
    )

async def cung_ban(client, message):
    user_id = await extract_user(message)
    if message.from_user.id != client.me.id:
        Tm = await eor(message, "<code>ᴍᴇᴍᴘʀᴏꜱᴇꜱ.....</code>")
    else:
        Tm = await eor(message, "<code>ᴍᴇᴍᴘʀᴏꜱᴇꜱ....</code>")
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        await Tm.edit(
            "<code>ungban</code> [ᴜꜱᴇʀ_ɪᴅ/ᴜꜱᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ]"
        )
    elif len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
    try:
        user = await client.get_users(user_id)
    except PeerIdInvalid:
        await Tm.edit("<b>ᴛɪᴅᴀᴋ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴜꜱᴇʀ ᴛᴇʀꜱᴇʙᴜᴛ.</b>")
        return
    iso = 0
    gagal = 0
    prik = user.id
    gua = client.me.id
    udah = await is_banned_user(gua, prik)
    async for dialog in client.get_dialogs():
        chat_type = dialog.chat.type
        if chat_type in [
            ChatType.GROUP,
            ChatType.SUPERGROUP,
            ChatType.CHANNEL,
        ]:
            chat = dialog.chat.id
            if prik in BANNED_USERS:
                BANNED_USERS.remove(prik) 
            try:
                await remove_banned_user(gua, prik)
                await client.unban_chat_member(chat, prik)
                iso = iso + 1
                await asyncio.sleep(0.1)
            except BaseException:
                gagal = gagal + 1
                await asyncio.sleep(0.1)

    return await Tm.edit(
        f"""
<b>ɢʟᴏʙᴀʟ ᴜɴʙᴀɴɴᴇᴅ</b>

<b>ʙᴇʀʜᴀꜱɪʟ ᴜɴʙᴀɴɴᴇᴅ: {iso} Chat</b>
<b>ɢᴀɢᴀʟ ᴜɴʙᴀɴɴᴇᴅ: {gagal} Chat</b>
<b>ᴜꜱᴇʀ: <a href='tg://user?id={prik}'>{user.first_name}</a></b>
"""
    )


async def gbanlist(client, message):
    gua = client.me.id
    total = await get_banned_count(gua)
    if total == 0:
        return await message.edit("<b>ʙᴇʟᴜᴍ ᴀᴅᴀ ᴘᴇɴɢɢᴜɴᴀ ʏᴀɴɢ ᴅɪɢʙᴀɴ.</b>")
    nyet = await message.edit("<b>ᴍᴇᴍᴘʀᴏꜱᴇꜱ...</b>")
    msg = "ᴛᴏᴛᴀʟ ɢʙᴀɴɴᴇᴅ:\n\n"
    tl = 0
    org = await get_banned_users(gua)
    for i in org:
        tl += 1
        try:
            user = await client.get_users(i)
            user = (
                user.first_name if not user.mention else user.mention
            )
            msg += f"{tl}• {user}\n"
        except Exception:
            msg += f"{tl}• {i}\n"
            continue
    if tl == 0:
        return await nyet.edit("<b>ʙᴇʟᴜᴍ ᴀᴅᴀ ᴘᴇɴɢɢᴜɴᴀ ʏᴀɴɢ ᴅɪɢʙᴀɴ.</b>")
    else:
        return await nyet.edit(msg)
