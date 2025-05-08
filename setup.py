from setuptools import setup, find_packages

setup(
    name="pyenv-inspector",
    version="0.1.0",
    description="A Python environment inspection tool to visualize and debug Python environments",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Max Base",
    author_email="maxbasecode@gmail.com",
    url="https://github.com/BaseMax/pyenv-inspector",
    packages=find_packages(),
    install_requires=[
        "rich>=10.0.0",
        "pipdeptree>=2.0.0",
    ],
    entry_points={
        "console_scripts": [
            "pyenv-inspector=pyenv_inspector.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    license="MIT",
    keywords="python environment inspector packages pip",
)
