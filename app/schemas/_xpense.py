from pydantic import BaseModel,ConfigDict
from typing import Optional, Dict, Any

class XpenseBase(BaseModel):
    email: Optional[str] # make this required 
    name: Optional[str]


class SMS_Payload(XpenseBase):
    model_config = ConfigDict(extra='allow')
    sms_payload : Dict[Any,Any]
    def to_json(self) -> str:
        return self.to_dict()  
    


# class User(XpenseBase):
#     status: 200


#     class Config:
#         orm_mode = True