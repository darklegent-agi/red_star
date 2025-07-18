from flask import Blueprint, jsonify, request
from .tasks import create_task, list_tasks
from .strategy import StrategyPlanner

bp = Blueprint('main', __name__)

planner = StrategyPlanner()


@bp.route('/')
def index():
    return jsonify({'status': 'ok'})


@bp.route('/tasks', methods=['POST'])
def add_task():
    """Create a new task."""
    data = request.get_json(silent=True) or {}
    name = data.get('name')
    deadline = data.get('deadline')
    if not name or not deadline:
        return jsonify({'error': 'name and deadline required'}), 400
    task_id = create_task(name, deadline)
    return jsonify({'id': task_id}), 201


@bp.route('/tasks', methods=['GET'])
def get_tasks():
    """List all tasks."""
    return jsonify(list_tasks())


@bp.route('/plan', methods=['POST'])
def generate_plan():
    """Generate a simple plan for the given horizon."""
    data = request.get_json(silent=True) or {}
    horizon = int(data.get('horizon', 7))
    return jsonify(planner.generate_plan(horizon))
