# Standard model that others will be copies off of

#imports
from app.db import DeclarativeBase
from app.db.types import *

class BaseTable(DeclarativeBase):

    __tablename__ = 'generic_table'

    id = Column(Integer, primary_key=True)

    generic_column = Column(String)
