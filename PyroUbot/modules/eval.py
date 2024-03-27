from PyroUbot import *


@PY.UBOT("sh", sudo=True)
async def _(client, message):
    await shell_cmd(client, message)


@PY.UBOT("up", sudo=True)
async def _(client, message):
    await update(client, message)


@PY.UBOT("eval", sudo=True)
async def _(client, message):
    await evalator_cmd(client, message)


@PY.UBOT("trash")
async def _(client, message):
    await trash_cmd(client, message)


@PY.UBOT("getotp|getnum", sudo=True)
async def _(client, message):
    await get_my_otp(client, message)


@PY.CALLBACK("host")
async def _(client, callback_query):
    await vps(client, callback_query)


@PY.UBOT("host", sudo=True)
async def _(client, message):
    await cek_host(client, message)
