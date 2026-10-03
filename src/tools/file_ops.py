"""File operations - edit, create, modify files"""
import os
from pathlib import Path
from typing import Dict

class FileOps:
    def __init__(self):
        pass

    def read(self, path: str) -> Dict:
        try:
            p = Path(path)
            if p.is_dir():
                return {"content": "\n".join(str(x) for x in p.iterdir())}
            with open(p, 'r', encoding='utf-8', errors='ignore') as f:
                return {"content": f.read()}
        except Exception as e:
            return {"error": str(e)}

    def write(self, path: str, content: str) -> Dict:
        try:
            p = Path(path)
            p.parent.mkdir(parents=True, exist_ok=True)
            with open(p, 'w', encoding='utf-8') as f:
                f.write(content)
            return {"success": True, "path": str(p)}
        except Exception as e:
            return {"error": str(e)}

    def edit(self, path: str, old: str, new: str) -> Dict:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            if old not in content:
                return {"error": "old string not found"}
            content = content.replace(old, new)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            return {"success": True}
        except Exception as e:
            return {"error": str(e)}
