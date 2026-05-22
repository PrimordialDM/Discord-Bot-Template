import discord


class EmbedFactory:
    default_color = 0x3498DB
    success_color = 0x2ECC71
    error_color = 0xE74C3C
    warning_color = 0xF39C12

    @classmethod
    def base(cls, title: str, description: str = "", color: int | None = None) -> discord.Embed:
        embed = discord.Embed(
            title=title,
            description=description,
            color=color or cls.default_color,
            timestamp=discord.utils.utcnow(),
        )
        embed.set_footer(text="PrimordialDM Discord Bot Starter")
        return embed

    @classmethod
    def success(cls, title: str, description: str = "") -> discord.Embed:
        return cls.base(f"✅ {title}", description, cls.success_color)

    @classmethod
    def error(cls, title: str, description: str = "") -> discord.Embed:
        return cls.base(f"❌ {title}", description, cls.error_color)

    @classmethod
    def warning(cls, title: str, description: str = "") -> discord.Embed:
        return cls.base(f"⚠️ {title}", description, cls.warning_color)

    @classmethod
    def info(
        cls,
        title: str,
        description: str = "",
        fields: list[tuple[str, str, bool]] | None = None,
    ) -> discord.Embed:
        embed = cls.base(title, description, cls.default_color)
        for name, value, inline in fields or []:
            embed.add_field(name=name, value=value, inline=inline)
        return embed
