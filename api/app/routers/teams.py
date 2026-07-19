from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import Team, User
from app.schemas.team import TeamCreate, TeamResponse
from app.schemas.user import UserResponse

router = APIRouter(prefix="/teams", tags=["teams"])

@router.post("/", response_model=TeamResponse)
def create_team(team: TeamCreate, db: Session = Depends(get_db)):
    new_team = Team(name=team.name)
    db.add(new_team)
    db.commit()
    db.refresh(new_team)
    return new_team

@router.post("/{team_id}/users/{user_id}")
def add_user_to_team(team_id: int, user_id: int, db: Session = Depends(get_db)):
    team = db.query(Team).filter(Team.id == team_id).first()
    user = db.query(User).filter(User.id == user_id).first()

    if not team or not user:
        raise HTTPException(status_code=404, detail="Team or User not found")

    team.users.append(user)
    db.commit()
    return {"message": f"User {user.name} added to team {team.name}"}

@router.get("/{team_id}/users", response_model=List[UserResponse])
def get_team_users(team_id: int, db: Session = Depends(get_db)):
    team = db.query(Team).filter(Team.id == team_id).first()
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team.users

@router.delete("/{team_id}/users/{user_id}")
def remove_user_from_team(team_id: int, user_id: int, db: Session = Depends(get_db)):
    team = db.query(Team).filter(Team.id == team_id).first()
    user = db.query(User).filter(User.id == user_id).first()

    if not team or not user:
        raise HTTPException(status_code=404, detail="Team or User not found")

    if user in team.users:
        team.users.remove(user)
        db.commit()
        return {"message": f"User {user.name} removed from team {team.name}"}
    
    raise HTTPException(status_code=404, detail="User is not in this team")

@router.put("/{team_id}", response_model=TeamResponse)
def update_team(team_id: int, team_update: TeamCreate, db: Session = Depends(get_db)):
    team = db.query(Team).filter(Team.id == team_id).first()
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    
    team.name = team_update.name
    db.commit()
    db.refresh(team)
    return team

@router.delete("/{team_id}")
def delete_team(team_id: int, db: Session = Depends(get_db)):
    team = db.query(Team).filter(Team.id == team_id).first()
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    db.delete(team)
    db.commit()
    return {"message": "Team deleted successfully"}
