import asyncio
from pyppeteer import launch
from dotenv import load_dotenv
import os
import time

# Load variables from .env into the environment
load_dotenv()

ROOT_URL = os.getenv('ROOT')

async def test_api(endpoint = '/'):

    browser = await launch(ignoreHTTPSErrors=True)
    page = await browser.newPage()
    page.setDefaultNavigationTimeout(60000); # Increases the timeout limit to 60 seconds


    response = await page.goto(ROOT_URL)
    print(response)
    await browser.close()


if __name__ == "__main__":

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(test_api())
