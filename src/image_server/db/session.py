import logging
import os
from functools import cache
from sqlalchemy import create_engine, Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL
from sqlalchemy.pool import QueuePool

logger = logging.getLogger(__name__)

Base = declarative_base()

@cache
def get_db_engine() -> Engine:
    logger.info("Database engine created!")
    connection_string: URL = build_connection_string()
    return create_engine(
        connection_string,
        echo=False,
        poolclass=QueuePool,
        pool_size=5,
        max_overflow=32,  # 2 * max_cpu
    )

def build_connection_string() -> URL:
    return URL.create(
        drivername="postgresql+psycopg2",
        username="test",
        password="test",
        host=os.getenv("DATABASE_HOST", "localhost"),
        port=5432,
        database="test",
    )
