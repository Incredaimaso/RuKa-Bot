


import os
import json


def get_user_list(key):
    with open("users.json", "r") as json_file:
        return json.load(json_file)[key]


class Config:
    # Basic Bot Configuration
    TOKEN = os.getenv("TOKEN", "7942335745:AAGFVnS-sEK-y1ZSL1Bsk8CtqTH4Pp7mb_U")
    API_ID = int(os.getenv("API_ID", 22403100))
    API_HASH = os.getenv("API_HASH", "ccbc3f662735abfa604ef6309ba76e67")
    BOT_USERNAME = os.getenv("BOT_USERNAME", "KatsuOneBot")

    # Database Configuration
    DATABASE_URL = os.getenv("DATABASE_URL", "https://blue-api.vercel.app/database?client=ishikki@xyz242.gramdb")

    # Logging and Monitoring
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1002432275758"))  # Example: -1001234567890 (Private Channel ID)
    ERROR_LOG_CHANNEL = int(os.getenv("ERROR_LOG_CHANNEL", -1002432275758))
   
    # Access Control
    DEV_USERS = list(map(int, os.getenv("DEV_USERS", "7950514048").split(',')))
    OWNER_ID = int(os.getenv("OWNER_ID", 7950514048))

    # Optional Extras
    SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "AnimeFantasyG")  # Without '@'
    SUPPORT_CHAT_ID = int(os.getenv("SUPPORT_CHAT_ID", -1002023828951))
    
    # Additional API integrations
    MEOWCORE_TOKEN = os.getenv("MEOWCORE_TOKEN", "69696969-MeowMeow")
