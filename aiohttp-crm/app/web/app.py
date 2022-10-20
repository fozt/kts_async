from aiohttp.web import (Application as AiohttpApplication, run_app as aiohttp_run_app,
                         Request as AiohttpRequest)
from aiohttp_pydantic import PydanticView, oas

from app.store import setup_accessors
from app.store.crm.accessor import CrmAccessor
from app.web.config import Settings, setup_config
from app.web.middlewares import setup_middlewares
from app.web.routes import setup_routes


class Application(AiohttpApplication):
    config: Settings | None = None
    database: dict = {}
    crm_accessor: CrmAccessor | None = None


class Request(AiohttpRequest):
    @property
    def app(self) -> Application:
        return super().app


class View(PydanticView):
    @property
    def request(self) -> Request:
        return super().request


app = Application()


def run_app():
    setup_config(app)
    oas.setup(app)
    setup_routes(app)
    setup_middlewares(app)
    setup_accessors(app)
    aiohttp_run_app(app)
