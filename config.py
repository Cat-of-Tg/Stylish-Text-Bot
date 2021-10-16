import os

class Config(object):

      BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
      API_ID = int(os.environ.get("API_ID", 12345))
      API_HASH = os.environ.get("API_HASH")
      OWNER_ID = int(os.environ.get("OWNER_ID"))
    AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS", "") else []
    if OWNER_ID not in AUTH_USERS:
        AUTH_USERS.append(OWNER_ID)

