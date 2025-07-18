"""Task management module (skeleton)."""

from flask import g
from bson.objectid import ObjectId


def create_task(name: str, deadline: str) -> str:
    col = g.db.tasks
    result = col.insert_one({'name': name, 'deadline': deadline, 'done': False})
    return str(result.inserted_id)


def list_tasks() -> list:
    col = g.db.tasks
    return [{'id': str(t['_id']), 'name': t['name'], 'deadline': t['deadline'], 'done': t['done']} for t in col.find()]
