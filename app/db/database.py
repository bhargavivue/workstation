from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Boolean, Column, String

DATABASE_URL ="mysql+pymysql://root:root1234@localhost:3306/softdev"   
engine=create_engine(DATABASE_URL, pool_recycle=3600, echo=True)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

class Workstationtbl(Base):
    __tablename__ = "workstation_tbl"
    
    WorkstationId=Column(String(100),primary_key=True, index=True)
    WorkstationType=Column(String(100))
    OperatingSystem=Column(String(100))
    DateOfPurchase=Column(String(100))
    SerialNumber=Column(String(100))
    Status=Column(String(100))
    IPAddress=Column(String(100))
    NetworkType=Column(String(100))
    AgentName=Column(String(100))
    BranchName=Column(String(100))
    Latitude  = Column(String(100))
    Longitude=Column(String(100))
    WorkingHoursStartTime=Column(String(100))
    WorkingHoursEndTime=Column(String(100))
    Movable=Column (Boolean, default=False)
 





def get_db():
    db =SessionLocal()
    try:
       yield db
    finally:
      db.close() 
# Create the tables in the database (if they don't already exist)
Base.metadata.create_all(bind=engine)


