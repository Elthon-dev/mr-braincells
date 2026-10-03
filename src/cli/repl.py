"""Interactive REPL with aesthetic UI"""
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
import sys

console = Console()

style = Style.from_dict({
    'prompt': '#00FFFF',
})

class REPL:
    def __init__(self):
        try:
            self.session = PromptSession()
        except Exception:
            self.session = None

    def run(self):
        console.print(Panel("Mr. Braincells CLI Ready", style="bold cyan"))
        if self.session is None:
            print("Non-interactive mode. Exiting.")
            return
        while True:
            try:
                cmd = self.session.prompt("mr-braincells> ", style=style)
                if cmd.lower() in ('exit', 'quit', 'q'):
                    break
                elif cmd.lower() == 'help':
                    self.show_help()
                elif cmd:
                    console.print(f"[dim]Thinking... (human-like step)[/dim]")
                    console.print(f"[green]→[/green] {cmd}")
            except (KeyboardInterrupt, EOFError):
                break
            except Exception as e:
                console.print(f"[red]Error:[/red] {e}")

    def show_help(self):
        help_text = """
[bold]Commands:[/bold]
  help           Show this help
  sessions       Manage sessions (create/delete/select/list)
  agents         Show deployed agents
  plan           Plan a task
  web            Search web
  memory         View memory
  exit/quit      Exit
        """
        console.print(Panel(help_text, title="Help"))
