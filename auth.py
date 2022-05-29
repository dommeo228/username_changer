import asyncio
from config import API_ID, API_HASH
from pyrogram import Client


async def auth():
    print('Started.')  # Log the start

    client = Client("username_changer", API_ID, API_HASH, workdir='sessions')  # Create a new client for auth
    await client.start()  # Connect to Telegram

    if not client.is_connected:  # If the client isn't connected
        return print('Authorization failed.')  # Log the failure

    print('Authorized successfully.')  # Log the successful authorization

    await client.stop()  # Disconnect from Telegram


if __name__ == '__main__':  # If this file is run directly
    asyncio.run(auth())
