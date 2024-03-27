from PyroUbot import *

__MODULE__ = "create"
__HELP__ = """
 <b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄʀᴇᴀᴛᴇ 』</b>

<b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}buat</code> gc
<b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ɢʀᴜᴘ ᴛᴇʟᴇɢʀᴀᴍ.

<b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}buat</code> ch
<b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴇʟᴇɢʀᴀᴍ.
"""


@PY.UBOT("buat", sudo=True)
async def _(client, message):
    await create_grup(client, message)
