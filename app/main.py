from fastapi import FastAPI
from app.api.v1.endpoints import router as api_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="CAG System", description="Cache-Augmented Generation API", version="1.0")

# Middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Cache-Augmented Generation API."}
