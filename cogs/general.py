import discord
from discord import app_commands
from discord.ext import commands

from utils.embeds import EmbedFactory


class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Check bot latency.")
    async def ping(self, interaction: discord.Interaction) -> None:
        latency = round(self.bot.latency * 1000)
        embed = EmbedFactory.success("Pong!", f"Current latency: **{latency}ms**")
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="about", description="About this bot starter.")
    async def about(self, interaction: discord.Interaction) -> None:
        embed = EmbedFactory.info(
            "About This Starter",
            "A clean modular starter built alongside PrimordialDM's master Discord bot reference.",
            fields=[
                ("Author", "PrimordialDM", True),
                ("Stack", "discord.py + slash commands", True),
                ("Reference File", "discord-bot-master-reference.py", False),
            ],
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="inviteinfo", description="Explain how to invite the bot safely.")
    async def inviteinfo(self, interaction: discord.Interaction) -> None:
        embed = EmbedFactory.info(
            "Invite Guidance",
            "Generate your invite URL from the Discord Developer Portal and only request the permissions you actually need.",
            fields=[
                ("Recommended", "Start minimal and add permissions as features require them.", False),
            ],
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(General(bot))
