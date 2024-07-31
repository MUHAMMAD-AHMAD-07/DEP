from flask import Flask, jsonify, request

app = Flask(__name__)

# Example tasks
task_list = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Find a good Python tutorial online',
        'done': False
    }
]

@app.route('/tasks', methods=['GET'])
def fetch_tasks():
    return jsonify({'tasks': task_list})

@app.route('/tasks/<int:task_id>', methods=['GET'])
def fetch_task(task_id):
    task = next((t for t in task_list if t['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify({'task': task})

@app.route('/tasks', methods=['POST'])
def add_task():
    if not request.json or 'title' not in request.json:
        return jsonify({'error': 'Invalid request'}), 400
    new_task = {
        'id': task_list[-1]['id'] + 1 if task_list else 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    task_list.append(new_task)
    return jsonify({'task': new_task}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def modify_task(task_id):
    task = next((t for t in task_list if t['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    if not request.json:
        return jsonify({'error': 'Invalid request'}), 400

    task['title'] = request.json.get('title', task['title'])
    task['description'] = request.json.get('description', task['description'])
    task['done'] = request.json.get('done', task['done'])
    return jsonify({'task': task})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def remove_task(task_id):
    task = next((t for t in task_list if t['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    task_list.remove(task)
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
