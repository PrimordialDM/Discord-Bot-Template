import discord
from discord import app_commands
from discord.ext import commands

from utils.embeds import EmbedFactory


class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def _is_owner(self, interaction: discord.Interaction) -> bool:
        return interaction.user.id == self.bot.settings.owner_id

    @app_commands.command(name="sync", description="Sync slash commands. Owner only.")
    async def sync(self, interaction: discord.Interaction) -> None:
        if not self._is_owner(interaction):
            await interaction.response.send_message("Owner only.", ephemeral=True)
            return

        if self.bot.settings.test_guild_id:
            guild = discord.Object(id=self.bot.settings.test_guild_id)
            synced = await self.bot.tree.sync(guild=guild)
            target = f"test guild {self.bot.settings.test_guild_id}"
        else:
            synced = await self.bot.tree.sync()
            target = "global scope"

        embed = EmbedFactory.success("Commands Synced", f"Synced **{len(synced)}** commands to {target}.")
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="extensions", description="List loaded extensions. Owner only.")
    async def extensions(self, interaction: discord.Interaction) -> None:
        if not self._is_owner(interaction):
            await interaction.response.send_message("Owner only.", ephemeral=True)
            return

        loaded = "\n".join(f"- {name}" for name in sorted(self.bot.extensions)) or "No extensions loaded."
        embed = EmbedFactory.info("Loaded Extensions", loaded)
        await interaction.response.send_message(embed=embed, ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Admin(bot))
