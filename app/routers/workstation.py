from fastapi  import APIRouter, Depends,HTTPException
from app.db.workstation_db import create_workstation_db, get_workstation_Id_db, get_all_workstations_db, update_workstation_Id_db, delete_workstation_Id_db 
from sqlalchemy.orm import Session

from app.schemas.req_res_model import RequestModel
from app.db.database import get_db



router=APIRouter(prefix="/workstations") 

@router.post("/")
def create_workstation(data:RequestModel, db: Session= Depends(get_db)):
   return create_workstation_db(data,db)

@router.get("/{workstation_Id}")
def get_workstation_Id(workstation_Id: str,data:RequestModel, db: Session= Depends(get_db)):
    workstation = get_workstation_Id_db(data) 
    if workstation is None: 
      raise HTTPException(status_code=404, detail="Workstation not found")
    return workstation

@router.get("/")    
def get_all_workstations_Id(db: Session=Depends(get_db)):
    workstations=get_all_workstations_db(db)
    print(workstations)
    if workstations is None:
      raise HTTPException(status_code=404, detail="no workstation exist")
    return workstations

@router.put("/update")
def update_workstation_Id(workstation_Id:str,data:RequestModel ,db:Session =Depends(get_db)):
      workstation=update_workstation_Id_db(workstation_Id,data,db)
      if workstation_Id is None:
        raise HTTPException(status_code=404, detail="Workstation not found")
      return workstation


@router.delete("{/workstation_Id}")
def delete_workstation_Id(workstation_Id: str,db:Session = Depends(get_db)):
   workstation = delete_workstation_Id_db(workstation_Id,db)
   if workstation is None:
      raise HTTPException(status_code=404, detail="Workstation is not found")
   return {"message": "Workstation deleted successfully"}
        
