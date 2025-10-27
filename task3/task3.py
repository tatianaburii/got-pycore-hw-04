#!/usr/bin/env python3
import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)
INDENT = "  "

def print_directory_contents(directory: Path, level: int = 0) -> None:
    if not directory.is_dir():
        print(Fore.RED + f"Error: {directory} is not a directory")
        return

    print(Fore.YELLOW + f"{INDENT * level}{directory.name}/")

    try:
        items = sorted(directory.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
    except Exception as e:
        print(Fore.RED + f"{INDENT * (level + 1)}Error accessing: {e}")
        return

    for p in items:
        if p.is_dir():
            print_directory_contents(p, level + 1)
        else:
            print(Fore.CYAN + f"{INDENT * (level + 1)}{p.name}")

def main() -> int:
    if len(sys.argv) < 2:
        print(Fore.RED + "Error: missing path argument")
        return 2
    root = Path(sys.argv[1]).expanduser().resolve()
    if not root.exists():
        print(Fore.RED + f"Error: path does not exist: {root}"); return 1
    if not root.is_dir():
        print(Fore.RED + f"Error: not a directory: {root}"); return 1
    print_directory_contents(root)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

