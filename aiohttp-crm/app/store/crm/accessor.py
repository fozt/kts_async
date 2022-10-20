import typing
import uuid

from loguru import logger

from app.crm.models import User


if typing.TYPE_CHECKING:
    from app.web.app import Application


class CrmAccessor:
    def __init__(self):
        self.app: Application | None = None

    async def add_user(self, user: User):
        self.app.database['users'].append(user)

    async def list_users(self) -> list[User]:
        return self.app.database['users']

    async def get_user(self, id_: uuid.UUID) -> User | None:
        for user in self.app.database['users']:
            if user.id_ == id_:
                return user

    async def connect(self, app: "Application"):
        self.app = app
        if "users" not in self.app.database:
            self.app.database["users"] = []
        logger.info('connect to database')

    async def disconnect(self, _: "Application"):
        self.app = None
        logger.info('disconnect to database')
