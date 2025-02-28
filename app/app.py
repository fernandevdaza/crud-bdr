from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.api.user import router as user_router
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/user", tags=["user"])