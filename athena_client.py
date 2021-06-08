import requests
import config


class HelloAPI:
    def get_request(self):
        return requests.get("%s:%d/hello" % (config.DOMAIN, config.PORT))

    def post_request(self, data):
        return requests.post("%s/hello" % config.DOMAIN,
                             data=data)


class SquareAPI:
    def get_square(self, num):
        return requests.get("%s:%d/square/%d" % (config.DOMAIN, config.PORT, num))


class TodoAPI:
    url = "%s:%d/" % (config.DOMAIN, config.PORT)

    def get_task(self, task_id):
        return requests.get(TodoAPI.url + 'todo/' + task_id)

    def put_task(self, task_id, task):
        return requests.put(TodoAPI.url + 'todo/' + task_id, data={"data": task})

    def delete_task(self, task_id):
        response = requests.delete(TodoAPI.url + 'todo/' + task_id)
