import hendlers
from fastapi import APIRouter
api_router = APIRouter()
# Setup routes
api_router.include_router(hendlers.router, tags=["home"])
