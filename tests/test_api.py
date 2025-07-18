import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app

def test_health_check():
    app = create_app()
    with app.test_client() as client:
        res = client.get('/')
        assert res.status_code == 200
        assert res.get_json() == {'status': 'ok'}
