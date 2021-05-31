import requests


print(requests.get("http://127.0.0.1:5001/greet/Alice").text)
print(requests.get("http://127.0.0.1:5001/").text)
print(requests.get("http://127.0.0.1:5001/square/8").text)
requests.put("http://127.0.0.1:5001/todo/todo_1", data={"data": "Buy groceries"})
print(requests.get("http://127.0.0.1:5001/todo/todo_1").text)
print(requests.get("http://127.0.0.1:5001/todo/todo_2").text)
requests.put("http://127.0.0.1:5001/todo/todo_2", data={"data": "Remember milk"})
print(requests.get("http://127.0.0.1:5001/todo/todo_2").text)

