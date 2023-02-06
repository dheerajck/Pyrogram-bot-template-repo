from io import BytesIO
import subprocess

from pyrogram import Client, filters

from shared_config import shared_object


SUPER_ADMIN = shared_object.clients["super_admin"]


@Client.on_message(filters.user(SUPER_ADMIN) & filters.command("makemigration", prefixes="!"))
async def makemigration_handler(client, message):
    p = subprocess.Popen(
        ['python', 'manage.py', 'makemigrations', 'db'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    output, error = p.communicate()

    result = f"OUTPUT\n\n{output.decode()}\nERROR\n\n{error.decode()}".strip()

    temp_file = BytesIO()
    temp_file.name = "result.txt"
    temp_file.write(result.encode())

    await message.reply_document(temp_file)


@Client.on_message(filters.user(SUPER_ADMIN) & filters.command("migrate", prefixes="!"))
async def migrate_handler(client, message):
    p = subprocess.Popen(
        ['python', 'manage.py', 'migrate'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    output, error = p.communicate()

    result = f"OUTPUT\n\n{output.decode()}\nERROR\n\n{error.decode()}".strip()

    temp_file = BytesIO()
    temp_file.name = "result.txt"
    temp_file.write(result.encode())

    await message.reply_document(temp_file)
