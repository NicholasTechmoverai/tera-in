from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os

from config import WEB_SERVER

# Allowed origins
ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:8000",
    "https://tera-in.top", "https://www.tera-in.top",
    "https://ezed.tera-in.top",
    "http://127.0.0.1:8000",
    f"{WEB_SERVER}",
]

app = FastAPI(
    title="My API",
    description="Example FastAPI project with Vue frontend",
    version="1.0.0",
    docs_url="/swagger",
    redoc_url="/redocs",
    openapi_url="/openapi.json",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VUE_DIST_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "dist"))

# Mount Vue static assets (JS, CSS, images, fonts…)
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(VUE_DIST_DIR, "static")),
    name="static",
)

# Serve Vue index.html at root
@app.get("/", include_in_schema=False)
async def serve_root():
    return FileResponse(os.path.join(VUE_DIST_DIR, "index.html"))

# Catch-all route for Vue Router (history mode)
@app.get("/{full_path:path}", include_in_schema=False)
async def serve_vue(full_path: str):
    file_path = os.path.join(VUE_DIST_DIR, full_path)

    # Serve file if it exists
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return FileResponse(file_path)

    # Otherwise return index.html (SPA fallback)
    return FileResponse(os.path.join(VUE_DIST_DIR, "index.html"))




# uvicorn app:zed_app --reload
# uvicorn app:zed_app --reload --host 0.0.0.0 --port 8007
# cloudflared tunnel --url http://localhost:8000
