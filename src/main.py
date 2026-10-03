#!/usr/bin/env python3
"""Mr. Braincells - Smart CLI AI Assistant"""
import sys
import os

# Add src to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from cli.core import startup_banner
except ImportError:
    def startup_banner():
        print("Mr. Braincells - Brain: Online")

def main():
    startup_banner()
    print("\nType 'help' for commands, 'exit' to quit")

if __name__ == "__main__":
    main()
