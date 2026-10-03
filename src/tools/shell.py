"""Shell command executor - can run any command as requested"""
import subprocess
import os
from typing import Dict

class ShellExecutor:
    def __init__(self):
        self.safe_mode = False  # As requested - can do anything without constraint (user wants it abliterated/unconstrained)

    def run(self, cmd: str, cwd: str = None) -> Dict:
        try:
            result = subprocess.run(
                cmd,
                shell=True,
                cwd=cwd or os.getcwd(),
                capture_output=True,
                text=True,
                timeout=120
            )
            return {
                "success": result.returncode == 0,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode
            }
        except subprocess.TimeoutExpired:
            return {"success": False, "error": "Command timed out"}
        except Exception as e:
            return {"success": False, "error": str(e)}
