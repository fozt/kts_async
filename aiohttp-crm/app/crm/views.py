import uuid

from aiohttp.web_exceptions import HTTPNotFound, HTTPUnauthorized, HTTPForbidden
from aiohttp_pydantic.oas.typing import r201, r200

from app.crm.models import User
from app.crm.schemes import IUserCreate, IUserRead
from app.web.app import View
from app.web.schemes import OkResponseSchemas
from app.web.utils import json_response, check_basic_auth


class AddUserView(View):
    async def post(self, user_in: IUserCreate) -> r201[OkResponseSchemas[IUserRead]]:
        user = User(email=user_in.email, id_=uuid.uuid4())
        await self.request.app.crm_accessor.add_user(user)
        return json_response(IUserRead.parse_obj(user), status=201)


class ListUsersView(View):
    async def get(self) -> r200[OkResponseSchemas[list[IUserRead]]]:
        auth_header = self.request.headers.get('Authorization')
        if not auth_header:
            raise HTTPUnauthorized
        if not check_basic_auth(auth_header, self.request.app.config.username, self.request.app.config.password):
            raise HTTPForbidden
        users = await self.request.app.crm_accessor.list_users()
        raw_users = [IUserRead.parse_obj(user) for user in users]
        return json_response(data=raw_users)


class GetUserView(View):
    async def get(self, id: uuid.UUID) -> r200[OkResponseSchemas[IUserRead]]:
        user = await self.request.app.crm_accessor.get_user(id)
        if user:
            return json_response(data=IUserRead.parse_obj(user))
        else:
            raise HTTPNotFound
