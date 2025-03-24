from pydantic import BaseModel,ConfigDict
from typing import Dict, Any


class SMS_Payload(BaseModel):
    
    sms_payload : Dict[Any,Any]
    
    def to_json(self) -> str:
        return self.to_dict()  
    
