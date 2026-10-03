"""Command handlers for sessions, agents, plan, web, memory"""
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
console = Console()

def cmd_sessions(action="list", name=None, **kwargs):
    from sessions.manager import SessionManager
    sm = SessionManager()
    if action == "list":
        sessions = sm.list()
        table = Table(title="Sessions")
        table.add_column("Name")
        for s in sessions:
            table.add_column(s) if False else None  # dummy
        # simpler
        table = Table(title="Sessions")
        table.add_column("Name")
        for s in sessions:
            table.add_row(s)
        console.print(table)
    elif action == "create" and name:
        sm.create(name)
        console.print(f"[green]Created session:[/green] {name}")
    elif action == "delete" and name:
        sm.delete(name)
        console.print(f"[red]Deleted session:[/red] {name}")
    else:
        console.print("Usage: sessions <list|create|delete> [name]")
