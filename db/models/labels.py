from pydantic import BaseModel
from db.models.users import User


class LabelValue(BaseModel):
    label_id: int # Identificador del valor dentro de la etiqueta
    value: str # Valor del campo


class Label(BaseModel):
    id: int # Identificador de la etiqueta
    user_id: int # Identificador del usuario que crea la etiqueta
    label_type: int # Define si la etiqueta es para ingresos o gastos
    label_name: str # Nombre de la etiqueta
    label_values: list[LabelValue] # Valores que puede tomar la etiqueta


class LabelModel():
    def __init__(self, user_id: int) -> None:
        pass