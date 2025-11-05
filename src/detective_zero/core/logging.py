
from loguru import logger

logger.add("app.log", rotation="1 week", retention="4 weeks", enqueue=True)
