"""
This module sets up the users resource
Authored by: Ogol
"""
from flask_restplus import Api
from flask import Blueprint

version_one = Blueprint('version1', __name__, url_prefix="/api/v1")

from .views import api as student_auth
from .views import api_c as course_auth


api = Api(version_one,
          title='ARIFU API',
          version='1.0',
          description="Arifu")

api.add_namespace(course_auth, path="/courses")
api.add_namespace(student_auth, path="/students")
