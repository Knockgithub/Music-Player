from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN", "6024489085:AAEajd4l5OTAr6LbscEWvpnS1Z6-oNAzhfo")
BOT_USERNAME = getenv("BOT_USERNAME", "@musicahere_bot")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH", "06766128d68d9c1a0d683ecfbb91de2f")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
