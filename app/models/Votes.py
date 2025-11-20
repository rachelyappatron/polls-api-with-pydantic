from datetime import datetime
from pydantic import BaseModel, Field, EmailStr
from uuid import UUID

class VoterCreate(BaseModel):
    email: EmailStr

class Voter(VoterCreate):
    voted_at: datetime = Field(default_factory=datetime.now)

class Vote(BaseModel):
    "The Vote read model"

    poll_id: UUID
    choice_id: UUID
    voter: Voter

class VoteById(BaseModel):
    choice_id: UUID
    voter: VoterCreate

class VoteByLabel(BaseModel):
    choice_label: int
    voter: VoterCreate