import requests


class GreetAPI:
    def get_request(self, name):
        try:
            response = requests.get("http://127.0.0.1:5001/greet/%s" % name)
        except:
            raise Exception('')
        return response


class HelloAPI:
    def get_request(self):
        return requests.get("http://127.0.0.1:5001/")

    def post_request(self, data):
        return requests.post("http://127.0.0.1:5001/", data=data)


class SquareAPI:
    def get_square(self, num):
        return requests.get("http://127.0.0.1:5001/square/8")


class TodoAPI:
    def get_task(self, task_id):
        return requests.get("http://127.0.0.1:5001/todo/%s" % task_id)

    def put_task(self, task_id, task):
        return requests.put("http://127.0.0.1:5001/todo/%s" % task_id, data={"data": task})

    def delete_task(self, task_id):
        response = requests.delete("http://127.0.0.1:5001/tasks/%s" % task_id)
