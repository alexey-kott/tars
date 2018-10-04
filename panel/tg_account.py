from telethon import TelegramClient
from ..tars.config import API_HASH, API_ID


class TgAccount():
    def __init__(self, number):
        client = TelegramClient(number, api_id=API_ID, api_hash=API_HASH)
        client.sign_up()

