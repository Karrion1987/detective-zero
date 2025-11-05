
from fastapi import APIRouter, Depends
from typing import List
from sqlmodel import select
from .models import Evidence
from .. import deps
from ..deps import Session

router = APIRouter(prefix="/evidence", tags=["evidence"])

@router.get("/", response_model=List[Evidence])
def list_evidence(session: Session = Depends(deps.get_session)):
    return session.exec(select(Evidence)).all()

@router.post("/", response_model=Evidence, status_code=201)
def create_evidence(evidence: Evidence, session: Session = Depends(deps.get_session)):
    session.add(evidence)
    session.commit()
    session.refresh(evidence)
    return evidence
