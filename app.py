from litestar import Litestar

from file_router import FILE_ROUTER

app = Litestar(route_handlers=[FILE_ROUTER])
