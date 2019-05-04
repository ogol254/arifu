from ..db import init_db
from .basemodel import BaseModel


class StudentModel(BaseModel):
    """This class encapsulates the functions of the user model"""

    def __init__(self, name="", email="", student_num="", course=""):
        """initialize the user model"""
        self.name = name
        self.student_num = student_num
        self.course = course
        self.email = email
        self.db = init_db()

    def save(self):
        """Add incident details to the database"""
        student = {
            "name": self.name,
            "email": self.email,
            "student_num": self.student_num,
            "course": self.course
        }
        # check if course exists
        exists = BaseModel().check_item_exists(table="students", field="student_num", data=student['student_num'])
        if exists == True:
            return "Student Exists"

        database = self.db
        curr = database.cursor()
        query = """INSERT INTO students (student_num, name, email, course) \
            VALUES ( %(student_num)s, %(name)s, %(email)s, %(course)s) RETURNING student_num;
            """
        curr.execute(query, student)
        student_id = curr.fetchone()[0]
        database.commit()
        curr.close()
        return student_id

    def get_all_students(self):
        """return all students from the db """
        curr = self.db.cursor()
        curr.execute("""SELECT student_num, name, email, course, date_created FROM students ;""")
        data = curr.fetchall()
        resp = []

        for i, items in enumerate(data):
            student_num, name, email, course, date_created = items
            students = dict(
                student_num=int(student_num),
                name=name,
                email=email,
                course=course,
                created_on=str(date_created)

            )
            resp.append(students)
        return resp


class CourseModel(BaseModel):
    """This class encapsulates the functions of the user model"""

    def __init__(self, name="", code=""):
        """initialize the user model"""
        self.name = name
        self.code = code
        self.db = init_db()

    def save(self):
        """Add incident details to the database"""
        course = {
            "name": self.name,
            "code": self.code
        }
        # check if  exists

        exists = BaseModel().check_item_exists(table="courses", field="code", data=course['code'])
        if exists == True:
            return "Course Exists"

        database = self.db
        curr = database.cursor()
        query = """INSERT INTO courses (name, code) \
            VALUES ( %(name)s, %(code)s) RETURNING code;
            """
        curr.execute(query, course)
        course_code = curr.fetchone()[0]
        database.commit()
        curr.close()
        return course_code

    def get_all(self):
        """return all students from the db """
        curr = self.db.cursor()
        curr.execute("""SELECT name, code, date_created FROM courses ;""")
        data = curr.fetchall()
        resp = []

        for i, items in enumerate(data):
            name, code, date_created = items
            courses = dict(
                code=int(code),
                name=name,
                created_on=str(date_created)

            )
            resp.append(courses)
        return resp
