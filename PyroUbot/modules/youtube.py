from PyroUbot import *

__MODULE__ = "youtube"
__HELP__ = f"""
<b>『 Bᴀɴᴛᴜᴀɴ Uɴᴛᴜᴋ Yᴏᴜᴛᴜʙᴇ 』</b>

• Pᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}sᴏɴɢ</ᴄᴏᴅᴇ> [sᴏɴɢ ᴛɪᴛʟᴇ]
• Pᴇɴᴊᴇʟᴀsᴀɴ: Uɴᴛᴜᴋ ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ᴍᴜsɪᴄ ʏᴀɴɢ ᴅɪɪɴɢɪɴᴋᴀɴ.

• Pᴇʀɪɴᴛᴀʜ: <ᴄᴏᴅᴇ>{0}ᴠsᴏɴɢ</ᴄᴏᴅᴇ> [ᴠɪᴅᴇᴏ ᴛɪᴛʟᴇ]
• Pᴇɴᴊᴇʟᴀsᴀɴ: Uɴᴛᴜᴋ ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ʏᴀɴɢ ᴅɪɪɴɢɪɴᴋᴀɴ.
"""


@PY.UBOT("vsong", sudo=True)
async def _(client, message):
    await vsong_cmd(client, message)


@PY.UBOT("song", sudo=True)
async def _(client, message):
    await song_cmd(client, message)
