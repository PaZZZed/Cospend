# 53650 SECI5 Final Project Cospend

## Group members
53650 - José SAAD. 

## Cospend

For the SECI5 Course, the goal of this project is to implement a secure client / server system handling the common expenses of a group of users. Considering the main aspect of this project is security, appropriate techniques have to be used, whether they have been covered in class or not.

I've choses to implement the project using Python and Django as framework.


## What This Git Repository Contains

This section outlines the contents of the repository, providing a brief description of each file and directory.

### Root Directory
- `.gitignore`: Specifies intentionally untracked files to ignore.
- `README.md`: This file, containing information about the project and repository.

### Cospend Directory
- `cospend_Server/`: Contains the server configuration for the Cospend application.
  - `__init__.py`: Initializes the Python package.
  - `asgi.py`: ASGI configuration for the Django project.
  - `settings.py`: Settings/configuration for the Django project.
  - `urls.py`: URL declarations for the Django project.
  - `wsgi.py`: WSGI configuration for deployment.

### Expense Manager Application
- `expense_manager/`: The main application directory for managing expenses.
  - `management/`: Contains management and utility scripts.
    - `seed_users.py`: Script for seeding the database with initial user data.
  - `migration/`: Database migration files.
    - `0001_initial.py`: Initial database migration.
    - `__init__.py`: Initializes the Python package.
  - `static/`: Static files like CSS, JavaScript, and images.
    - `expense_manager/`: Specific static files for the expense manager.
      - `js/`: JavaScript files.
        - `cospend.png`: Image file for the application.
        - `style.css`: CSS file for styling the application.
  - `templates/`: HTML templates for the application views.
    - `expense_manager/`: Templates specific to expense management.
      - `home.html`: Home page template.
      - `create_expense.html`: Template for creating a new expense.
      - `consult_expense.html`: Template for consulting expenses.
      - `edit_group.html`: Template for editing groups.
      - `info.html`: Information page template.
      - `manage_expense.html`: Template for managing expenses.
      - `manage_group.html`: Template for managing groups.
      - `register.html`: User registration template.
    - `registration/`: Templates for user registration.
      - `register.html`: User registration template.
  - `__init__.py`: Initializes the Python package.
  - `admin.py`: Configuration for admin interface.
  - `apps.py`: Application configuration.
  - `forms.py`: Form definitions for the application.
  - `models.py`: Database model definitions.
  - `tests.py`: Test suite for the application.
  - `urls.py`: URL declarations for the application.
  - `views.py`: View definitions for the application.

### Global Templates
- `templates/`: Contains global templates.
  - `_base.html`: Base template for the application.

### `Cospend/db.sqlite3`
The SQLite database file for the project.

### `Cospend/manage.py`
A command-line utility for administrative tasks.

---

## Build the Project



### On an x64 Ubuntu 22.04 Distribution

To build the project on an x64 Ubuntu 22.04 distribution, follow these steps:

1. **Update Your System**

   Before proceeding, ensure your system is up to date. This can be done by running:

   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. **Install Python and Pip**

   Ubuntu 22.04 comes with Python pre-installed. However, you may need to install pip, Python's package manager. Execute the following command:

   ```bash
   sudo apt install python3-pip -y
   ```

3. **Set Up a Virtual Environment**

   It's recommended to use a virtual environment to manage the project dependencies. Install and activate a virtual environment using:

   ```bash
   pip3 install virtualenv
   python3 -m virtualenv venv
   source venv/bin/activate
   ```

4. **Install Required Packages**

   With the virtual environment activated, install the necessary Python packages using pip:

   ```bash
   pip install django
   pip install django_extensions
   pip install Werkzeug
   pip install pyOpenSSL
   ```

5. **Run the Development Server with SSL**

   To run the Django development server with SSL, use the following command:

   ```bash
   python manage.py runserver_plus --cert-file cert.pem --key-file key.pem
   ```

   Make sure you have the `cert.pem` and `key.pem` files in your project directory. If you don't have them, you can generate these files using tools like OpenSSL. (je dois check si c'est une bonne idée de mettre ca dans un git les clés, je dirai que non mais je checkerai une derniere fois quand meme ?? )

---


Run the shell script file with the following command:

```bash
./setup_and_run_django.sh
```

This command assumes that the script `setup_and_run_django.sh` is located in the current directory and has already been made executable. If the script is not executable, you will need to run `chmod +x setup_and_run_django.sh` first.


### On a x64 Windows 10 Machine

To build the project on a x64 Windows 10 machine, follow these steps:

1. **Install Python and Pip**

   If Python is not already installed on your Windows machine, download and install it from the [official Python website](https://www.python.org/downloads/windows/). During installation, ensure that you check the option to add Python to your PATH.

2. **Set Up a Virtual Environment**

   Windows 10 has a different command for activating virtual environments. After installing virtualenv, create and activate a virtual environment using:

   ```cmd
   pip install virtualenv
   python -m virtualenv venv
   .\venv\Scripts\activate
   ```

   This activates the virtual environment. Your command prompt should now include `(venv)` at the beginning of the line.

3. **Install Required Packages**

   With the virtual environment activated, install the necessary Python packages using pip:

   ```cmd
   pip install django
   pip install django_extensions
   pip install Werkzeug
   pip install pyOpenSSL
   ```

4. **Run the Development Server with SSL**

   Running the Django development server with SSL on Windows follows a similar command as on Ubuntu. Use the following command:

   ```cmd
   python manage.py runserver_plus --cert-file cert.pem --key-file key.pem
   ```

   Ensure that the `cert.pem` and `key.pem` files are located in your project directory. If these files are not present, you can generate them using OpenSSL or similar tools available for Windows.

---

## How to run the project 
Go to cospend directory, 
then enter  
```cmd
chmod +x setup_and_run_django.sh
 ```
Then the server has started, so connect yourself to https://127.0.0.1:8000/


## Project implementations

• The server uses a self-signed certificat. 
• The project uses Django as framework.
• The project achieves end-to-end encryption.
