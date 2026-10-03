"""Core CLI engine"""
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
console = Console()

def startup_banner():
    banner = Panel.fit(
        "[bold cyan]Mr. Braincells[/bold cyan]\n"
        "[dim]Smart CLI AI • Local-first • Multi-agent[/dim]",
        border_style="cyan"
    )
    console.print(banner)
