# Student Management System

A RESTful Student Management System built using Python, FastAPI, SQLAlchemy, and PostgreSQL.


## Features

- Create, read, update, and delete student records
- PostgreSQL database integration
- SQLAlchemy ORM
- Pydantic request and response validation
- Input validation and error handling
- Search students by name
- Pagination
- Sorting by student ID or name
- Ascending and descending order
- Swagger/OpenAPI API documentation




## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Git & GitHub



## API Endpoints


| Method   | Endpoint                       | Description                              |
| -------- | ------------------------------ | ---------------------------------------- |
| `GET`    | `/students`                    | Get students with pagination and sorting |
| `GET`    | `/students/search?name={name}` | Search students by name                  |
| `GET`    | `/students/{student_id}`       | Get a student by ID                      |
| `POST`   | `/students`                    | Create a new student                     |
| `PUT`    | `/students/{student_id}`       | Update an existing student               |
| `DELETE` | `/students/{student_id}`       | Delete a student                         |




## Project Structure

```text
Student_Management_System/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
│
├── routers/
│   ├── __init__.py
│   └── students.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md




## Installation & Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd Student_Management_System
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=your_postgresql_database_url
```

Do not commit the `.env` file to GitHub.

### 5. Run the application

```bash
python -m uvicorn main:app --port 8002
```

### 6. Open API documentation

Open:

```text
http://127.0.0.1:8002/docs
```





## API Documentation

The API provides interactive documentation using Swagger UI.

After starting the application, visit:

```text
http://127.0.0.1:8002/docs
```

From Swagger UI, you can:

* View all available endpoints
* Test API requests
* View request and response schemas
* Test validation and error responses
