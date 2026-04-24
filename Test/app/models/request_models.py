from pydantic import BaseModel

class PatientRequest(BaseModel):
    message: str