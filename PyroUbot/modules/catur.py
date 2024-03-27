from PyroUbot import *
__MODULE__ = "game"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢᴀᴍᴇ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}catur</code></code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍᴀɴɢɢɪʟ ɢᴀᴍᴇ ᴄᴀᴛᴜʀ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}game</code></code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍᴜɴᴄᴜʟᴋᴀɴ ɢᴀᴍᴇ ʀᴀɴᴅᴏᴍ.
  <b>• ɴᴏᴛᴇ : ᴊᴜᴍʟᴀʜ ᴍᴇɴᴜ 𝟻𝟶+ ɢᴀᴍᴇ </b>
"""



@PY.UBOT("catur", sudo=True)
async def _(client, message):
    await catur_cmd(client, message)
    

@PY.UBOT("game", sudo=True)
async def _(client, message):
    await game_cmd(client, message)