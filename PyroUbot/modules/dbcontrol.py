from PyroUbot import *


@PY.BOT("prem")
@PY.UBOT("prem", sudo=False)
async def _(client, message):
    await prem_user(client, message)


@PY.BOT("user")
@PY.UBOT("user")
async def _(client, message):
    await jumlah_user(client, message)
    

@PY.BOT("unprem")
@PY.UBOT("unprem", sudo=False)
async def _(client, message):
    await unprem_user(client, message)


@PY.BOT("getprem")
@PY.UBOT("getprem", sudo=False)
async def _(cliebt, message):
    await get_prem_user(client, message)


@PY.BOT("seles")
@PY.UBOT("seles", sudo=False)
async def _(client, message):
    await seles_user(client, message)


@PY.BOT("unseles")
@PY.UBOT("unseles", sudo=False)
async def _(client, message):
    await unseles_user(client, message)


@PY.BOT("getseles")
@PY.UBOT("getseles", sudo=False)
async def _(client, message):
    await get_seles_user(client, message)


@PY.BOT("time")
@PY.UBOT("time", sudo=False)
async def _(client, message):
    await expired_add(client, message)


@PY.BOT("cek")
@PY.UBOT("cek", sudo=False)
async def _(client, message):
    await expired_cek(client, message)


@PY.BOT("untime")
@PY.UBOT("untime", sudo=False)
async def _(client, message):
    await un_expired(client, message)


@PY.CALLBACK("restart")
async def _(client, callback_query):
    await cb_restart(client, callback_query)


@PY.CALLBACK("gitpull")
async def _(client, callback_query):
    await cb_gitpull(client, callback_query)


@PY.BOT("bcast")
async def _(client, message):
    await bcast_cmd(client, message)