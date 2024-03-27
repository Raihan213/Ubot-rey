from PyroUbot import *

__MODULE__ = "logo"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʟᴏɢᴏ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}logo</code> [ᴛᴇxᴛ/ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ ᴛᴇxᴛ ᴍᴇɴᴊᴀᴅɪ ʟᴏɢᴏ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}blogo</code> [ᴛᴇxᴛ/ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b>ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ ʙᴀᴄᴋɢʀᴏᴜɴᴅ ᴊᴀᴅɪ ʜɪᴛᴀᴍ  
"""


@PY.UBOT("blogo|logo", sudo=True)
async def _(client, message):
    await logo_cmd(client, message)
