# Employee Management System (Django)

A web-based Prototype Employee Management System built using Django. The system provides employee management, role management, authentication, and administrative features through server-rendered templates.

## Features

* User Authentication
* Role Management
* Employee Management
* Form custom Validation
* Transaction Management
* Admin Dashboard
* AdminLTE Thame UI

---

## Technology Stack

* Python 3.x
* Django
* PostgreSQL database
* HTML
* CSS
* Bootstrap
* JavaScript

---

## Screenshots
screenshots/dashbaord.png

## Project Modules

### Authentication

* User Login
* User Logout

### Role Management

* Create Role
* View Roles
* Active/Inactive Status

### Employee Management

* Create Employee
* Employee Listing
* Delete Employee
* Role Assignment

---

## Installation

### Clone Repository

```bash
git clone https://github.com/bhimpdrajbanshi/HR-Management-System-Core-Django-.git

cd HR-Management-System-Core-Django
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Start Development Server

```bash
python manage.py runserver
```

---

## Authentication Flow

1. User enters email and password.
2. Django authenticates the user.
3. Session is created.
4. Protected pages use `@login_required`.
5. User logs out and session is destroyed.

---

## Database Transactions

Critical operations use Django transactions.

Example:

```python
with transaction.atomic():
    user = User.objects.create_user(...)
    Employee.objects.create(...)
```

If any operation fails, all database changes are rolled back automatically.

---

## Validation Layer

Business validation logic is separated from views.

Example Structure:

```text
validation/
├── validation_employee.py
├── role_validation.py
```

Benefits:

* Cleaner views
* Reusable validation
* Easier testing

---

## Employee Delete Strategy

Employees are not permanently removed.

Instead:

```python
employee.is_void = True
employee.save()
```

This helps maintain historical records and prevents accidental data loss.

---

## Security Features

* Django Authentication System
* Session Management
* CSRF Protection
* Login Required Decorator
* Server-Side Validation

---

## Future Improvements

* Django REST Framework APIs
* Role-Based Permissions
* Audit Logging
* Activity Tracking
* Dashboard Analytics
* Email Notifications

---

## License

This project is licensed under the MIT License.
