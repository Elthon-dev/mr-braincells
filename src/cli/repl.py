"""Interactive REPL with aesthetic UI"""
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from core.engine import BrainEngine
from core.llm import OllamaLLM
from core.model_selector import ModelSelector

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
        self.engine = BrainEngine()
        self.llm = OllamaLLM()
        self.selector = ModelSelector()

    def run(self):
        console.print(Panel("Mr. Braincells CLI Ready", style="bold cyan"))
        if self.session is None:
            print("Non-interactive mode.")
            return
        while True:
            try:
                cmd = self.session.prompt("mr-braincells> ", style=style)
                if not cmd or cmd.strip() == '':
                    continue
                if cmd.lower() in ('exit', 'quit', 'q'):
                    break
                elif cmd.lower() == 'help':
                    self.show_help()
                    continue
                elif cmd.lower().startswith('plan '):
                    goal = cmd[5:]
                    tasks = self.engine.planner.plan(goal)
                    from rich.table import Table
                    t = Table(title=f"Plan: {goal}")
                    t.add_column("ID")
                    t.add_column("Task")
                    t.add_column("Status")
                    t.add_column("Priority")
                    for task in tasks:
                        t.add_row(str(task['id']), task['content'], task['status'], task['priority'])
                    console.print(t)
                    continue
                elif cmd.lower().startswith('sessions'):
                    parts = cmd.split()
                    action = parts[1] if len(parts) > 1 else 'list'
                    name = parts[2] if len(parts) > 2 else None
                    from cli.commands import cmd_sessions
                    cmd_sessions(action=action, name=name)
                    continue
                elif cmd.lower() == 'agents':
                    agents = self.engine.agents.get_agents()
                    from rich.table import Table
                    t = Table(title="Deployed Agents")
                    t.add_column("Name")
                    t.add_column("Role")
                    t.add_column("Task")
                    t.add_column("Status")
                    for a in agents:
                        t.add_row(a.name, a.role, a.task, a.status)
                    console.print(t)
                    continue
                elif cmd.lower().startswith('web '):
                    q = cmd[4:]
                    results = self.engine.web.search(q)
                    console.print(results)
                    continue
                elif cmd.lower() == 'memory':
                    console.print("[dim]Memory stored[/dim]")
                    continue

                # Regular chat/query - think first, then respond
                with console.status("[bold cyan]Brain cells firing... thinking like human[/bold cyan]", spinner="dots"):
                    thought = self.engine.reasoner.think(cmd)
                console.print(Panel(f"[yellow]Thinking:[/yellow] {thought['thought']}", title="Step 1: Human-like Thought"))

                # Process with engine
                result = self.engine.process(cmd)

                # Try to get LLM response if Ollama available
                if self.llm.is_available():
                    model = self.selector.select("general")
                    with console.status(f"[bold green]Generating with {model}...[/bold green]", spinner="dots"):
                        response = self.llm.generate(f"User: {cmd}\n\nAnswer helpfully and naturally, be concise but smart.")
                    console.print(Panel(response, title="Mr. Braincells", border_style="green"))
                else:
                    console.print(Panel(f"I processed: {cmd}\n\n[dim]Ollama not running. Start with: ollama serve[/dim]", title="Response", border_style="blue"))

            except (KeyboardInterrupt, EOFError):
                break
            except Exception as e:
                console.print(f"[red]Error:[/red] {e}")

    def show_help(self):
        help_text = """
[bold]Commands:[/bold]
  help           Show this help
  plan <task>    Plan a task
  sessions       Manage sessions (create/delete/select/list)
  agents         Show deployed agents
  web <query>    Search web
  memory         View memory
  exit/quit      Exit

[bold]Chat:[/bold]
  Just type anything to chat with AI
        """
        console.print(Panel(help_text, title="Help"))
