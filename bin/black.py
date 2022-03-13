#!/usr/bin/env python3
import pathlib
from typing import cast

from utils import PROJECT_ROOT, error_handler, gray, print_with_time, red, run


def _black(path: pathlib.Path) -> None:
    """
    Run black on all files in provided path. Print error message if path does not exist
    """

    if path.exists():
        with error_handler(description=f"Running black on {gray(path)}"):
            run("black", path)
    else:
        print_with_time(f'{red(f"Unable to run black on `{path}`. Not found")}')


def main() -> None:
    """
    Run black on all configured directories and bin scripts
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
        _black(directory.absolute())

    script_root = pathlib.Path(__file__).parent

    for script_file in script_root.iterdir():
        if script_file.is_file():
            with open(cast(str, script_file), "r") as handle:
                if "python" in handle.readline():
                    _black(script_file.absolute())


if __name__ == "__main__":
    main()
