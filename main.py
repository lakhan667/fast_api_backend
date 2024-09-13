from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.user_router import router

app = FastAPI()

origins = [
    "http://localhost:8001", 
    "http://localhost:8000", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)