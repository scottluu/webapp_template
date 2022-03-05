from pathlib import Path

import aiofiles
from fastapi import FastAPI
from starlette.middleware.gzip import GZipMiddleware
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

_BUILD_DIR = Path(__file__).parent / "frontend" / "build"

app = FastAPI()
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.mount("/static", StaticFiles(directory=str(_BUILD_DIR / "static")), name="static")


@app.get("/", response_class=HTMLResponse)
async def get_root():
    index = _BUILD_DIR / "index.html"
    async with aiofiles.open(str(index), "r") as f:
        return await f.read()


@app.get("/api")
async def read_root():
    return {"Hello": "World"}
