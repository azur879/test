import aiohttp
import asyncio
from flask import Flask

app = Flask('discord')

@app.route('/')
def hello():
    return "Congratulations, it's a web app!"

if __name__ == '__main__':
    app.run(debug=True)

#ws = await session.ws_connect('http://warm-octopus-1337.loca.lt')

 #   async with aiohttp.ClientSession() as session:
 #       async with session.get('http://warm-octopus-1337.loca.lt') as response:

 #           print("Status:", response.status)
 #           print("Content-type:", response.headers['content-type'])

 #           html = await response.text()
 #           print("Body:", html[:15], "...")

#loop = asyncio.get_event_loop()
#loop.run_until_complete(main())p().run_until_complete(send_message())