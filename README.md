# Mr. Braincells 🤖

The best, smartest while still fast and lightweight AI CLI for Termux. Ready to run locally with Ollama.

## Features

- **Aesthetic UI** - Beautiful terminal interface with rich colors
- **Human-like Thinking** - Thinks step by step before responding
- **Run Any Commands** - Can freely execute shell commands when needed
- **Multi-Agent System** - Deploys mini agents for specific tasks
- **Web Search** - Autonomous web search with fallback/research
- **Memory** - Persistent long-term memory
- **Sessions** - Create, delete, select, manage and run sessions
- **Fallback & Research** - Automatically researches when info is missing
- **Planning** - Plans before acting
- **Task Sequencing** - Tracks, lists and updates task list continuously
- **Smart Model Selection** - Chooses best model per task
- **Local-first** - Runs with Ollama, completely local

## Quick Start

```bash
# Clone
git clone https://github.com/Elthon-dev/mr-braincells
cd mr-braincells

# Termux setup (auto installs everything)
bash setup-termux.sh

# Or manual
pip install -r requirements.txt
./mr-braincells
```

## Usage

```bash
mr-braincells
```

## Connection Credentials

See workflow output or run:
```bash
python3 scripts/print_creds.py
```

## GitHub Workflow

The included workflow sets up Ollama and prints connection credentials at the end as requested.
