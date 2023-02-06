from pyrogram import Client, filters


@Client.on_message(
    filters.me & filters.private & filters.command(["test1", "test2"], ["/", "!"]),
)
async def get_me(client, message):
    me = await client.get_me()
    await message.reply(me)
