# using flask_restful
from flask import Flask
from flask_restful import Api
from resources import daily_tasks, health_check

app = Flask(__name__)
api = Api(app)


@app.route('/')
def home():
    return 'Welcome to Apollo'


api.add_resource(health_check.Health, '/health')
api.add_resource(daily_tasks.DailyTasks, '/tasks/<task_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
