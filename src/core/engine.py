"""Main engine - coordinates everything"""
from core.reasoner import Reasoner
from core.planner import Planner
from core.fallback import Fallback
from agents.manager import MultiAgentManager
from memory.manager import MemoryManager
from sessions.manager import SessionManager
from tools.web import WebSearcher

class BrainEngine:
    def __init__(self):
        self.reasoner = Reasoner()
        self.planner = Planner()
        self.fallback = Fallback()
        self.agents = MultiAgentManager()
        self.memory = MemoryManager()
        self.sessions = SessionManager()
        self.web = WebSearcher()

    def process(self, query: str):
        # Think like human first
        thought = self.reasoner.think(query)
        self.memory.add(f"Query: {query}")

        # Plan before acting
        tasks = self.planner.plan(query)
        self.memory.add(f"Planned {len(tasks)} tasks")

        # Check fallback - research if needed
        if self.fallback.needs_research(query):
            results = self.web.search(query)
            self.memory.add(f"Web search conducted")

        # Deploy agents if multi-step
        for task in tasks:
            if "agent" in task["content"].lower() or len(tasks) > 3:
                agent = self.agents.deploy_agent("general", task["content"])
                self.memory.add(f"Deployed {agent.name}")

        return {
            "thought": thought,
            "tasks": tasks,
            "agents": self.agents.get_agents()
        }
