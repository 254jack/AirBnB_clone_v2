#!/usr/bin/python3
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import sqlalchemy
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """Used to instantiate engine create attributes"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('new_MYSQL_USER'),
                getenv('new_MYSQL_PWD'),
                getenv('new_MYSQL_HOST'),
                getenv('new_MYSQL_DB')),
            pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

        if getenv('new_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Run query on Current database session"""
        all_dict = {}
        if cls:
            for item in self.__session.query(models.classes[cls]).all():
                key = '{}.{}'.format(item.__class__.name, item.id)
                all_dict[key] = item
        else:
            for item, value in models.classes.items():
                if not isinstance(value, type(BaseModel)):
                    for it in self.__session.query(value).all():
                        key = '{}.{}'.format(it.__class__.__name__, it.id)
                        all_dict[key] = it
        return all_dict

    def new(self, obj):
        """Add the object to current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """remove/delete from the current database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session)
        self.__session = Session

    def close(self):
        """invokes remove() method on private session attributes"""
        self.__session.remove()
