import uuid
from sqlalchemy.orm import Session
from app.models import Link

def create_link(db: Session, long_url: str):
    # Generate a unique 8-character short code
    code = str(uuid.uuid4())[:8]
    
    db_link = Link(code=code, long_url=long_url)
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link
def get_link_by_code(db: Session, code: str):
    return db.query(Link).filter(Link.code == code).first()