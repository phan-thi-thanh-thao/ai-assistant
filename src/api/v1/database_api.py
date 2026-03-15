from fastapi import APIRouter, HTTPException
from typing import List, Dict
from ...database.database import database_crud
from ...schemas.data import SearchRequest

router = APIRouter(prefix="/database", tags=["database"])

@router.get("/tables", response_model=List[str])
async def get_all_tables():
    """Get all table names."""
    try:
        tables = database_crud.get_all_tables()
        return tables
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/tables/{table_name}", response_model=List[Dict])
async def get_table_data(table_name: str, limit: int = None):
    """Get data from specific table."""
    try:
        data = database_crud.get_table_data(table_name, limit)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/tables/{table_name}/{id_value}", response_model=Dict)
async def get_by_id(table_name: str, id_value: str, id_column: str = "id"):
    """Get record by ID."""
    try:
        data = database_crud.get_by_id(table_name, id_value, id_column)
        if data is None:
            raise HTTPException(status_code=404, detail="Record not found")
        return data
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/tables/{table_name}/search", response_model=List[Dict])
async def search_in_table(table_name: str, request: SearchRequest):
    """Search in specific table."""
    try:
        results = database_crud.search(table_name, request.keyword)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))