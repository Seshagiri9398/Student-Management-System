import os

import psycopg2
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker


load_dotenv()


DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)



engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(
    bind=engine, 
    autoflush=False, 
    autocommit =False
    )

Base = declarative_base()



def get_connection():
    connection = psycopg2.connect(
        host = os.getenv("DB_HOST"),
        database = os.getenv("DB_NAME"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD"),
        port = os.getenv("DB_PORT")
        
    )

    return connection

def add_student_to_db(student):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO students
        (student_id,student_name,age,course,department)
        VALUES (%s,%s,%s,%s,%s)
    """

    try:

        cursor.execute(
            query,
            (
                student.student_id,
                student.student_name,
                student.age,
                student.course,
                student.department
            )
        )

        connection.commit()
    except Exception as e:
        print("Database error:",e)
        connection.rollback()
    finally:
        cursor.close()
        connection.close()


def get_all_students():
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT student_id,student_name,age,course,department
        FROM students
        ORDER BY student_id
    """
    try:

        cursor.execute(query)

        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print("Database error:",e)
        connection.rollback()
    finally:
        cursor.close()
        connection.close()


def update_student_in_db(student):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        UPDATE students
        SET student_name = %s,
        age = %s,
        course = %s,
        department = %s
        WHERE student_id = %s
    """
    try:

        cursor.execute(
                query,
                (
                    student.student_name,
                    student.age,
                    student.course,
                    student.department,
                    student.student_id
                )
            )
        connection.commit()

    except Exception as e:
        print("Database error:",e)
        connection.rollback()

    finally:
        cursor.close()
        connection.close()


def delete_student_in_db(student_id):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        DELETE FROM students
        WHERE student_id=%s
    """
    try:

        cursor.execute(
            query,
            (student_id,)
        )

        connection.commit()

    except Exception as e:
        print("Database error:",e)
        connection.rollback()

    finally:
        cursor.close()
        connection.close()

def check_student_id(student_id):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT student_id from students
        WHERE student_id = %s
    """

    exist = False
    try:

        cursor.execute(
            query,
            (student_id,)
        )

        result = cursor.fetchone()

        if result:
           exist = True

    except Exception as e:
        print("Database error:",e)
        connection.rollback()

    finally:
        cursor.close()
        connection.close()

    return exist 

def get_student_by_id(student_id):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT student_id,student_name,age,course,department
        FROM students
        WHERE student_id = %s
    """

    result = None
    
    try:

        cursor.execute(
            query,
            (student_id,)
        )

        result = cursor.fetchone()
    except Exception as e:
        print("Database error:",e)
        connection.rollback()
    finally:
        cursor.close()
        connection.close()
        
    return result
 


if __name__ == "__main__":
    connection = get_connection()

    print("Database connection successful!")
    connection.close()

try:
    with engine.connect() as connection:
        print("SQLAlchemy database connected successfully!")
except Exception as e:
    print("SQLAlchemy connection failed:", e)
