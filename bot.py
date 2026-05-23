import logging

import discord
from discord.ext import commands

from utils.config import Settings, load_settings

# Quick customization options:
# - Add or remove cogs in ENABLED_EXTENSIONS.
# - Uncomment optional intent flags if your features need them.
# - Change DEFAULT_PRESENCE_TEXT to match your project branding.
# - Uncomment the optional event stubs at the bottom to extend behavior quickly.
ENABLED_EXTENSIONS = (
    "cogs.general",
    "cogs.admin",
    # "cogs.fun",        # Example: add your own cogs here
    # "cogs.moderation", # Example: add your own cogs here
)

DEFAULT_PRESENCE_TEXT = "PrimordialDM master template"

# Optional presence examples (uncomment one in on_ready):
# await self.change_presence(activity=discord.Game("Use /help to get started"))
# await self.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="/help"))
# await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="your server"))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("PrimordialBot")


class PrimordialBot(commands.Bot):
    def __init__(self, settings: Settings):
        intents = discord.Intents.default()

        # Core intents used by this template.
        intents.guilds = True
        intents.messages = True
        intents.message_content = True
        intents.members = True

        # Optional intent toggles (uncomment if your bot needs these).
        # intents.reactions = True
        # intents.typing = False
        # intents.presences = True  # Requires privileged intent in Discord developer portal.

        super().__init__(
            command_prefix=settings.prefix,
            intents=intents,
            help_command=None,
        )
        self.settings = settings

    async def setup_hook(self) -> None:
        for extension in ENABLED_EXTENSIONS:
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
        await self.change_presence(activity=discord.Game(DEFAULT_PRESENCE_TEXT))

    # Optional quick stubs (uncomment and customize):
    # async def on_guild_join(self, guild: discord.Guild) -> None:
    #     logger.info("Joined guild: %s (%s)", guild.name, guild.id)

    # async def on_guild_remove(self, guild: discord.Guild) -> None:
    #     logger.info("Removed from guild: %s (%s)", guild.name, guild.id)

    # async def on_command_error(self, ctx: commands.Context, error: Exception) -> None:
    #     logger.exception("Command error in %s: %s", ctx.command, error)

    # async def on_message(self, message: discord.Message) -> None:
    #     if message.author.bot:
    #         return
    #     # Add custom message handling here, then keep command processing.
    #     await self.process_commands(message)


if __name__ == "__main__":
    settings = load_settings()
    bot = PrimordialBot(settings)
    bot.run(settings.token, log_handler=None)
