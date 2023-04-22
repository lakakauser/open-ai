from dotenv import load_dotenv
import os
from typing import List

load_dotenv()

DISCORD_BOT_TOKEN = os.environ["DISCORD_BOT_TOKEN"]
DISCORD_CLIENT_ID = os.environ["DISCORD_CLIENT_ID"]

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
OPENAI_API_URL = os.environ['OPENAI_API_URL']
OPENAI_MODEL = os.environ['OPENAI_MODEL']

SYSTEM_MESSAGE = os.environ["SYSTEM_MESSAGE"]
KNOWLEDGE_CUTOFF = os.environ["KNOWLEDGE_CUTOFF"]

ALLOWED_SERVER_IDS: List[int] = []
server_ids = os.environ["ALLOWED_SERVER_IDS"].split(",")
for s in server_ids:
    ALLOWED_SERVER_IDS.append(int(s))

# Send Messages
# Create Public Threads
# Send Messages in Threads
# Manage Messages
# Manage Threads
# Read Message History
# Use Slash Command
BOT_INVITE_URL = f"https://discord.com\
/api/oauth2/authorize\
?client_id={DISCORD_CLIENT_ID}\
&permissions=328565073920\
&scope=bot"

SECONDS_DELAY_RECEIVING_MSG = (
    3  # give a delay for the bot to respond so it can catch multiple messages
)
MAX_THREAD_MESSAGES = 200
ACTIVATE_THREAD_PREFX = "💬✅"
INACTIVATE_THREAD_PREFIX = "💬❌"
MAX_CHARS_PER_REPLY_MSG = (
    2000  # discord has a 2k limit
)
