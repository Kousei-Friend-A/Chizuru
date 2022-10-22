import os
import logging
import time
import sys
from pyrogram import Client

logging.basicConfig(level=logging.INFO)

LOGS = logging.getLogger("AnimeBot")
LOGS.setLevel(level=logging.INFO)

#-------------------------------LIST----------------------------------------

#-------------------------------VARS-----------------------------------------
BOT_TOKEN = "5698053647:AAGgW2ZOloLQEBYqTaL00TCA0VW-FQpytcg"
API_ID = 17945796
API_HASH = "4a05481a5da2d66f801acffc4ca5ee4b"
MONGO_DB = "mongodb+srv://autoanimebitch:bitch@cluster0.qs6r6ux.mongodb.net/?retryWrites=true&w=majority"
OWNER = 5152809878
#-------------------------------DEFAULT---------------------------------------
TRIGGERS = os.environ.get("TRIGGERS", "/").split()
UTRIGGERS = os.environ.get("TRIGGERS", ".").split()
plugins = dict(root="Chizuru/plugin")
#------------------------------CONNECTION------------------------------------
if BOT_TOKEN is not None:
    try:
        pbot = Client("Chizuru", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=plugins)
        LOGS.info("❤️ Bot Connected")
    except:
        LOGS.info('😞 Error While Connecting To Bot')    
        sys.exit()            
