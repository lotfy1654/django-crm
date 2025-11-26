# Django CRM Project

This is a **Django CRM (Customer Relationship Management) web application** that uses **MySQL** as the database backend.  

---

## Technologies

- Python 3.x  
- Django 4.x (or your version)  
- MySQL  

---

## Setup and Installation

1. **Clone the repository**  

```bash
git clone https://github.com/lotfy1654/django-crm.git
cd django-crm
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

## Database Setup

You can create the MySQL database using your Python script `mydb.py`:

```bash
python mydb.py
```

## Finally, apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Running the Project

```bash 
python manage.py runserver
```
Visit http://127.0.0.1:8000/ in your browser.