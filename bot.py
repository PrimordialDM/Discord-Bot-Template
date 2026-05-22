import logging

import discord
from discord.ext import commands

from utils.config import Settings, load_settings

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("PrimordialBot")


class PrimordialBot(commands.Bot):
    def __init__(self, settings: Settings):
        intents = discord.Intents.default()
        intents.guilds = True
        intents.messages = True
        intents.message_content = True
        intents.members = True

        super().__init__(
            command_prefix=settings.prefix,
            intents=intents,
            help_command=None,
        )
        self.settings = settings

    async def setup_hook(self) -> None:
        for extension in ("cogs.general", "cogs.admin"):
            try:
                await self.load_extension(extension)
                logger.info("Loaded extension: %s", extension)
            except Exception:
                logger.exception("Failed to load extension: %s", extension)

        if self.settings.test_guild_id:
            guild = discord.Object(id=self.settings.test_guild_id)
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)
            logger.info("Synced commands to test guild %s", self.settings.test_guild_id)
        else:
            await self.tree.sync()
            logger.info("Synced commands globally")

    async def on_ready(self) -> None:
        if self.user is None:
            return
        logger.info("Logged in as %s (%s)", self.user, self.user.id)
        await self.change_presence(activity=discord.Game("PrimordialDM master template"))


if __name__ == "__main__":
    settings = load_settings()
    bot = PrimordialBot(settings)
    bot.run(settings.token, log_handler=None)
