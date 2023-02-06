import asyncio
import os

import uvloop
from dotenv import load_dotenv

from pyrogram import Client, compose

from shared_config import shared_object
from simple_logging.standard_logging_loguru_interface_class import set_logger


# load env
load_dotenv("bot_folder/.env")

# set logging
set_logger()

# set uvloop
uvloop.install()


async def main():
    api_id = os.getenv('API_ID')
    api_hash = os.getenv('API_HASH')
    bot_token = os.getenv('BOT_TOKEN')
    shared_object.clients["super_admin"] = os.getenv('SUPER_ADMIN')

    plugins_tgbot = dict(
        root="bot_folder.plugins.tgbot/",
    )
    plugins_userbot = dict(
        root="bot_folder.plugins.userbot/",
    )

    tgbot = Client("tgbot", api_id=api_id, api_hash=api_hash, bot_token=bot_token, plugins=plugins_tgbot)
    userbot = Client("userbot", api_id=api_id, api_hash=api_hash, plugins=plugins_userbot)

    shared_object.clients["tgbot"] = tgbot
    shared_object.clients["userbot"] = userbot

    apps = [tgbot, userbot]
    await compose(apps)


def uvloop_test():
    loop = asyncio.new_event_loop()
    print(isinstance(loop, uvloop.Loop))
    assert isinstance(loop, uvloop.Loop)


if __name__ == "__main__":
    asyncio.run(main())
