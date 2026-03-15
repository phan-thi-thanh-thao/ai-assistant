class DatabaseError(Exception):
    """Database operation error."""
    pass

class ClaudeError(Exception):
    """Claude service error."""
    pass

class ConfigError(Exception):
    """Configuration error."""
    pass
