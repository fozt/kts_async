import typing


if typing.TYPE_CHECKING:
    from app.web.app import Application


from pydantic import BaseSettings


class Settings(BaseSettings):
    username: str
    password: str

    class Config:
        env_file = '.env'


def setup_config(app: "Application"):
    app.config = Settings()
