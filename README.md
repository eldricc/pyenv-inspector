# pyenv-inspector

`pyenv-inspector` is a Python tool for inspecting and visualizing Python environments. It provides a command-line interface (CLI) to gather useful information about your Python setup, list installed packages, visualize the dependency tree, search for specific packages, and export package information in multiple formats.

## Features

- Display Python environment information (Python version, executable, platform, virtual environment status, etc.)
- List installed packages with versions
- Show the dependency tree of installed packages
- Search for a package by name
- Export package list in JSON or `requirements.txt` format

## Installation

You can install the required dependencies using `pip`:

```bash
pip install rich pipdeptree
```

## Usage

### 1. Show Python environment information

```bash
pyenv-inspector info
```

Displays information about the current Python environment, including the Python executable, version, platform, virtual environment, and site-packages.

### 2. List installed packages

```bash
pyenv-inspector list
```

Lists all installed packages and their versions. You can also output the result as JSON:

```bash
pyenv-inspector list --json
```

### 3. Show the dependency tree

```bash
pyenv-inspector tree
```

Shows a visual representation of the dependency tree for installed packages. Output can also be in JSON format:

```bash
pyenv-inspector tree --json
```

### 4. Search for a package

```bash
pyenv-inspector search <package-name>
```

Searches for a specific package by name and displays the results.

### 5. Export the package list

```bash
pyenv-inspector export --format json --output <file-path>
```

Exports the installed packages list in JSON format.

```bash
pyenv-inspector export --format requirements --output <file-path>
```

Exports the installed packages list in `requirements.txt` format.

### License

MIT License

[Source Code](https://github.com/BaseMax/pyenv-inspector)

© Copyright 2025, Max Base
