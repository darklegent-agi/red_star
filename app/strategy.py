"""Planning and forecasting module (skeleton)."""

import datetime


class StrategyPlanner:
    def generate_plan(self, horizon_days: int) -> dict:
        """Return a dummy plan for the given horizon."""
        today = datetime.date.today()
        return {
            'start': today.isoformat(),
            'end': (today + datetime.timedelta(days=horizon_days)).isoformat(),
            'tasks': []
        }
