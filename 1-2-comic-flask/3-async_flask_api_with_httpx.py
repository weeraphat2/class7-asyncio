# https://flask.palletsprojects.com/en/2.3.x/
# https://www.python-httpx.org/async/
# https://flask.palletsprojects.com/en/2.3.x/quickstart/#rendering-templates

import asyncio
import time
from random import randint
import httpx
from flask import Flask, render_template

app = Flask(__name__)

# function converted to coroutine
async def get_xkcd_image(session): # dont wait for the response of API
    

# function converted to coroutine
async def get_multiple_images(number): 
    async with 

@app.get('/comic')
async def hello(): 
    

if __name__ == '__main__':
    app.run(debug=True, port=5555)