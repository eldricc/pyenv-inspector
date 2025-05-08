#!/usr/bin/env python3

import sys
import os
import argparse
import platform
import subprocess

try:
    from pipdeptree import get_installed_distributions, build_dist_index, construct_tree
    from rich.console import Console
    from rich.tree import Tree
    from rich.table import Table
except ImportError:
    print("Required packages not found. Run: pip install rich pipdeptree")
    sys.exit(1)

console = Console()

def get_python_info():
    return {
        "Python Executable": sys.executable,
        "Python Version": platform.python_version(),
        "Platform": platform.platform(),
        "Virtual Env": os.environ.get("VIRTUAL_ENV", "Not in a virtual environment")
    }

def display_env_info():
    info = get_python_info()
    table = Table(title="Environment Info")
    table.add_column("Property", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    for key, value in info.items():
        table.add_row(key, value)

    console.print(table)

def display_packages():
    result = subprocess.run([sys.executable, "-m", "pip", "list"], capture_output=True, text=True)
    console.print("[bold yellow]Installed Packages:[/bold yellow]")
    console.print(result.stdout)

def display_dependency_tree():
    console.print("[bold green]Dependency Tree:[/bold green]")
    dists = get_installed_distributions()
    dist_index = build_dist_index(dists)
    tree = construct_tree(dist_index)

    def render_tree(tree, parent):
        for dist, deps in tree.items():
            branch = parent.add(f"[bold]{dist.project_name}[/bold] ({dist.version})")
            render_tree(deps, branch)

    root = Tree("Packages")
    render_tree(tree, root)
    console.print(root)

def main():
    parser = argparse.ArgumentParser(description="pyenv-inspector - Visualize and debug Python environments")
    parser.add_argument("--tree", action="store_true", help="Show dependency tree")
    parser.add_argument("--info", action="store_true", help="Show Python environment info")
    parser.add_argument("--list", action="store_true", help="List installed packages")
    args = parser.parse_args()

    if not any([args.tree, args.info, args.list]):
        args.info = args.list = args.tree = True

    if args.info:
        display_env_info()
    if args.list:
        display_packages()
    if args.tree:
        display_dependency_tree()

if __name__ == "__main__":
    main()
