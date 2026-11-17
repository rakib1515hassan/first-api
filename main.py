from fastapi import FastAPI

from apis.home import router as home_router
from apis.landing_page import router as landing_page_router

app = FastAPI()

app.include_router(home_router)
app.include_router(landing_page_router)
