# pyenv-inspector 🐍🔍

![GitHub release](https://img.shields.io/github/release/eldricc/pyenv-inspector.svg?style=flat-square)

Welcome to **pyenv-inspector**, a tool designed to help you visualize and debug your Python virtual environments, packages, and dependencies. Whether you're a beginner or an experienced developer, this tool simplifies the management of your Python environments, making it easier to understand and troubleshoot your projects.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Understanding Output](#understanding-output)
- [Contributing](#contributing)
- [License](#license)
- [Links](#links)

## Features

- **Visualize Environments**: Get a clear view of your Python virtual environments.
- **Package Management**: Easily list installed packages and their versions.
- **Dependency Tracking**: Understand the dependencies of your packages.
- **Environment Variables**: Inspect environment variables affecting your Python projects.

## Installation

To get started with **pyenv-inspector**, download the latest release from the [Releases section](https://github.com/eldricc/pyenv-inspector/releases). Once downloaded, follow the instructions to execute the tool.

### Requirements

- Python 3.x
- pyenv installed on your system

## Usage

After installing, you can run **pyenv-inspector** from your command line. It provides various commands to help you inspect your Python environments.

### Basic Command

```bash
pyenv-inspector
```

This command will display a summary of your current Python environment.

## Commands

### List Environments

To list all your Python virtual environments, use:

```bash
pyenv-inspector list
```

### Show Packages

To see the installed packages in the current environment, run:

```bash
pyenv-inspector packages
```

### Show Dependencies

To view the dependencies of a specific package, use:

```bash
pyenv-inspector dependencies <package_name>
```

### Environment Variables

To inspect the environment variables affecting your Python project, run:

```bash
pyenv-inspector env
```

## Understanding Output

The output of **pyenv-inspector** is designed to be straightforward. Each command will provide clear information about your Python environments, packages, and dependencies.

- **Environments**: Displays the name and path of each virtual environment.
- **Packages**: Lists the installed packages along with their versions.
- **Dependencies**: Shows which packages depend on others, helping you identify potential issues.

## Contributing

We welcome contributions to **pyenv-inspector**. If you want to help improve the tool, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push to your branch.
5. Create a pull request.

Please ensure your code follows the project's coding style and includes tests where applicable.

## License

**pyenv-inspector** is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Links

For more information, visit the [Releases section](https://github.com/eldricc/pyenv-inspector/releases) to download the latest version. You can also check the [GitHub repository](https://github.com/eldricc/pyenv-inspector) for updates and documentation.

---

Thank you for using **pyenv-inspector**! We hope this tool makes managing your Python environments easier and more efficient. If you have any questions or feedback, feel free to reach out. Happy coding!