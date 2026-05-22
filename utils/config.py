from dataclasses import dataclass
import os

from dotenv import load_dotenv


@dataclass(slots=True)
class Settings:
    token: str
    owner_id: int
    log_channel_id: int
    welcome_channel_id: int
    starboard_channel_id: int
    suggestions_channel_id: int
    test_guild_id: int
    prefix: str


def load_settings() -> Settings:
    load_dotenv()

    token = os.getenv("DISCORD_TOKEN", "").strip()
    owner_id = int(os.getenv("OWNER_ID", "0") or "0")

    if not token:
        raise RuntimeError("DISCORD_TOKEN is missing. Copy .env.example to .env and fill it in.")
    if not owner_id:
        raise RuntimeError("OWNER_ID is missing. Set your Discord user ID in .env.")

    return Settings(
        token=token,
        owner_id=owner_id,
        log_channel_id=int(os.getenv("LOG_CHANNEL_ID", "0") or "0"),
        welcome_channel_id=int(os.getenv("WELCOME_CHANNEL_ID", "0") or "0"),
        starboard_channel_id=int(os.getenv("STARBOARD_CHANNEL_ID", "0") or "0"),
        suggestions_channel_id=int(os.getenv("SUGGESTIONS_CHANNEL_ID", "0") or "0"),
        test_guild_id=int(os.getenv("TEST_GUILD_ID", "0") or "0"),
        prefix=os.getenv("BOT_PREFIX", "!"),
    )
