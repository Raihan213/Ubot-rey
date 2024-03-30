import os

DEVS = [
    6421929620
]

API_ID = int(os.getenv("API_ID", "17250424"))

API_HASH = os.getenv("API_HASH", "753bc98074d420ef57ddf7eb1513162b")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6600120685:AAGFFxa73wHq_S8T1h8o6hrbGeDCsFTKGXw")

OWNER_ID = int(os.getenv("OWNER_ID", "6421929620"))

USER_ID = list(map(int,os.getenv("USER_ID", "6421929620 5316973462",).split(),))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002047274922"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002047274922 -1002047274922").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "50"))

RMBG_API = os.getenv("RMBG_API", "WEnHwQnst3E2HzjGgwmy4UpB")

COMMAND = os.getenv("COMMAND", ".")
PREFIX = COMMAND.split()

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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",
).split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://reybot:reybot@cluster0.hwt9afk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)
