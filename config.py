from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Awesome Avatar Generator Bot"

    # your telegram bot access token from BotFather
    telegram_bot_token: str

    # the telegram bot username
    telegram_bot_username: str

    # the base url for this app, has to be https:...
    base_url: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
