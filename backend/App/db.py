import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://usuario:senha@localhost:5432/minhalivraria"
)

# cria o engine SQLAlchemy (síncrono)
engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)


# session factory e base declarativa para os models
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# dependency para FastAPI — use Depends(get_db) nas rotas


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
