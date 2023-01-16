from fastapi import FastAPI

from v1.phone_numbers.endpoints import router as phone_numbers_router

app = FastAPI()

app.include_router(
    router=phone_numbers_router,
    prefix="/v1",
)
