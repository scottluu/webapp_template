from pathlib import Path

from litestar import Router, Response, get, MediaType
from litestar.exceptions import NotFoundException

DIST = (Path(__file__).parent / "frontend" / "dist").absolute()

INDEX_HTML = DIST / "index.html"


@get("/", media_type=MediaType.HTML)
async def get_index_html() -> bytes:
    """Handler function that returns a greeting dictionary."""
    return INDEX_HTML.read_bytes()


_MEDIA_TYPE_MAPPING = {
    "js": "text/javascript",
    "css": "text/css",
    "png": "image/png",
    "jpg": "image/jpeg",
    "svg": "image/svg+xml",
}


@get("/{p:path}")
async def get_file(p: Path) -> Response[bytes]:
    """Handler function that returns a greeting dictionary."""
    full = DIST.joinpath(str(p).lstrip("\\")).absolute()
    if str(full).startswith(str(DIST)) and full.exists():
        return Response(
            full.read_bytes(),
            media_type=_MEDIA_TYPE_MAPPING[full.name.split(".")[-1].lower()],
        )
    raise NotFoundException()


FILE_ROUTER = Router(path="/", route_handlers=[get_index_html, get_file])
