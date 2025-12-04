import os

def get_int_env(name, default=None):
    val = os.environ.get(name, "")
    if val is None or val == "":
        return default
    try:
        return int(val)
    except (ValueError, TypeError):
        return default

API_ID = get_int_env("API_ID", None)
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

OWNER_ID = get_int_env("OWNER_ID", None)

SUDO_USERS = []
_sudo = os.environ.get("SUDO_USERS", "").strip()
if _sudo:
    try:
        SUDO_USERS = list(map(int, _sudo.split()))
    except ValueError:
        SUDO_USERS = []

MONGO_URL = os.environ.get("MONGO_URL", "")
CHANNEL_ID = get_int_env("CHANNEL_ID", None)
PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "")
