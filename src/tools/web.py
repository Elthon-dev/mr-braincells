"""Web search feature - can search web autonomously"""
import httpx
from typing import List, Dict

class WebSearcher:
    def __init__(self):
        self.enabled = True

    def search(self, query: str, max_results: int = 5) -> List[Dict]:
        """Search web - falls back gracefully if no API key"""
        try:
            # Try DuckDuckGo instant answer API (no key needed)
            url = "https://api.duckduckgo.com/"
            params = {"q": query, "format": "json", "no_redirect": 1, "no_html": 1}
            with httpx.Client(timeout=10) as client:
                resp = client.get(url, params=params)
                data = resp.json()
                results = []
                if data.get("Abstract"):
                    results.append({"title": query, "snippet": data["Abstract"], "url": data.get("AbstractURL")})
                return results
        except Exception as e:
            return [{"error": f"Search failed: {str(e)}"}]
