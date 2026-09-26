
# Import SQLAlchemy components required for database configuration
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Configure the SQLite database
DATABASE_URL = "sqlite:///./pfms.db"

# Create the database engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Create a session factory for database operations
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Create the base class for database models
Base = declarative_base()
