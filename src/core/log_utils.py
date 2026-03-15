import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler(sys.stderr)]
)

logging.getLogger("strands").setLevel(logging.DEBUG)

def get_logger(name: str) -> logging.Logger:
    """Get logger instance."""
    return logging.getLogger(name)