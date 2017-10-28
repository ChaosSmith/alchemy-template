# Standard model that others will be copies off of

#imports
from api.db.alchemy import *

class BaseTable(DeclarativeBase):

    __tablename__ = 'generic_table'

    id = Column(Integer, primary_key=True)

    generic_column = Column(String)
