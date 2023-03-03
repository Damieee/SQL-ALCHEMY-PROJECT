from flask import Flask, jsonify, request, render_template
from models import db, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/")
def index():
    db.create_all()
    return render_template("index.html")

@app.route('/seed_db')
def seed_db():
    try:
        students = [
            {'name': 'Alice', 'email': 'alice@example.com', 'major': 'Computer Science'},
            {'name': 'Bob', 'email': 'bob@example.com', 'major': 'Electrical Engineering'},
            {'name': 'Charlie', 'email': 'charlie@example.com', 'major': 'Mathematics'},
        ]
        for student in students:
            db.session.add(Student(**student))
        db.session.commit()
        return jsonify({'message': 'Database seeded successfully!'})
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)})

@app.route('/get_all_students')
def get_all_students():
    # Write your code here.
    pass

@app.route('/students', methods=["GET", "POST"])
def get_student_by_id():
    # Write your code here.
    pass

if __name__ == '__main__':
 
    app.run(debug=True)
