"""Logging configuration."""

import sys

from loguru import logger

from core.config import settings


def setup_logging() -> None:
    """Setup logging configuration."""
    logger.remove()
    logger.add(
        sys.stdout,
        format="<level>{level: <8}</level> | {time:YYYY-MM-DD HH:mm:ss} | {name}:{function}:{line} - <level>{message}</level>",
        level=settings.API_LOG_LEVEL,
        colorize=True,
    )
