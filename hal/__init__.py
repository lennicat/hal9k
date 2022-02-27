"""Python module containing main bot class."""

import disnake
from disnake.ext import commands


class HAL(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')