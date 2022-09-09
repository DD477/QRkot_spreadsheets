
from pydantic import BaseModel, Field, HttpUrl


class GoogleApiReport(BaseModel):
    url: HttpUrl = Field(
        ...,
        example='https://docs.google.com/spreadsheets/d/{spreadsheet_id}'
    )