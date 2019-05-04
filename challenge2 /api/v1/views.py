from flask_restplus import Resource
from flask import jsonify, make_response, request

from .models import StudentModel, CourseModel
from .utils import StudentDTO, CourseDTO

api = StudentDTO().api
api_c = CourseDTO().api
n_stud = StudentDTO().n_stud
n_c = CourseDTO().course


@api.route("/welcome")
class DefaultR(Resource):
    def get(self):
        return "HELLO, Welcome to Arifu...."


@api.route("/students")
class Students(Resource):

    """This class collects the methods for the collecting student information"""
    @api.expect(n_stud, validate=True)
    def post(self):
        """This endpoint allows to collect student information """
        req_data = request.data.decode().replace("'", '"')
        if not req_data:
            return make_response(jsonify({"Message": "Provide data in the request"}))

        student_dateils = json.loads(req_data)
        try:
            name = student_dateils['name'].strip()
            student_num = student_dateils['student_num']
            email = student_dateils['email'].strip()
            course_code = student_dateils['course']
            if not re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
                            email):
                return make_response(jsonify({"Message": "The email provided is invalid"}))
        except (KeyError, IndexError) as e:
            return()
        student = {
            "name": name,
            "course": course_code,
            "student_num": student_num,
            "email": email
        }

        student_model = StudentModel(**student)
        try:
            _u_s = student_model.save()
            if not _u_s:
                raise ValueError
            else:
                return make_response(jsonify({
                    "Message": _u_s
                }), 201)
        except ValueError:
            return make_response(jsonify({"Message": "The student already exists"}))

    def get(self):
        """ Get all student"""
        students = StudentModel().get_all_students()
        resp = {
            "message": "success",
            "students": students
        }
        return resp, 200


@api_c.route("/courses")
class Course(Resource):

    """This class collects the methods for the collecting student information"""
    @api.expect(n_c, validate=True)
    def post(self):
        """This endpoint allows to collect student information """
        req_data = request.data.decode().replace("'", '"')
        if not req_data:
            return make_response(jsonify({"Message": "Provide data in the request"}))

        course = json.loads(req_data)
        try:
            name = course['name'].strip()
            code = course['code']

        except (KeyError, IndexError) as e:
            return()
        new_course = {
            "name": name,
            "code": code
        }
        coursemodel = CourseModel(**new_course)
        try:
            _u_s = coursemodel.save()
            if not _u_s:
                raise ValueError
            else:
                return make_response(jsonify({
                    "Message": _u_s
                }), 201)
        except ValueError:
            return make_response(jsonify({"Message": "The course already exists"}))

    def get(self):
        """ Get all student"""
        courses = CourseModel().get_all()
        resp = {
            "message": "success",
            "course": courses
        }
        return resp, 200
