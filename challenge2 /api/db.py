import psycopg2
import os

# sample = "dbname='arifu' host='localhost' port='5432' user='Mcogol' password='root'"

url = os.getenv("DATABASE_URL")


def connection(connect_url):
    conn = psycopg2.connect(connect_url)
    return conn


def init_db():
    conn = connection(url)
    curr = conn.cursor()
    queries = tables()

    for query in queries:
        curr.execute(query)
    conn.commit()
    return conn


def tables():
    db1 = """CREATE TABLE IF NOT EXISTS students (
    student_num numeric PRIMARY KEY NOT NULL,
    name character varying(50) NOT NULL,
    course numeric NOT NULL,
    email character varying(50) NOT NULL,
    date_created timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
    );"""

    db2 = """CREATE TABLE IF NOT EXISTS courses (
    code serial PRIMARY KEY NOT NULL,
    name character varying(50) NOT NULL,
    date_created timestamp with time zone DEFAULT ('now'::text)::date NOT NULL
    );"""

    queries = [db2, db1]
    return queries
