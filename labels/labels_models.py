from pydantic import BaseModel



class LabelValue(BaseModel):
    label_id: int
    value: str

class LabelHeader(BaseModel):
    id: int
    label_name: str
    label_values: list[LabelValue]
