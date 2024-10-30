import os
import sys
import asyncio
import requests
from Bot import LOG, soheru
from Bot.database.client import startup

async def main():
    # Check the status of the URL
    x = requests.get('http://soheru.in', allow_redirects=True).status_code
    if x != 200:
        sys.exit()
    
    # Clean up specific files in the current directory
    for x in os.listdir("."):
        if x.endswith(".mp4") or x.endswith(".png"):
            os.remove(x)
    LOG.info('Cleaned Terminal')

    # Start the bot
    await soheru.start()
    print('[×] - INFO - STARTING THE BOT')
    print('[×] - INFO - EVERYTHING LOOKING GOOD')

    # Database startup
    startup()  # Call startup without await if it’s synchronous
    print('[×] - INFO - BOT STARTED')

    # Keep the bot running (no explicit call to run_forever)
    await asyncio.Event().wait()  # This keeps the main function running indefinitely

if __name__ == "__main__":
    asyncio.run(main())