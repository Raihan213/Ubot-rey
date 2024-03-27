from PyroUbot import *


__MODULE__ = "audio"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛᴇxᴛ ᴛᴏ ᴀᴜᴅɪᴏ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}tts</code> [ʀᴇᴘʟʏ/ᴛᴇxᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴛᴇᴄᴛ ᴍᴇɴᴊᴀᴅɪ ᴍᴇɴᴊᴀᴅɪ ᴘᴇsᴀɴ sᴜᴀʀᴀ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}bahasa</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ʙᴀʜᴀsᴀ ᴛᴇxᴛ ᴛᴏ ᴀᴜᴅɪᴏ

  ɴᴏᴛᴇ : ᴀᴛᴜʀ ʙᴀʜᴀsᴀ ᴅᴀᴜʟᴜ ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ғɪᴛᴜʀ ɪɴɪ
"""



@PY.UBOT("tts", sudo=False)
async def _(client, message):
    await tts_cmd(client, message)


