import os
import configparser
import pymongo
from mongeasy.exceptions import MongEasyDBConnectionError
from mongeasy.dynamics import create_document_class

connection = None


def get_connection():
    return connection


def connect(connection_str: str=None, db_name: str=None):
    global connection
    if connection is not None:
        return connection

    try:
        # Try connecting using connect function
        if connection_str and db_name:
            connection = pymongo.MongoClient(connection_str)[db_name]
            return connection
    except Exception as e:
        print(e)
    
    connect_from_env()
    connect_from_config()

    if connection is None:
        raise MongEasyDBConnectionError("Failed to connect to database using environment variables or config file.")

    return connection

def connect_from_env():
    global connection
    try:
        # Try connecting using environment variables
        connection_string = os.environ.get('MONGOEASY_CONNECTION_STRING')
        database_name = os.environ.get('MONGOEASY_DATABASE_NAME')
        if connection_string and database_name:
            connection = pymongo.MongoClient(connection_string)[database_name]
    except Exception as e:
        print(e)

def connect_from_config():
    global connection
    try:
        # Try connecting using config file
        config = configparser.ConfigParser()
        config.read('mongeasy.conf')
        if 'mongoeasy' in config:
            section = config['mongoeasy']
            connection_string = section.get('connection_string')
            database_name = section.get('database_name')
            if connection_string and database_name:
                connection = pymongo.MongoClient(connection_string)[database_name]
    except Exception as e:
        print(e)
        
        
connect()