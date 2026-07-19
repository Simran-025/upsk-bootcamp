from pydantic import BaseModel, field_validator
from datetime import datetime

class LinkCreate(BaseModel):
    long_url: str

    @field_validator("long_url")
    @classmethod
    def validate_url(cls, v: str) -> str:
        # 1. Clean whitespace
        v = v.strip()
        
        # 2. Block control characters (security check)
        if any(ord(c) < 32 for c in v):
            raise ValueError("URL contains illegal control characters")
            
        # 3. Scheme validation (Allowlist only http/https)
        # Prevents 'javascript:' or 'data:' protocol attacks
        if not (v.startswith("http://") or v.startswith("https://")):
            raise ValueError("URL must start with http:// or https://")
            
        return v

class LinkResponse(BaseModel):
    id: int
    code: str
    long_url: str
    created_at: datetime
    
    class Config:
        from_attributes = True