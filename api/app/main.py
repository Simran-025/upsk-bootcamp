from fastapi import FastAPI
# Note: Ensure you have an 'app' folder with a 'routers' subfolder. 
# If your folder is named 'api' instead, change this to: from routers import links, redirect
from app.routers import links, redirect

app = FastAPI()

@app.get("/live")
async def live():
    return {"status": "ok"}

@app.get("/ready")
async def ready():
    return {"status": "ok"}

# Include your API routers
app.include_router(links.router)
app.include_router(redirect.router)