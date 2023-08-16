import asyncio
import time
from random import randint
import httpx
from flask import Flask, render_template

app = Flask(__name__)

async def get_xkcd_image(session, comicid):
    random = randint(0, 1000)
    result = await session.get(f'https://xkcd.com/{comicid}/info.0.json') 
    return result.json()['img']

async def get_multiple_images(session, number):
    async with httpx.AsyncClient() as session:
        tasks = [get_xkcd_image(session) for _ in range(number)]
        result = await asyncio.gather(*tasks, return_exceptions=True)
    return result

@app.get('/comic')
async def hello():
        start = time.perf_counter()
        urls = await get_multiple_images(10)
        end = time.perf_counter()
        return await render_template('index.html', end=end, start=start, urls=urls)

if __name__ == '__main__':
    app.run(debug=True, port=5555)
