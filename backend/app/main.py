from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.routes import upload
from app.routes import auth, upload, chat, summary

app = FastAPI(title="AI Document & Multimedia Chat API")

# CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROUTERS
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(upload.router)
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(summary.router, prefix="/summary", tags=["Summary"])
app.include_router(summary.router) 
app.mount("/media", StaticFiles(directory="uploads"), name="media")
