import os


class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "2033518274:AAEui4qfA_Thp8IvdaPj6Z5IxcmgEalqks0")

    APP_ID = int(os.environ.get("APP_ID", 7122114))

    API_HASH = os.environ.get("API_HASH", "3ff382cb976bdf8aead9359f2c352ac1")

