# Django MongoDB DRF Project
Welcome to my Django project using MongoDB and Django Rest Framework (DRF)!

## Overview
This project is designed as a learning exercise to explore the integration of Django with MongoDB as the database backend, leveraging Django Rest Framework for API development. It focuses on using MongoDB instead of traditional SQL databases and employs DRF's @api_view decorator for creating custom APIs. Serializers are used extensively to validate and manage data input and output.

## Features
- **MongoDB Integration:** The project utilizes MongoDB, a NoSQL database, for flexible and scalable data storage solutions.
- **Custom APIs with DRF:** Custom endpoints are created using DRF's @api_view decorator, allowing for fine-grained control over API behavior and responses.
- **Serializer Validation:** Serializers are used to validate incoming data, ensuring data integrity and consistency.
- **Django Commands:** Custom Django management commands are implemented to handle data import tasks efficiently.
  
## Requirements
- Python 3.x
- Django
- Django Rest Framework
- pymongo (MongoDB driver for Python)
## Setup
- Clone the repository:
```bash
https://github.com/Muneeb1030/django_mongo.git
cd django_mongo
```
- Install dependencies:
```bash
pip install -r requirements.txt
```
- Apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
- Run the development server:
```bash
python manage.py runserver
```
- Access the API at `http://localhost:8000/api/`.

## Usage
- **API Endpoints:** Use the custom API endpoints defined in views.py to interact with the data stored in MongoDB.
- **Data Import:** Utilize Django management commands (import_data) to import data into MongoDB from various sources.
- **Task Management:** Monitor and manage Celery tasks via the Django admin interface or command line.
## Contributing
Contributions are welcome! If you have any ideas, bug fixes, or enhancements, please open an issue or submit a pull request on the project's GitHub repository.

## Contact
For any questions or feedback, please email me at muhammadmuneeburrehman.vercel.app
