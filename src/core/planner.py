"""Planning system - plans before acting"""
from typing import List, Dict

class Planner:
    def __init__(self):
        self.tasks: List[Dict] = []
        self.current_task = 0

    def plan(self, goal: str) -> List[Dict]:
        """Create task list from goal"""
        # Basic planning
        tasks = [
            {"id": 1, "content": f"Understand: {goal}", "status": "pending", "priority": "high"},
            {"id": 2, "content": f"Research if needed: {goal}", "status": "pending", "priority": "medium"},
            {"id": 3, "content": f"Execute: {goal}", "status": "pending", "priority": "high"},
            {"id": 4, "content": f"Verify and test", "status": "pending", "priority": "medium"},
        ]
        self.tasks = tasks
        return tasks

    def get_next_task(self):
        for t in self.tasks:
            if t["status"] == "pending":
                t["status"] = "in_progress"
                return t
        return None

    def complete_task(self, task_id: int):
        for t in self.tasks:
            if t["id"] == task_id:
                t["status"] = "completed"
