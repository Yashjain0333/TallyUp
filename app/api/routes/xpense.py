from fastapi import APIRouter, Depends
from typing import Annotated
import json
from api.dependencies import oauth2_scheme
from schemas._xpense import SMS_Payload
from utils.ai_utils import TestGem

xpense_router = APIRouter()


@xpense_router.post("/xpense")
async def read_sms(
    token: str = Depends(oauth2_scheme),
    sms_payload: SMS_Payload = Depends(),
):
    """
    Endpoint to process SMS payloads with token-based authentication.

    Args:
        token (str): The access token provided by the client.
        sms_payload (SMS_Payload): The payload containing SMS data.

    Returns:
        int: HTTP status code 200 on success.
    """

    print(sms_payload)
    # print(type(await sms_payload.json()))

    return 200


@xpense_router.get("/chat",)
async def get_users():
    """_summary_

    Returns:
        _type_: _description_
    """
    return json.loads(TestGem()._try())
