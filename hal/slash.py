from disnake.ext import commands
from disnake import ApplicationCommandInteraction


class BasicCommands(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.slash_command(
        name="hello",
        description="Just a test command for now"
    )
    async def hello(inter: ApplicationCommandInteraction):
        await inter.response.send_message(f'Hello, {inter.user.display_name}.')
