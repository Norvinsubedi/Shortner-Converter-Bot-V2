# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "1532484"))
API_HASH = os.environ.get("API_HASH", "21ba7c10c1532484c2f69fdf07a99284")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6042874961:AAFWI3CAh1i6zz355FlKrWCbf_CsNsuI-AE")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5182822827")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "NORVIN")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Norvin:<password>@cluster0.miwdkej.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5182822827")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001859138110/2")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "@Trrry") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
