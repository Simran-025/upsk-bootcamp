from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.link import LinkCreate, LinkResponse
from app.services import links_service

router = APIRouter(prefix="/links")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=LinkResponse)
def create(data: LinkCreate, db: Session = Depends(get_db)):
    return links_service.create_link(db, data.long_url)