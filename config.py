"""
Ingestion Service - Configuration
Loads database connection string from environment variable.
"""

import os
from dataclasses import dataclass


@dataclass
class Settings:
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:password@postgresql:5432/app_db",
    )

settings = Settings()