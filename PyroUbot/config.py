import os

DEVS = [
    800789318
]

API_ID = int(os.getenv("API_ID", "xxxx"))

API_HASH = os.getenv("API_HASH", "xxxx")

BOT_TOKEN = os.getenv("BOT_TOKEN", "728827:xxxx")

OWNER_ID = int(os.getenv("OWNER_ID", "800789318"))

USER_ID = list(map(int,os.getenv("USER_ID", "800789318 800789318",).split(),))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-100xxxxxx"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-100xxxxx -100xxxxxx").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "50"))

RMBG_API = os.getenv("RMBG_API", "")

COMMAND = os.getenv("COMMAND", ".")
PREFIX = COMMAND.split()

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "",
).split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "",
)
