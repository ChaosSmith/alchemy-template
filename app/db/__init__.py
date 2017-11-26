from sqlalchemy.ext.declarative import declarative_base
from app.db.methods import session, connect, DATABASE, parse_url, create, load, drop

DeclarativeBase = declarative_base()
db_session = session()
DeclarativeBase.query = db_session.query_property()
