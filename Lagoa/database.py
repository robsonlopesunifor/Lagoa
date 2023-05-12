from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://{user}:{password}@{host}:{port}".format(
    user="postgres",
    password="postgres",
    host="postgres",
    port="5432",
)


engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_reset_on_return=None,)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=5, max_overflow=5, echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()

