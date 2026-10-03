"""Smart model selector - choose best AI for the task"""
import httpx

class ModelSelector:
    def __init__(self):
        self.models = {
            "code": ["deepseek-coder", "codellama", "codegemma"],
            "reasoning": ["mistral", "llama3.2", "phi"],
            "fast": ["llama3.2", "phi"],
            "general": ["mistral", "llama3.2", "cogito"]
        }

    def select(self, task_type="general"):
        # Pick best available
        return self.models.get(task_type, self.models["general"])[0]
