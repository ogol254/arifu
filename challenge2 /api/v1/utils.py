from flask_restplus import Namespace, fields


class StudentDTO(object):
    """Student Data Transfer Object"""
    api = Namespace('student', description='Collecting new user Documentation')
    n_stud = api.model('student request', {
        'name': fields.String(required=True, description="student name"),
        'student_num': fields.Integer(required=True, description="student's id"),
        'course': fields.Integer(required=True, description="student's course code"),
        'email': fields.String(required=True, description="student's email address")
    })


class CourseDTO(object):
    """Student Data Transfer Object"""
    api = Namespace('course', description='Collecting new course')
    course = api.model('course request', {
        'name': fields.String(required=True, description="course  name"),
        'code': fields.Integer(required=True, description="course code")
    })
