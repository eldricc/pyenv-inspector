#!/usr/bin/env python3

import sys
import os
import json
import argparse
import platform
import subprocess
import site
from typing import Optional

from rich.console import Console
from rich.table import Table
from rich.tree import Tree

console = Console()

# --------------------------
# Core Info & Utilities
# --------------------------
def get_env_info():
    return {
        "Python Executable": sys.executable,
        "Python Version": platform.python_version(),
        "Platform": platform.platform(),
        "Virtual Environment": os.environ.get("VIRTUAL_ENV", "Not detected"),
        "Base Prefix": sys.base_prefix,
        "Prefix": sys.prefix,
        "Site-Packages": ", ".join(site.getsitepackages()),
    }

def is_venv():
    return sys.prefix != sys.base_prefix or "VIRTUAL_ENV" in os.environ

def run_pip_list():
    result = subprocess.run([sys.executable, "-m", "pip", "list", "--format", "json"], capture_output=True, text=True)
    if result.returncode != 0:
        console.print("[red]Failed to get pip list[/red]")
        sys.exit(1)
    return json.loads(result.stdout)

# --------------------------
# Display Functions
# --------------------------
def show_env_info(json_output=False):
    info = get_env_info()
    if json_output:
        print(json.dumps(info, indent=2))
    else:
        table = Table(title="Environment Info")
        table.add_column("Key", style="cyan")
        table.add_column("Value", style="magenta")
        for key, val in info.items():
            table.add_row(key, val)
        console.print(table)

def show_package_list(json_output=False):
    packages = run_pip_list()
    if json_output:
        print(json.dumps(packages, indent=2))
    else:
        table = Table(title="Installed Packages")
        table.add_column("Package", style="green")
        table.add_column("Version", style="blue")
        for pkg in packages:
            table.add_row(pkg["name"], pkg["version"])
        console.print(table)

def show_dependency_tree(json_output=False):
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pipdeptree", "--json"],
            capture_output=True,
            text=True,
            check=True
        )
        tree_data = json.loads(result.stdout)

        if json_output:
            print(json.dumps(tree_data, indent=2))
            return

        pkg_map = {pkg["package"]["key"]: pkg for pkg in tree_data}
        visited = set()
        root = Tree("Dependency Tree")

        def add_node(pkg_key, parent):
            if pkg_key in visited:
                return
            visited.add(pkg_key)
            pkg = pkg_map.get(pkg_key)
            if not pkg:
                return
            name = pkg["package"]["key"]
            version = pkg["package"]["installed_version"]
            node = parent.add(f"{name} [dim]({version})[/dim]")
            for dep in pkg["dependencies"]:
                add_node(dep["key"], node)

        for pkg_key in pkg_map:
            add_node(pkg_key, root)

        console.print(root)

    except subprocess.CalledProcessError as e:
        console.print(f"[red]Failed to run pipdeptree: {e}[/red]")
        sys.exit(1)

def search_package(name: str):
    packages = run_pip_list()
    results = [pkg for pkg in packages if name.lower() in pkg["name"].lower()]
    if results:
        table = Table(title=f"Search results for '{name}'")
        table.add_column("Package")
        table.add_column("Version")
        for pkg in results:
            table.add_row(pkg["name"], pkg["version"])
        console.print(table)
    else:
        console.print(f"[yellow]No package matching '{name}' found.[/yellow]")

def export_packages(format: str, output_file: Optional[str]):
    packages = run_pip_list()
    if format == "json":
        with open(output_file, "w") as f:
            json.dump(packages, f, indent=2)
        console.print(f"[green]Exported packages to {output_file}[/green]")
    elif format == "requirements":
        with open(output_file, "w") as f:
            for pkg in packages:
                f.write(f"{pkg['name']}=={pkg['version']}\n")
        console.print(f"[green]Exported requirements.txt to {output_file}[/green]")
    else:
        console.print("[red]Invalid export format. Use 'json' or 'requirements'.[/red]")

# --------------------------
# Argument Parsing
# --------------------------
def main():
    parser = argparse.ArgumentParser(
        description="🔍 pyenv-inspector — Visualize and debug Python environments"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("info", help="Show Python environment information")

    list_parser = subparsers.add_parser("list", help="List installed packages")
    list_parser.add_argument("--json", action="store_true", help="Output as JSON")

    tree_parser = subparsers.add_parser("tree", help="Show dependency tree")
    tree_parser.add_argument("--json", action="store_true", help="Output as JSON")

    search_parser = subparsers.add_parser("search", help="Search for a package")
    search_parser.add_argument("name", help="Name to search for")

    export_parser = subparsers.add_parser("export", help="Export package list")
    export_parser.add_argument("--format", choices=["json", "requirements"], default="json")
    export_parser.add_argument("--output", required=True, help="Output file path")

    args = parser.parse_args()

    if args.command == "info":
        show_env_info()
    elif args.command == "list":
        show_package_list(json_output=args.json)
    elif args.command == "tree":
        show_dependency_tree(json_output=args.json)
    elif args.command == "search":
        search_package(args.name)
    elif args.command == "export":
        export_packages(args.format, args.output)

if __name__ == "__main__":
    main()
