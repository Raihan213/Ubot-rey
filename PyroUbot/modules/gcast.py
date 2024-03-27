from PyroUbot import *

__MODULE__ = "gcast"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢᴄᴀsᴛ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}ucast</code> [ᴛᴇxᴛ/ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ/ᴍᴇᴅɪᴀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ sᴇᴍᴜᴀ ᴜsᴇʀ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}gcast</code> [ᴛᴇxᴛ/ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ/ᴍᴇᴅɪᴀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ sᴇᴍᴜᴀ ɢʀᴏᴜᴘ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}spamg</code> [ᴊᴜᴍʟᴀʜ_ᴘᴇsᴀɴ - ʀᴇᴘ_ᴘᴇsᴀɴ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ sᴘᴀᴍ ᴘᴇsᴀɴ ɢᴄᴀsᴛ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}send</code> [ᴜsᴇʀɪᴅ/ᴜsᴇʀɴᴀᴍᴇ - ᴛᴇxᴛ/ʀᴇᴘʟʏ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ ᴜsᴇʀ/ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟd

  <b>ɢᴄᴀsᴛ: ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ʙᴜᴛᴛᴏɴ, ɢᴜɴᴀᴋᴀɴ ꜰᴏʀᴍᴀᴛ:</b>
  <code>ᴛᴇxᴛ ~> ʙᴜᴛᴛᴏɴ_ᴛᴇxᴛ:ʙᴜᴛᴛᴏɴ_ᴜʀʟ</code>
"""


@PY.UBOT("gcast", sudo=True)
async def _(client, message):
    await broadcast_group_cmd(client, message)


@PY.UBOT("ucast", sudo=True)
async def _(client, message):
    await broadcast_users_cmd(client, message)


@PY.UBOT("send", sudo=True)
async def _(client, message):
    await send_msg_cmd(client, message)


@PY.INLINE("^get_send")
@INLINE.QUERY
async def _(client, inline_query):
    await send_inline(client, inline_query)


@PY.INLINE("^gcast_button")
@INLINE.QUERY
async def _(client, inline_query):
    await gcast_inline(client, inline_query)

