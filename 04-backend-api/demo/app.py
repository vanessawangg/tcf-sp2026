"""
Minimal layered REST API demo (Flask) in one file.

Run:
  python3 app.py

Endpoints:
  GET    /tasks
  GET    /tasks/<id>
  POST   /tasks
  PUT    /tasks/<id>
  DELETE /tasks/<id>
"""

from flask import Flask, jsonify, request


# Repository layer: data storage only (in-memory for demo)
class TaskRepository:
    def __init__(self):
        self.tasks = [
            {"id": 1, "title": "Learn what REST is", "done": False},
            {"id": 2, "title": "See API layers in action", "done": False},
        ]
        self.next_id = 3

    def list_all(self):
        return self.tasks

    def get(self, task_id):
        return next((task for task in self.tasks if task["id"] == task_id), None)

    def create(self, title, done=False):
        task = {"id": self.next_id, "title": title, "done": done}
        self.tasks.append(task)
        self.next_id += 1
        return task

    def update(self, task_id, title=None, done=None):
        task = self.get(task_id)
        if not task:
            return None
        if title is not None:
            task["title"] = title
        if done is not None:
            task["done"] = done
        return task

    def delete(self, task_id):
        task = self.get(task_id)
        if not task:
            return False
        self.tasks = [item for item in self.tasks if item["id"] != task_id]
        return True


# Service layer: validation + business rules
class TaskService:
    def __init__(self, repository):
        self.repository = repository

    def list_tasks(self):
        return {"ok": True, "data": self.repository.list_all()}, 200

    def get_task(self, task_id):
        task = self.repository.get(task_id)
        if not task:
            return {"ok": False, "error": "Task not found"}, 404
        return {"ok": True, "data": task}, 200

    def create_task(self, payload):
        title = str(payload.get("title", "")).strip()
        if not title:
            return {"ok": False, "error": "title is required"}, 400

        task = self.repository.create(title=title, done=bool(payload.get("done", False)))
        return {"ok": True, "data": task}, 201

    def update_task(self, task_id, payload):
        title = payload.get("title")
        done = payload.get("done")

        if title is not None and (not isinstance(title, str) or not title.strip()):
            return {"ok": False, "error": "title must be a non-empty string"}, 400

        if done is not None and not isinstance(done, bool):
            return {"ok": False, "error": "done must be true or false"}, 400

        updated = self.repository.update(
            task_id,
            title=title.strip() if isinstance(title, str) else None,
            done=done,
        )
        if not updated:
            return {"ok": False, "error": "Task not found"}, 404

        return {"ok": True, "data": updated}, 200

    def delete_task(self, task_id):
        deleted = self.repository.delete(task_id)
        if not deleted:
            return {"ok": False, "error": "Task not found"}, 404
        return {"ok": True, "data": {"message": "Task deleted"}}, 200


# Controller layer: maps HTTP requests to service methods
class TaskController:
    def __init__(self, service):
        self.service = service

    def list_tasks(self):
        return self.service.list_tasks()

    def get_task(self, task_id):
        return self.service.get_task(task_id)

    def create_task(self, payload):
        return self.service.create_task(payload)

    def update_task(self, task_id, payload):
        return self.service.update_task(task_id, payload)

    def delete_task(self, task_id):
        return self.service.delete_task(task_id)


app = Flask(__name__)

repository = TaskRepository()
service = TaskService(repository)
controller = TaskController(service)


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
    return response


@app.route("/", methods=["GET"])
def home():
    return jsonify(
        {
            "message": "Simple Flask REST API demo is running",
            "routes": [
                "GET /tasks",
                "GET /tasks/<id>",
                "POST /tasks",
                "PUT /tasks/<id>",
                "DELETE /tasks/<id>",
            ],
        }
    )


@app.route("/tasks", methods=["GET"])
def list_tasks():
    body, status = controller.list_tasks()
    return jsonify(body), status


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    body, status = controller.get_task(task_id)
    return jsonify(body), status


@app.route("/tasks", methods=["POST"])
def create_task():
    payload = request.get_json(silent=True)
    if payload is None:
        return jsonify({"ok": False, "error": "Invalid JSON body"}), 400

    body, status = controller.create_task(payload)
    return jsonify(body), status


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    payload = request.get_json(silent=True)
    if payload is None:
        return jsonify({"ok": False, "error": "Invalid JSON body"}), 400

    body, status = controller.update_task(task_id, payload)
    return jsonify(body), status


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    body, status = controller.delete_task(task_id)
    return jsonify(body), status


@app.route("/<path:_>", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
def catch_all(_):
    return jsonify({"ok": False, "error": "Route not found"}), 404


if __name__ == "__main__":
    app.run( port=8000, debug=False)
