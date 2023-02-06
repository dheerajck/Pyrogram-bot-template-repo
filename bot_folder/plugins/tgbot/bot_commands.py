from pyrogram import Client, filters


@Client.on_message(filters.text & filters.private)
async def echo(client, message):
    await message.reply(message.text)
