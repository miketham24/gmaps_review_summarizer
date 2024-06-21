import google.generativeai as gai
import asyncio
from pyppeteer import launch

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')
print(api_key)

url = "https://www.google.com/maps/place/Phnom+Penh+Restaurant/@49.2784175,-123.1085087,15z/data=!3m1!4b1!4m6!3m5!1s0x5486716fe509c2b3:0x4e43d6ef30d0b5df!8m2!3d49.278418!4d-123.0982304!16s%2Fg%2F1td5lcxj?entry=ttu"

#headless = true as we don't want it to open a browser
browser = launch({"headless": True, "args":["--window-size=800,3200"]})

page = browser.newPage()
page.setViewport({"width": 800, "height": 3200})
page.goto(url)
