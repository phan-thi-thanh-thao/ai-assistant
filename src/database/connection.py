from supabase import create_client, Client
from ..core.config import config
from ..core.log_utils import get_logger

class SupabaseConnection:
    _instance = None
    _client = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if self._client is None:
            self.logger = get_logger(__name__)
            self._connect()
    
    def _connect(self):
        """Connect to Supabase."""
        try:
            if not config.SUPABASE_URL or not config.SUPABASE_ANON_KEY:
                raise ValueError("Missing SUPABASE_URL or SUPABASE_ANON_KEY")
            
            self._client = create_client(config.SUPABASE_URL, config.SUPABASE_ANON_KEY)
            self.logger.info("Connected to Supabase")
            
        except Exception as e:
            self.logger.error(f"Failed to connect to Supabase: {e}")
            raise
    
    @property
    def client(self) -> Client:
        """Get Supabase client."""
        if self._client is None:
            self._connect()
        return self._client

supabase_conn = SupabaseConnection()