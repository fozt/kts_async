import typing

from aiohttp.web import middleware
from aiohttp.web_exceptions import HTTPException

from app.web.utils import json_response

if typing.TYPE_CHECKING:
    from app.web.app import Application


@middleware
async def error_handling_middleware(request, handler):
    try:
        response = await handler(request)
    except HTTPException as exc:
        return json_response(status=exc.status, message=str(exc))
    except Exception as exc:
        return json_response(status=500, message=str(exc))
    return response


def setup_middlewares(app: "Application"):
    app.middlewares.append(error_handling_middleware)
