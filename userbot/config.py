import os

DEVS = [
    400626816,
]

API_ID = int(os.getenv("API_ID", "28610365"))

API_HASH = os.getenv("API_HASH", "8219cdcb17704a457a2423322410baa4")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6863127605:AAGLsnL0cTl2JjobqWQ9NZGj-fV-Ia-52UQ")

OWNER_ID = int(os.getenv("OWNER_ID", "400626816"))

USER_ID = list(map(int,os.getenv("USER_ID", "400626816 400626816",).split(),))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002082932015"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002082932015 -1002082932015").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "50"))

RMBG_API = os.getenv("RMBG_API", "abcdefg")

COMMAND = os.getenv("COMMAND", ".")
PREFIX = COMMAND.split()

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "reyganteng",
).split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://reybot:reybot@cluster0.hwt9afk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)
