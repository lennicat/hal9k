from dotenv import dotenv_values
from disnake.ext import commands
import disnake
from hal import HAL
from hal.db import Database
from hal.slash import BasicCommands
from hal.twitch import HalTwitch

intents = disnake.Intents.default()
intents.members = True

db = Database()

db.init

config = dotenv_values(".env")

bot = HAL(intents=intents, 
    command_prefix=commands.when_mentioned,
    test_guilds=[934620780216610816],
    sync_commands_debug=True
)

bot.add_cog(BasicCommands(bot))
bot.add_cog(HalTwitch(bot, config))
bot.run(token=config.get('TOKEN'))