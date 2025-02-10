from fastapi import HTTPException
from sqlalchemy.orm import Session
#import test.db
from app.schemas.req_res_model import RequestModel
from app.db.database import Workstationtbl


def create_workstation_db(data:RequestModel, db:Session):
  db_workstation= Workstationtbl(**data.dict())
  db.add(db_workstation)
  db.commit()
  db.refresh(db_workstation)
  return db_workstation

def get_workstation_Id_db(workstation_Id: int, db: Session):
  
  return db.query(Workstationtbl).filter(Workstationtbl.WorkstationId == workstation_Id).first()
  

def get_all_workstations_db(db: Session):
    return db.query(Workstationtbl).all()

def update_workstation_Id_db(workstation_Id: str, data: RequestModel, db: Session):
    workstation = db.query(Workstationtbl).filter(Workstationtbl.WorkstationId == workstation_Id).first()
    if not workstation:
        raise HTTPException(status_code=404, detail="Workstation not found")
    for key, value in data.dict().items():
        setattr(workstation, key, value)
    db.commit()
    db.refresh(workstation)
    return {"message": "Workstation is updated successfully"}
   

def delete_workstation_Id_db(workstation_Id:str,db: Session):
    workstation=db.query(Workstationtbl).filter(Workstationtbl.WorkstationId==workstation_Id).first()
    if not workstation:
      return None  
    db.delete(workstation)
    db.commit()  # Commit the deletion to the database
    return workstation
    