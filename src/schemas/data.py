from pydantic import BaseModel
from typing import List, Dict, Any

# Database schemas
class SearchRequest(BaseModel):
    keyword: str

class TableResponse(BaseModel):
    tables: List[str]

class DataResponse(BaseModel):
    data: List[Dict[str, Any]]

class HealthResponse(BaseModel):
    status: str
    message: str