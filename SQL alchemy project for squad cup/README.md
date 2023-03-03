## Student Lookup App

This is a Flask-based application that allows you to lookup student records by ID or get a list of all students in the database. This project is designed to give you hands-on experience in developing a simple Flask application using SQLAlchemy ORM to interact with a SQLite database.

## Installation

Clone this repository to your local machine.
Install the required dependencies by running pip install -r requirements.txt.
Run the application using the command python app.py.

## Usage

Once the application is running, you can access it by visiting http://localhost:5000/ in your web browser. This will take you to the homepage where you can enter a student ID to look up or click the "Get all students" button to retrieve a list of all students in the database.

To seed the database with some sample data, you can click the "Seed students" button on the homepage. This will add three sample students to the database.

## Code structure

The main code for this application is contained in the app.py file, which defines the Flask application and its various routes. The models.py file contains the definition of the Student model used to interact with the database using SQLAlchemy ORM.

# The following routes are available in the application:

/: The homepage of the application.

/seed_db: A route to seed the database with sample student data.

/get_all_students: A route to retrieve a list of all students in the database.

/students: A route to retrieve a student record by ID or add a new student record to the database.


# Task

Your task is to complete the code for the /get_all_students and /students routes. 

In the /get_all_students route, you should retrieve all students from the database and return them as a JSON response. 

In the /students route, you should implement logic to retrieve a student record by ID or add a new student record to the database, depending on the HTTP method used (GET or POST).

Feel free to modify the code structure and/or add additional functionality to the application as you see fit. Good luck!