from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.trivia import router as trivia_router

app = FastAPI(
    title="Eho-Eho API",
    description="Eho-EhoアプリケーションのバックエンドAPI。",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(trivia_router, prefix="/trivia", tags=["trivia"])

@app.get("/")
async def root():
    return {"message": "Welcome to Eho-Eho API"}
