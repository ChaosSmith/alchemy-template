# imports
import os
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.engine.url import URL
from app.db.config import DATABASE
from app.models import *
from sqlalchemy.ext.declarative import declarative_base

def parse_url(database):
    """
    Converts a db config dictionairy into an acceptable
    connection string.
    """
    if database and database['password']:
        # Assuming Remote
        return URL(**database)
    elif database:
        # Assuming Local
        return 'postgresql:///' + database['database']
    else:
        # Assuming Master Set Up
        return 'postgresql:///postgres'

def connect(database):
    """
    Performs database connection using database settings from db_config.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(parse_url(database))

def session():
    """
    Creates a new session with a database depending on the current environment
    Returns the new session object
    """

    Session = sessionmaker(bind=connect(DATABASE), autocommit=False, autoflush=False)
    return scoped_session(Session)

def create(engine, database):
    """
    Creates database
    """
    connection = engine.connect()
    connection.execute("commit")
    try:
        connection.execute("create database {db_name}".format(db_name=database['database']))
    except exc.ProgrammingError:
        print("Database Already Exists!")
    except:
        print("DB create failed!")
        raise
    finally:
        connection.close()

def drop(engine, database):
    """
    Drops database
    """
    connection = engine.connect()
    connection.execute("commit")
    try:
        connection.execute("drop database {db_name}".format(db_name=database['database']))
    except exc.ProgrammingError:
        print("Database Does Not Exist!")
    except:
        print("DB drop failed!")
        raise
    finally:
        connection.close()

def load(engine):
    """
    Generates schema as defined in model files
    """
    #if not database_exists(engine.url):
    # create_database(engine.url)
    DeclarativeBase.metadata.create_all(engine)

db_session = session()
DeclarativeBase.query = db_session.query_property()
