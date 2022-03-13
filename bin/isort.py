#!/usr/bin/env python3
import pathlib

from utils import PROJECT_ROOT, error_handler, gray, print_with_time, red, run


def _isort(path: pathlib.Path) -> None:
    """
    Run isort recursively on provided path. Print error message if path does not exist
    """

    if path.exists():
        with error_handler(description=f"Running isort on: {gray(path)}"):
            run("isort", "--recursive", path)
    else:
        print_with_time(f'{red(f"Unable to run isort on `{path}`. Path not found")}')


def main():
    """
    Run isort on all configured directories
    """

    directories = [
        PROJECT_ROOT / "",
        PROJECT_ROOT / "bin",
        PROJECT_ROOT / "covid19",
        PROJECT_ROOT / "facial_recognition",
        PROJECT_ROOT / "Home",
        PROJECT_ROOT / "man_sim",
        PROJECT_ROOT / "semi_auto",
        PROJECT_ROOT / "simulatorx",
    ]

    for directory in directories:
        _isort(directory.absolute())


if __name__ == "__main__":
    main()
