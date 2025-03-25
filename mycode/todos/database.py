from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

# SessionLocal is a class that will be used to create a database session. Parameters autocommit=False and autoflush=False are set to prevent the session from automatically committing changes to the database and to prevent autoflushing.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base is an instance of the declarative_base class. It will be used to create a base class for our database models.
Base = declarative_base()