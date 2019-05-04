"""
This module defines the base model and associated functions
"""

from flask import jsonify, make_response

from ..db import init_db


class BaseModel(object):
    """
    This class encapsulates the functions of the base model
    that will be shared across all other models
    """

    def __init__(self):
        """initialize the database"""
        self.db = init_db()

    def check_item_exists(self, table, field, data):
        """Check if the records exist"""
        curr = self.db.cursor()
        query = "SELECT * FROM {} WHERE {}='{}'".format(table, field, data)
        curr.execute(query)
        data = curr.fetchone()
        if not data:
            return False
        return True

    def _type(self):
        """returns the name of the inheriting class"""
        return self.__class__.__name__

    def close_db(self):
        """This function closes the database"""
        self.db.close()
        pass
