from .. import *


@PY.UBOT("ping", sudo=True)
@ubot.on_message(filters.user(USER_ID) & filters.command("ping", "1") & ~filters.me)
async def _(client, message):
    await ping_cmd(client, message)


@PY.BOT("start")
async def _(client, message):
    await start_cmd(client, message)
