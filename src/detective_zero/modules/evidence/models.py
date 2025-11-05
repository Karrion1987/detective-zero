
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class Evidence(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    case_id: Optional[int] = Field(default=None, foreign_key="case.id")
    kind: str = "file"
    path: str = ""
    hash: str = ""
    custody_signature: str = ""
    created_at: datetime = Field(default_factory=datetime.utcnow)
