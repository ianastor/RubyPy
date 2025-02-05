import logging
from .config import CONFIG

# Configure logging based on settings in config.py
logging.basicConfig(level=CONFIG.get("logging_level", "INFO"),
                    format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("RubyPy")