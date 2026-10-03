"""LLM interface for Ollama"""
import httpx
import json

class OllamaLLM:
    def __init__(self, model="llama3.2", base_url="http://localhost:11434"):
        self.model = model
        self.base_url = base_url
        self.api_url = f"{base_url}/api/generate"

    def generate(self, prompt: str, system: str = None) -> str:
        try:
            payload = {
                "model": self.model,
                "prompt": prompt,
                "stream": False,
                "options": {"temperature": 0.7, "top_p": 0.9}
            }
            if system:
                payload["system"] = system
            with httpx.Client(timeout=120) as client:
                resp = client.post(self.api_url, json=payload)
                if resp.status_code == 200:
                    data = resp.json()
                    return data.get("response", "").strip()
                return f"Error: {resp.status_code}"
        except Exception as e:
            return f"Error: {str(e)}"

    def is_available(self) -> bool:
        try:
            with httpx.Client(timeout=5) as client:
                resp = client.get(f"{self.base_url}/api/tags")
                return resp.status_code == 200
        except:
            return False
