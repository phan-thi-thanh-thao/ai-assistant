from strands import tool
from typing import Any
import json
from ...database.database import database_crud

@tool
def get_all_tables() -> str:
    """Get all tables in database.
    
    Returns:
        List of table names as JSON string
    """
    tables = database_crud.get_all_tables()
    return json.dumps(tables, ensure_ascii=False)

@tool
def get_table_data(table_name: str, limit: int = 10) -> str:
    """Get data from a specific table.
    
    Args:
        table_name: Table name
        limit: Maximum number of records (default 10)
    
    Returns:
        Table data as JSON string
    """
    data = database_crud.get_table_data(table_name, limit)
    return json.dumps(data, ensure_ascii=False)

@tool
def get_record_by_id(table_name: str, id_value: Any, id_column: str = "id") -> str:
    """Get a record by ID.
    
    Args:
        table_name: Table name
        id_value: ID value to find
        id_column: ID column name (default "id")
    
    Returns:
        Record as JSON string
    """
    data = database_crud.get_by_id(table_name, id_value, id_column)
    return json.dumps(data, ensure_ascii=False)

@tool
def search_in_table(table_name: str, keyword: str) -> str:
    """Search in table by keyword.
    
    Args:
        table_name: Table name to search
        keyword: Search keyword
    
    Returns:
        Search results as JSON string
    """
    results = database_crud.search(table_name, keyword)
    return json.dumps(results, ensure_ascii=False)