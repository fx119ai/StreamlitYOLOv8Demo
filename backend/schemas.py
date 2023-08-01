from pydantic import BaseModel
from typing import List


class PredictionResponse(BaseModel):
    annotated_img: List[List[List[int]]]