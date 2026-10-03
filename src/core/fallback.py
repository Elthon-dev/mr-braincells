"""Fallback system - when uncertain, research"""
class Fallback:
    def __init__(self):
        self.enabled = True

    def needs_research(self, query: str, knowledge: Dict = None) -> bool:
        keywords = ["unknown", "how to", "latest", "current", "research", "find", "search"]
        if any(k in query.lower() for k in keywords):
            return True
        return False
