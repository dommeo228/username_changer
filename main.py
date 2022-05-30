import asyncio
import random
import string

import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from loguru import logger
from pyrogram import Client, idle
from pyrogram.errors.exceptions.bad_request_400 import UsernameOccupied

from config import API_ID, API_HASH


async def change_username():
    app: Client  # Type hinting
    async with Client("username_changer", API_ID, API_HASH, workdir='sessions') as app:  # Create a new client
        for i in range(5):  # 5 tries
            # Generate random username (5 - 32 characters) from a-z, A-Z, 0-9
            random_username = "".join(random.choices(string.ascii_letters + string.digits,
                                                     k=random.randint(5, 32)))

            try:
                await app.set_username(random_username)  # Try to change username

                logger.info(f'Username changed to: @{random_username}')  # Log the username change

                break  # If the username is set successfully, break the loop
            except UsernameOccupied:  # If username is occupied, try again
                pass  # Do nothing
            except Exception as e:  # If any other error, log it
                logger.error(e)  # Log the error

            await asyncio.sleep(5)  # Cooldown time (in seconds)


async def main():
    logger.info('Started.')  # Log the start

    scheduler = AsyncIOScheduler(timezone=pytz.timezone('UTC'))  # Create a new scheduler
    scheduler.add_job(change_username, "cron", hour='0', minute='0', second='0')  # Add a job to change username at midnight
    scheduler.start()  # Start the scheduler

    await idle()  # Idle the client


if __name__ == '__main__':  # If this file is run directly, run the main function
    asyncio.run(main())  # Run the main function
