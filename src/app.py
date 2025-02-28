from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configuración de la base de datos desde variables de entorno
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/mydatabase")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Modelo de base de datos
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    career = db.Column(db.String(100), nullable=False)

# Crear la base de datos
with app.app_context():
    db.create_all()

# Endpoint para obtener todos los estudiantes
@app.route("/students", methods=["GET"])
def get_students():
    students = Student.query.all()
    return jsonify([{"id": s.id, "name": s.name, "age": s.age, "career": s.career} for s in students])

# Endpoint para obtener un estudiante por su ID
@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify({"id": student.id, "name": student.name, "age": student.age, "career": student.career})

# Endpoint para agregar un estudiante
@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()
    new_student = Student(name=data["name"], age=data["age"], career=data["career"])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"message": "Student added successfully"}), 201

# Endpoint para actualizar un estudiante por su ID
@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.get_json()

    # Actualizar los campos del estudiante
    student.name = data.get("name", student.name)
    student.age = data.get("age", student.age)
    student.career = data.get("career", student.career)

    db.session.commit()
    return jsonify({"message": "Student updated successfully"})

# Endpoint para eliminar un estudiante por su ID
@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student deleted successfully"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)