from PyroUbot import *

__MODULE__ = "copy"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴏᴘʏ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}copy</code> [ʟɪɴᴋ_ᴋᴏɴᴛᴇɴ_ᴛᴇʟᴇɢʀᴀᴍ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴍʙɪʟ ᴘᴇsᴀɴ ᴅᴀɴ ᴘᴏsᴛɪɴɢᴀɴ ᴄʜᴀɴᴇʟ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇʟᴀʟᴜɪ ʟɪɴᴋ ᴍᴇʀᴇᴋᴀ
  """


@PY.UBOT("copy", sudo=False)
async def _(client, message):
    await nyolongnih(client, message)
