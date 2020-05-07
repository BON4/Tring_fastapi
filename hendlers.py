from fastapi import APIRouter, HTTPException
router = APIRouter()


class SiteHandler:

    def __init__(self, conf, executor, base_root):
        self._conf = conf
        self._executor = executor
        self._root = base_root
        self._loop = asyncio.get_event_loop()


@router.get("/")
async def index():
    return {"index": "Hello"}
