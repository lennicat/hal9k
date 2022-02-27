import requests
import json
from disnake.ext import tasks, commands


class HalTwitch(commands.Cog):
    def __init__(self, bot, config) -> None:
        self.config = config
        self.bot = bot
        self.check_twitch_live.start()
        self.live = False

    async def check_stream(self, streamer):

        body = {
            'client_id': self.config.get('CLIENT_ID'),
            'client_secret': self.config.get('CLIENT_SECRET'),
            "grant_type": 'client_credentials'
        }

        r = requests.post('https://id.twitch.tv/oauth2/token', body)
                
        #data output
        keys = r.json();
        
        headers = {
            'Client-ID': self.config.get('CLIENT_ID'),
            'Authorization': 'Bearer ' + keys['access_token']
        }

        streamer_name = streamer

        stream = requests.get('https://api.twitch.tv/helix/streams?user_login=' + streamer_name, headers=headers)

        stream_data = json.loads(stream.text)

        return stream_data


    @tasks.loop(minutes=1)
    async def check_twitch_live(self):
        stream = await self.check_stream('nagifur')

        if self.live == True and stream.get('data') != []:
            pass
        elif self.live == True and stream.get('data') == []:
            self.live = False
        elif self.live == False and stream.get('data') != []:
            self.live = True
    
    @check_twitch_live.before_loop
    async def before_live(self):
        await self.bot.wait_until_ready()