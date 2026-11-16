# University REST API in Django

A django REST API.

## Tech stack

- Python 3
- Django
- Django REST Framework
- psycopg2 (PostgreSQL)
- Pillow
- Database: PostgreSQL

## Project structure

- `university_rest_api_in_django/`: project settings and root URLs
- `university_app/`: Django app
- Tests: `university_app/tests.py`

## Data model

| Model | App | Fields |
|---|---|---|
| `StudyLevel` | `university_app` | — |
| `Person` | `university_app` | name, familyName, password, email, birthDate |
| `Group` | `university_app` | name, level, speciality, email, student_number |
| `Address` | `university_app` | number, street, city, postal_code |
| `Student` | `university_app` | photo, group, address |
| `Module` | `university_app` | name, due, model_type, level, study |
| `Teacher` | `university_app` | email_work, photo, grade, teacher_modules |
| `TeacherModules` | `university_app` | teacher, module, year, nb_Hours |

## URL routes

Declared in `urls.py`:

- `/student/all/`
- `/student/add/`
- `/student/delete/`
- `/group/`
- `/group/<int:id>`
- `/students/ (router)`
- `/groups/ (router)`
- `/addresses/ (router)`
- `/modules/ (router)`
- `/blog/`
- `/university/`

## How to run

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

`settings.py` is configured for PostgreSQL: create the database and use your own credentials before running `migrate`.

Then open `http://127.0.0.1:8000/`.

---

Author: [Chaouki Bayoudhi](https://github.com/ChaoukiBayoudhi)
