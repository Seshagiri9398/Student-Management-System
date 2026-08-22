import psycopg2

def get_connection():
    connection = psycopg2.connect(
        host="localhost",
        database="student_management_db",
        user="postgres",
        password="seshu123",
        port="5432"

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

    cursor.execute(query)

    rows = cursor.fetchall()

    cursor.close()
    connection.close()
    return rows

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
    cursor.close()
    connection.close()

if __name__ == "__main__":
    connection = get_connection()

    print("Database connection successful!")

    connection.close()