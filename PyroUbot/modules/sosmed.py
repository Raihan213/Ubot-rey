from PyroUbot import *

__MODULE__ = "sosmed"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴏsᴍᴇᴅ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}sosmed</code> [ʟɪɴᴋ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ᴍᴇᴅɪᴀ ᴅᴀʀɪ ꜰᴀᴄᴇʙᴏᴏᴋ/ᴛɪᴋᴛᴏᴋ/ɪɴsᴛᴀɢʀᴀᴍ/ᴛᴡɪᴛᴛᴇʀ/ʏᴏᴜᴛᴜʙᴇ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}song</code> [sᴏɴɢ ᴛɪᴛʟᴇ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>  ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ᴍᴜsɪᴄ ʏᴀɴɢ ᴅɪɪɴɢɪɴᴋᴀɴ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}vsong</code> [sᴏɴɢ ᴛɪᴛʟᴇ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ʏᴀɴɢ ᴅɪɪɴɢɪɴᴋᴀɴ
"""


@PY.UBOT("sosmed", sudo=False)
async def _(client, message):
    await sosmed_cmd(client, message)


@PY.UBOT("vsong", sudo=False)
async def _(client, message):
    await vsong_cmd(client, message)


@PY.UBOT("song", sudo=False)
async def _(client, message):
    await song_cmd(client, message)
