from fastapi import FastAPI
from app.routers import links, redirect

app = FastAPI()

@app.get("/live")
async def live():
    return {"status": "ok"}

@app.get("/ready")
async def ready():
    return {"status": "ok"}

# Include your new API routers
app.include_router(links.router)
app.include_router(redirect.router)