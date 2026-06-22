from telethon import TelegramClient
from telethon.sessions import StringSession

from config import *

client = TelegramClient(
    StringSession(STRING_SESSION),
    API_ID,
    API_HASH
)
