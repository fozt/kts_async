import base64
from typing import Any

import jsons
from aiohttp.web_response import Response
from aiohttp.web_response import json_response as aiohttp_json_response

from app.web.schemes import OkResponseSchemas


def json_response(data: Any = None, message: str = 'ok', status: int = 200) -> Response[OkResponseSchemas]:
    if data is None:
        data = {}
    return aiohttp_json_response(data=OkResponseSchemas(data=data, status=message).dict(),
                                 dumps=jsons.dumps, status=status)


def check_basic_auth(raw_credentials: str, username: str, password: str) -> bool:
    raw_credentials = raw_credentials.removeprefix('Basic ')
    credentials = base64.b64decode(raw_credentials).decode()

    parts = credentials.split(":")
    if len(parts) != 2:
        return False
    return parts[0] == username and parts[1] == password
