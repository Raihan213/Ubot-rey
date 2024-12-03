import os

DEVS = [
    28382341,
]

API_ID = int(os.getenv("API_ID", "28382341"))

API_HASH = os.getenv("API_HASH", "abfba018c7576a5c0f4445732c1d7603")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7059273304:AAFtNYNQXM_3fSIGHz7nQ8Uer607CjCFpEg")

OWNER_ID = int(os.getenv("OWNER_ID", "28382341"))

USER_ID = list(map(int,os.getenv("USER_ID", "28382341 28382341",).split(),))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-4673039767"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-4673039767 -4673039767").split()))

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
