# Archivo con las definiciones del motor, sesión y base de SQLAlchemy.

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///comunidad.sqlite')
Session = sessionmaker(bind=engine)
Base = declarative_base()