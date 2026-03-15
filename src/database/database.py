from typing import List, Dict, Any
from .connection import supabase_conn
from ..core.log_utils import get_logger

class DatabaseCRUD:
    def __init__(self):
        self.client = supabase_conn.client
        self.logger = get_logger(__name__)
    
    def get_all_tables(self) -> List[str]:
        """Get all table names."""
        try:
            result = self.client.rpc('get_table_names').execute()
            tables = [row['table_name'] for row in result.data] if result.data else []
            self.logger.info(f"Retrieved {len(tables)} tables")
            return tables
        except Exception as e:
            self.logger.error(f"Error getting tables: {e}")
            # Fallback: return hardcoded tables if RPC fails
            # TODO: Update this list with your actual table names
            return ['users', 'products', 'orders']  # Replace with your tables
    
    def get_table_data(self, table_name: str, limit: int = None) -> List[Dict]:
        """Get data from table."""
        try:
            query = self.client.table(table_name).select("*")
            if limit:
                query = query.limit(limit)
            result = query.execute()
            self.logger.info(f"Retrieved {len(result.data)} records from {table_name}")
            return result.data
        except Exception as e:
            self.logger.error(f"Error getting data from {table_name}: {e}")
            return []
    
    def get_by_id(self, table_name: str, id_value: Any, id_column: str = "id") -> Dict:
        """Get record by ID."""
        try:
            result = self.client.table(table_name).select("*").eq(id_column, id_value).execute()
            data = result.data[0] if result.data else None
            self.logger.info(f"Retrieved record from {table_name} with {id_column}={id_value}")
            return data
        except Exception as e:
            self.logger.error(f"Error getting record from {table_name}: {e}")
            return None
    
    def search(self, table_name: str, keyword: str) -> List[Dict]:
        """Search by keyword in all columns."""
        try:
            # Get all data and filter in Python (simple approach)
            result = self.client.table(table_name).select("*").execute()
            
            # Filter records containing keyword in any field
            filtered = []
            for record in result.data:
                if any(keyword.lower() in str(v).lower() for v in record.values()):
                    filtered.append(record)
            
            self.logger.info(f"Found {len(filtered)} records in {table_name}")
            return filtered
        except Exception as e:
            self.logger.error(f"Error searching in {table_name}: {e}")
            return []
        
database_crud = DatabaseCRUD()