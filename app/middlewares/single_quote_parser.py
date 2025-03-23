import ast
import json
from starlette.types import Receive, Scope, Send, ASGIApp

class SingleQuoteJSONMiddleware:
    def __init__(self, app: ASGIApp):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        if scope["type"] == "http":
            content_type = None
            for header_name, header_value in scope.get("headers", []):
                if "content-type" in header_name.decode():
                    content_type = header_value.decode()
                    break

            # Yeh Patani har baar aise hi aega toh theek nahi toh change karna padega @Vinayak
            if content_type == "application/json":

                async def receive_wrapper():
                    message = await receive()

                    if message["type"] == "http.request" and "body" in message:
                        body = message.get("body", b"")
                        if body:
                            body_str = body.decode()
                            if "'" in body_str:
                                try:
                                    data = ast.literal_eval(body_str)
                                    corrected_body = json.dumps(data).encode()
                                    message["body"] = corrected_body
                                except Exception as e:
                                    print(e)

                    return message

                await self.app(scope, receive_wrapper, send)
            else:
                await self.app(scope, receive, send)
        else:
            await self.app(scope, receive, send)