from fastapi import APIRouter, status, Request
from schemas._xpense import SMS_Payload
from typing import List, Any, Dict

xpense_router = APIRouter()


@xpense_router.post("/xpense")
async def read_sms(sms_payload: SMS_Payload):
    """_summary_

    Args:
        user (UserCreate): _description_
    """
    print(sms_payload)
    # print(type(await sms_payload.json()))

    return 200


# @xpense_router.get("/users/", response_model=List[User])
# async def get_users():
#     """_summary_

#     Returns:
#         _type_: _description_
#     """
#     # GO TO USER SERVICE

#     # Some Logic
#     # return users
#     pass
