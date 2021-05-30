# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

tasks = {}


@app.route('/tasks/<task_id>', methods=['GET', 'POST', 'DEgit add --all'
                                                       'LETE'])
def daily_tasks(task_id):
    if request.method == 'POST':
        tasks[task_id] = request.form['data']
        return {task_id: tasks[task_id]}
    elif request.method == 'DELETE':
        if task_id in tasks:
            del tasks[task_id]
            return "%s has been removed!!!" % task_id
        else:
            return "%s is not available to be deleted" % task_id
    else:
        if task_id in tasks:
            return {task_id: tasks[task_id]}
        else:
            return "%s is not available." % task_id


# driver function
if __name__ == '__main__':
    app.run(debug=True)
