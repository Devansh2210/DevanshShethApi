from flask import Flask, request, jsonify

app = Flask(__name__)
students = [
    {'id': 1, 'name': 'Devansh', 'CGPA': 80},
    {'id': 2, 'name': 'Vinit', 'CGPA': 97},
    {'id': 3, 'name': 'Sonu', 'CGPA': 60}
]


# [GET REQUEST]
@app.route('/students/<int:student_id>', methods = ['GET'])
def read_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        return jsonify({'error': 'Student not found'}), 
    return jsonify({'info': f'Student: listed', 'data': student}), 

# [GET REQUEST]
@app.route('/students', methods = ['GET'])
def get_students():
    return jsonify({'info': 'All students', 'data': students}), 

# [POST REQUEST]
@app.route('/students', methods = ['POST'])
def create_student():
    data = request.get_json()
    student = {
        'id': data['id'],
        'name': data['name'],
        'grade': data['grade']
    }
    students.append(student)
    return jsonify({'info': 'New student added', 'data': student}), 

# Delete a student by ID 
@app.route('/students/<int:student_id>', methods = ['DELETE'])
def delete_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        return jsonify({'error': 'Student not found'}), 
    students.remove(student)
    return jsonify({'info': f'Student: {student_id} is deleted', 'data': student}), 

# Update a student by ID 
@app.route('/students/<int:student_id>', methods = ['PUT'])
def update_student(student_id):
    data = request.get_json()
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        return jsonify({'error': 'Student not found'}), 
    student.update(data)
    return jsonify({'info': f'Student: list updated', 'data': student}), 



if __name__ == '__main__':
    app.run(debug = False)