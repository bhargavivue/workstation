from pydantic import BaseModel

class RequestModel(BaseModel):
    WorkstationId: str
    WorkstationType: str
    OperatingSystem: str
    DateOfPurchase: str
    SerialNumber: str 
    Status:str
    IPAddress:str
    NetworkType:str
    AgentName:str
    BranchName: str
    Latitude: str
    Longitude: str
    WorkingHoursStartTime: str
    WorkingHoursEndTime: str
    Movable:bool=True
    
    class Config:
     orm_mode =True