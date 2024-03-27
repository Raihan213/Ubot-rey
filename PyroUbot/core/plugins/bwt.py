import os
from PyroUbot import *

async def create_grup(client, message):
    if len(message.command) < 3:
        return await message.reply(
            f"sɪʟᴀʜᴋᴀɴ ᴋᴇᴛɪᴋ {message.command} ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ʙᴀɴᴛᴜᴀɴ ᴅᴀʀɪ ᴍᴏᴅᴜʟ ɪɴɪ."
        )
    group_type = message.command[1]
    split = message.command[2:]
    group_name = " ".join(split)
    xd = await message.reply("<code>sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs...</code>")
    desc = "Welcome To My " + ("Group" if group_type == "gc" else "Channel")
    if group_type == "gc":  # for supergroup
        _id = await client.create_supergroup(group_name, desc)
        link = await client.get_chat(_id.id)
        await xd.edit(
            f"<b>ʙᴇʀʜᴀsɪʟ ᴍᴇᴍʙᴜᴀᴛ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴜᴘ : [{group_name}]({link.invite_link})</b>",
            disable_web_page_preview=True,
        )
    elif group_type == "ch":  # for channel
        _id = await client.create_channel(group_name, desc)
        link = await client.get_chat(_id.id)
        await xd.edit(
            f"<b>ʙᴇʀʜᴀsɪʟ ᴍᴇᴍʙᴜᴀᴛ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ : [{group_name}]({link.invite_link})</b>",
            disable_web_page_preview=True,
        )
