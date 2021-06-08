from flask_restful import Resource
from flask import request


tasks = {}


class DailyTasks(Resource):
    def get(self, task_id):
        if task_id in tasks:
            return {task_id: tasks[task_id]}
        else:
            return "%s is not available." % task_id

    def post(self, task_id):
        tasks[task_id] = request.form['data']
        return {task_id: tasks[task_id]}

    def delete(self, task_id):
        if task_id in tasks:
            del tasks[task_id]
            return "%s has been removed!!!" % task_id
        else:
            return "%s is not available to be deleted" % task_id
