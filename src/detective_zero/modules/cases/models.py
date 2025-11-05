
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class Case(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str = ""
    status: str = "open"
    created_at: datetime = Field(default_factory=datetime.utcnow)
