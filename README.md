# Personal-Assistant

## Description

This project is a Django-based web application that implements functionality for managing personal data, including contacts, notes, files storage. The application allows user registration, profile management and integration with APIs for data exchange. Key features include:

- User registration and authentication.
- Ability to reset the password.
- API integration for receiving news and exchange rate.
- An authorized user has access to their contact list and notes, has the ability to manage the contact list (create, search, edit, delete, view upcoming birthdays). In notes, can add tags, make a selection by tags. Also user can upload and manage their files.

## Requirements

The project runs on Python 3.10 or higher and uses the following libraries:

- **Django**: 5.1.1
- **psycopg2**: for working with PostgreSQL
- **django-cors-headers**: to handle CORS requests
- **django-crispy-forms**: to improve the appearance of forms
- **cloudinary**: for image storage
- **whitenoise**: for serving static files
- Other libraries specified in `requirements.txt`.

## Installation

### 1. Clone the repository

Copy the project to your local computer:
```bash
git clone https://github.com/A-Lastovets/Personal-Assistant.git
``` 
Go to the root folder

### 2. Create a virtual environment:

python -m venv venv
source venv/bin/activate # For Linux/Mac
venv\Scripts\activate # For Windows

### 3. Install the dependencies:

pip install -r requirements.txt

### **4. Configure the .env file:**
Create an .env file in the root directory of the project and add the necessary environment variables using the sample file .env.sample

### 5. Perform database migrations:
```
python manage.py migrate
```
### 6. Start the server:
```
python manage.py runserver
```
### Using

Once the server is up and running, you can open the web application in your browser at http://127.0.0.1:8000/. You will be able to register, log in, add contacts and notes, and manage your profile.

### Testing

To run the tests, use the command:
```
python manage.py test
```
### License
This project is licensed under the MIT License.

Thank you for using our web application!