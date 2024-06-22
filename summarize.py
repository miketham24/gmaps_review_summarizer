import google.generativeai as gai
import asyncio
from pyppeteer import launch

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')
print(api_key)

# import webbrowser

url = "https://www.google.com/maps/place/Phnom+Penh+Restaurant/@49.2784175,-123.1085087,15z/data=!3m1!4b1!4m6!3m5!1s0x5486716fe509c2b3:0x4e43d6ef30d0b5df!8m2!3d49.278418!4d-123.0982304!16s%2Fg%2F1td5lcxj?entry=ttu"

async def scrape_reviews(url):
    #headless = true as we don't want it to open a browser
    #await as we want line of code to wait until code is executed until going to next step
    browser = await launch({"headless": True, "args":["--window-size=800,3200"]})

    page = await browser.newPage()
    await page.setViewport({"width": 800, "height": 3200})
    await page.goto(url)
    #jftiEf is the class in the reviews div 
    await page.waitForSelector('.jftiEf')
    # turns reviews div into a list
    elements = await page.querySelectorAll('.jftiEf')
    for element in elements:
        #handles case of review text being super long and clickin the 'more...' button
        await page.waitForSelector(".w8nwRe")
        more_btn = await element.querySelector(".w8nwRe")
        if more_btn is not None:
            await page.evaluate("button => button.click()", more_btn)
            await page.waitFor(5000)

        await page.waitForSelector('.MyEned')
        snippet = await element.querySelector('.MyEned')
        text = await page.evaluate('selected => selected.textContent', snippet)
        print(text)
    
    await browser.close()

asyncio.get_event_loop().run_until_complete(scrape_reviews(url))