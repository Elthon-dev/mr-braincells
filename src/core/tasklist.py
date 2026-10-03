"""Task list with sequence tracking - list, update, track"""
from typing import List, Dict
import json

class TaskList:
    def __init__(self):
        self.tasks: List[Dict] = []

    def add(self, content: str, priority="medium"):
        self.tasks.append({
            "id": len(self.tasks) + 1,
            "content": content,
            "status": "pending",
            "priority": priority
        })

    def update(self, task_id: int, status: str):
        for t in self.tasks:
            if t["id"] == task_id:
                t["status"] = status
                return t
        return None

    def complete_current(self):
        for t in self.tasks:
            if t["status"] == "in_progress":
                t["status"] = "completed"
                break

    def get_current(self):
        for t in self.tasks:
            if t["status"] == "in_progress":
                return t
        # start next pending
        for t in self.tasks:
            if t["status"] == "pending":
                t["status"] = "in_progress"
                return t
        return None

    def list_all(self) -> List[Dict]:
        return self.tasks

    def to_json(self):
        return json.dumps(self.tasks, indent=2)
