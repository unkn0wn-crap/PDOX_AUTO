import logging 
from os import environ, path, remove
from sys import exit
from pyrogram import Client 
from pyromod import listen

if path.exists('log.txt'):
    remove('log.txt')
    
logging.basicConfig(filename='log.txt', level=logging.INFO)
LOG = logging.getLogger("AutoPahe")
LOG.setLevel(level=logging.INFO)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',}

API_ID = int(environ.get('API_ID', 6435225)) #API ID
API_HASH = environ.get('API_HASH', '4e984ea35f854762dcde906dce426c2d') #API HASH
BOT_TOKEN = environ.get('BOT_TOKEN', '5527818445:AAE7TLprBfyUuQvYZsaOesQ0F-9C2sl2I80') #BOT TOKEN
DATABASE_URL = environ.get('DATABASE_URL', 'mongodb+srv://arnavgupta0078:arnav@cluster3301.ojyvd.mongodb.net/retryWrites=true&w=majority') #MONGO DB
OWNER_ID = "6259443940" #OWNER ID
MAIN_CHANNEL = int(environ.get('MAIN_CHANNEL', "-1002231792362"))#YOUR MAIN CHANNEL ID
ARCHIVE_CHANNEL = int(environ.get('ARCHIVE_CHANNEL', "-1002231792362"))#YOUR ARCHIVE CHANNEL
MESSAGE_ID = int(environ.get('MESSAGE_ID', "42")) #SUB CHANNEL STATUS ID

soheru = Client('SoheruBots', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
