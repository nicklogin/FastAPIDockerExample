from pydantic import BaseModel


class EmptyResponse(BaseModel):
    ...


class PDInfo(BaseModel):
    version: str


class CSVRow(BaseModel):
    user_id: int
    firstname: str
    userdata: int
