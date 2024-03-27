from PyroUbot import *

__MODULE__ = "translate"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛʀᴀɴsʟᴀᴛᴇ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}tr</code> [ʀᴇᴘʟʏ/ᴛᴇxᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴇʀᴊᴇᴍᴀʜᴋᴀɴ ᴛᴇxᴛ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}bahasa</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ʙᴀʜᴀsᴀ ᴛʀᴀɴsʟᴀᴛᴇ

  ɴᴏᴛᴇ : ᴀᴛᴜʀ ʙᴀʜᴀsᴀ ᴅᴀʜᴜʟᴜ ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ғɪᴛᴜʀ ɪɴɪ
"""




@PY.UBOT("tr|tl", sudo=False)
async def _(client, message):
    await tr_cmd(client, message)


@PY.UBOT("bahasa", sudo=False)
async def _(client, message):
    await set_lang_cmd(client, message)


@PY.INLINE("^ubah_bahasa")
@INLINE.QUERY
async def _(client, inline_query):
    await ubah_bahasa_inline(client, inline_query)


@PY.CALLBACK("^set_bahasa")
@INLINE.DATA
async def _(client, callback_query):
    await set_bahasa_callback(client, callback_query)
