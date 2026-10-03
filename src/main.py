#!/usr/bin/env python3
"""Mr. Braincells - Smart CLI AI Assistant"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from cli.core import startup_banner
from cli.repl import REPL

def main():
    startup_banner()
    repl = REPL()
    repl.run()

if __name__ == "__main__":
    main()
