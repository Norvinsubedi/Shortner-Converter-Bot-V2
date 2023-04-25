# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "24541503"))
API_HASH = os.environ.get("API_HASH", "c75e70947a88a4b91c30b530ea36645d")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6262059299:AAF2M9_wMwam89IDhl62QaFM3QWsuZUu2XI")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("6181653250")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "NORVIN")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://subamsubedi:<Norvin44#>@cluster1.khe2ksw.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "t6181653250")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(6181653250)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "6181653250")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "@needtojoinchannel") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
