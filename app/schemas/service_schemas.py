from app.schemas.common import CommonResponse


class PingResponse(CommonResponse):
    message: str
