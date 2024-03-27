from PyroUbot import *

__MODULE__ = "staff"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴛᴀғғ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}staff</code> [ɪᴘ ᴀᴅᴅʀᴇꜱ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ɪɴꜰᴏʀᴍᴀsɪ sᴇʟᴜʀᴜʜ sᴛᴀғғ ɢʀᴜᴘ
  """


@PY.UBOT("staff", sudo=False)
async def _(client, message):
    await staff_cmd(client, message)