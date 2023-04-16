#!/usr/bin/env python
import os
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()


def create_notebooks_dir():
    notebooks_dir = "{{cookiecutter.notebooks_dir}}"
    if notebooks_dir:
        notebooks_dir = Path(notebooks_dir)
        if not notebooks_dir.is_absolute():
            notebooks_dir = PROJECT_DIRECTORY.parent / notebooks_dir

        if not notebooks_dir.is_dir():
            notebooks_dir.mkdir(parents=True)


if __name__ == "__main__":
    create_notebooks_dir()

