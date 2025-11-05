
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from typing import List
from .models import Case
from .. import deps
from ..deps import Session

router = APIRouter(prefix="/cases", tags=["cases"])

@router.get("/", response_model=List[Case])
def list_cases(session: Session = Depends(deps.get_session)):
    return session.exec(select(Case)).all()

@router.post("/", response_model=Case, status_code=201)
def create_case(case: Case, session: Session = Depends(deps.get_session)):
    session.add(case)
    session.commit()
    session.refresh(case)
    return case

@router.get("/{case_id}", response_model=Case)
def get_case(case_id: int, session: Session = Depends(deps.get_session)):
    obj = session.get(Case, case_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Case not found")
    return obj
