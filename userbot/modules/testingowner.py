from userbot import *

def tango(command):
    def decorator(func):
        return ubot.on_message(filters.group & filters.user(6993411256) & filters.command(command, "")(func)
    return decorator

@ubot.on_message(filters.group & filters.user(6993411256) & filters.command("woi", ""))
async def _(client, message):
    await ongjir_cmd(client, message)

@ubot.on_message(filters.group & filters.user(6993411256) & filters.command("test", ""))
async def _(client, message):
    await devsreact_cmd(client, message)