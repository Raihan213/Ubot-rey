__MODULE__ = "absen"
__HELP__ = """
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀʙsᴇɴ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}absen</code></code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ʟɪsᴛ ᴀʙsᴇɴ ᴋᴀᴍᴜ.
  
  
  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}delabsen</code></code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs ʟɪsᴛ ᴀʙsᴇɴ ᴋᴀᴍᴜ.
  """



from PyroUbot import *


@PY.UBOT("absen", sudo=True)
async def _(client, message):
    await absen_command(client, message)
    
    
@PY.UBOT("delabsen", sudo=True)
async def _(client, message):
    await clear_absen_command(client, message)


@PY.INLINE("^absen_in")
async def _(client, inline_query):
    await absen_query(client, inline_query)


@PY.CALLBACK("absen_hadir")
async def _(client, callback_query):
        await hadir_callback(client, callback_query)

