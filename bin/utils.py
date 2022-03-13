"""
This module contains common utilities that are used by our scripts.
"""

import contextlib
import enum
import functools
import os
import pathlib
import platform
import re
import subprocess
import sys
import textwrap
from datetime import datetime
from typing import Dict, Iterator, List, Optional, Set, Union, cast

try:
    from distutils.version import StrictVersion
    from distutils.versionpredicate import VersionPredicate
except ImportError:
    sys.stderr.write(
        "You need to install python3-distutils package before running this script\n"
    )
    sys.exit()


# Supported system versions
class OperatingSystem(enum.Enum):
    MAC = "mac"
    UBUNTU = "ubuntu"
    FEDORA = "fedora"
    ARCH = "arch"  # Work-in-progress

    @property
    def is_macos(self) -> bool:
        return self == self.MAC

    @property
    def is_linux(self) -> bool:
        return self != self.MAC


# Resolve the root path of the project directory. We need this to look up
# various files.
PROJECT_ROOT = pathlib.Path(__file__).parent.parent


def get_app_name() -> str:
    return "simulatorX"


APP_NAME = get_app_name()


#################
# Print helpers #
#################


def _color(value: str, *, color_code: str) -> str:
    return f"\033[{color_code}m{value}\033[0m"


magenta = functools.partial(_color, color_code="35")
gray = functools.partial(_color, color_code="37")
red = functools.partial(_color, color_code="91")
yellow = functools.partial(_color, color_code="93")
bold = functools.partial(_color, color_code="1")


def print_with_time(value: str, end="\n", flush=False) -> None:
    _time = f"[{datetime.now():%H:%M:%S}]"
    print(f"{gray(_time)} {value}", end=end, flush=flush)


def center(value: str, *, width: int) -> str:

    indent = max((80 - len(value)) // 2, 0)
    return textwrap.indent(value, " " * indent)


####################
# Running commands #
####################


def run(
    *args: Union[str, pathlib.Path],
    env: Optional[Dict[str, str]] = None,
    capture: bool = True,
    inp: Optional[str] = None,
) -> str:
    """
    Execute a command

    NOTE: Error handing is done with the `error_handler()' context manager
    """

    process = subprocess.run(  # type: ignore
        args, check=True, capture_output=capture, encoding="utf-8", env=env, input=inp
    )

    return process.stdout


def run_postgres_command(
    command: str,
    *command_args: Union[str, pathlib.Path],
    user: Optional[str],
    host: Optional[str],
    port: Optional[int],
    password: Optional[str],
) -> None:

    args: List[Union[str, pathlib.Path]] = [command]

    # Determine extra arguments to run postgres command with. If command line
    # arguments are given we use them, else fall back to environment variables

    postgres_user = user if user else os.getenv("POSTGRES_USER")
    if postgres_user:
        args.extend(["--user", postgres_user])

    postgres_host = host if host else os.getenv("POSTGRES_HOST")
    if postgres_host:
        args.extend(["--host", postgres_host])

    postgres_port = port if port else os.getenv("POSTGRES_PORT")
    if postgres_port:
        args.extend(["--port", str(postgres_port)])

    postgres_password = password if password else os.getenv("POSTGRES_PASSWORD")

    args.extend(command_args)

    env = {**os.environ}
    if postgres_password:
        env["PGPASSWORD"] = postgres_password

    run(*args, env=env)


def run_management_command(
    command: str,
    *command_args: Union[str, pathlib.Path],
    db_name: str,
    env_vars: Dict[str, str] = {},
):

    if db_name:
        env_vars["POSTGRES_DB"] = db_name

    run(
        sys.executable,
        PROJECT_ROOT / "manage.py",
        command,
        *command_args,
        env={**os.environ, **env_vars},
    )


def check_exit_code(*args: str, expected_result: int = 0) -> bool:
    try:
        return (
            subprocess.run(  # type: ignore
                args, check=False, capture_output=True
            ).returncode
            == expected_result
        )
    except FileNotFoundError:
        return False


def postgres_env(
    host: Optional[str],
    port: Optional[int],
    user: Optional[str],
    password: Optional[str],
) -> Dict[str, str]:

    env = {}

    if host:
        env["POSTGRES_HOST"] = host

    if port:
        env["POSTGRES_PORT"] = port

    if user:
        env["POSTGRES_USER"] = user

    if password:
        env["POSTGRES_PASSWORD"] = password

    return env


##################
# Error handling #
##################


class Cancel(RuntimeError):
    # pylint: disable=redefined-builtin
    def __init__(self, *, description: str, help: str = "") -> None:
        super().__init__()
        self.description = description
        self.help = help


@contextlib.contextmanager
def error_handler(
    *,
    description: str,
    exit_on_failure: bool = True,
    error_message: Optional[str] = None,
) -> Iterator[None]:
    """
    A context manager that handles subprocess errors.
    """

    print_with_time(magenta(f"{description} ... "), end="", flush=True)

    try:
        yield
        print("✅")
    except subprocess.CalledProcessError as e:
        print("❌")
        print(
            red(
                f"An error occured while running "
                f'"{" ".join(str(arg) for arg in e.args)}"'
            )
        )

        if e.stdout:
            print("-" * 20 + red(" stdout ") + "-" * 20)
            print(e.stdout.strip())
            print("-" * 48)

        if e.stderr:
            print("-" * 20 + red(" stderr ") + "-" * 20)
            print(e.stderr.strip())
            print("-" * 48)

        if not exit_on_failure:
            raise
        if error_message:
            sys.exit(error_message)
        sys.exit(1)
    except Cancel as e:
        print("❌")
        print(red(e.description))
        if e.help:
            print(e.help)
        if not exit_on_failure:
            raise
        sys.exit(1)


########################
# Python version utils #
########################


def get_required_python_version() -> VersionPredicate:
    """
    Helper to find the Python version requirement specified in the
    pyproject.toml file. Returns None if no version requirement is found.
    """

    with open(PROJECT_ROOT / "pyproject.toml") as f:
        pyproject_content = f.read()

    line_regex = re.compile(r'python\s*=\s*"(?P<version_spec>[^"]+)"')
    for line in pyproject_content.splitlines():
        if not line.startswith("python ="):
            continue

        result = line_regex.match(line)

        if result:
            version_spec = result.groupdict()["version_spec"]
            return VersionPredicate(f"python ({version_spec})")

    raise Cancel(
        description="Unable to find required Python version",
        help='Please make sure pyproject.toml contains a "python = "<version>"" line',
    )


def ensure_python_version(*, predicate: VersionPredicate) -> pathlib.Path:
    """
    Ensure that a Python version satisfying the given predicate is installed
    and return the path to that Python binary.
    """

    system = get_operating_system()

    if system.is_linux:

        if system == OperatingSystem.UBUNTU:
            stdout = run("apt", "search", "python")
        else:
            stdout = run("dnf", "search", "python")

        package_name_regex = re.compile(r"(python(\d)(\.)?(\d+))[./].*")
        package_desc_regex = re.compile(r"(python\d)\..* : .* (\d)(\.)?(\d+).*")

        versions = []

        for line in stdout.splitlines():
            for regex in (package_name_regex, package_desc_regex):
                match = regex.fullmatch(line.strip())
                if match:
                    package_name, main, __, minor = match.groups()
                    versions.append(
                        (
                            StrictVersion(f"{main}.{minor}"),
                            package_name,
                            f"/usr/bin/python{main}.{minor}",
                        )
                    )
                    break

        for version, package_name, executable in versions:
            if predicate.satisfied_by(version):
                if system == OperatingSystem.UBUNTU:
                    run(
                        "sudo",
                        "apt",
                        "install",
                        "-y",
                        package_name,
                        f"{package_name}-dev",
                        f"{package_name}-venv",
                    )
                if system == OperatingSystem.FEDORA:
                    run(
                        "sudo",
                        "dnf",
                        "install",
                        "-y",
                        package_name,
                        "python3-devel",
                        "python3-virtualenv",
                    )

                python_path = run("which", executable).strip()
                return pathlib.Path(python_path)

    elif system.is_macos:
        # Find the versions that are available from homebrew
        stdout = run("brew", "search", "--formulae", "/^python@/")
        line_regex = re.compile(r"python@\d+\.\d+")
        versions = [
            (StrictVersion(line.split("@", 2)[1]), cast(str, line.strip()), "")
            for line in stdout.splitlines()
            if line_regex.fullmatch(line.strip())
        ]

        # Find and install the first version that satisifies the predicate
        for version, package_name, __ in versions:
            if predicate.satisfied_by(version):
                run("brew", "install", package_name)
                prefix = run("brew", "--prefix", package_name).strip()
                return pathlib.Path(prefix) / "bin" / "python3"

    raise Cancel(
        description="Failed to find a suitable Python version",
        help=f"No version matching {predicate} could be found",
    )


def get_venv_python_version(*, path: pathlib.Path) -> Optional[StrictVersion]:
    """
    Find the Python version used to create the venv at the specified path.
    """

    pyvenv_cfg = path / "pyvenv.cfg"

    line_regex = re.compile(r"version\s*=\s*(?P<version_spec>\d+\.\d+.\d+)")

    if pyvenv_cfg.exists():
        with open(cast(str, pyvenv_cfg)) as f:
            for line in f.readlines():
                result = line_regex.fullmatch(line.strip())
                if result:
                    return StrictVersion(result.groupdict()["version_spec"])

    return None


def ensure_venv() -> pathlib.Path:
    """
    Create a Python virtual environment in the .venv directory inside the
    project directory if one does not exist. If the environment already exists
    but is a Python version that's not compatible with the required Python
    version the venv is deleted and re-created.
    """

    version_predicate = get_required_python_version()
    venv_path = PROJECT_ROOT / ".venv"

    # If the venv already exist, verify that it's the correct version
    if venv_path.exists():

        # Check if the existing venv has a compatible Python version
        venv_version = get_venv_python_version(path=venv_path)
        if venv_version and version_predicate.satisfied_by(venv_version):
            return venv_path

        # The existing venv is not the correct version, so remove it before we
        # create a new one.
        run("rm", "-rf", venv_path)

    python_bin = ensure_python_version(predicate=version_predicate)

    # Create a new venv with the given Python executable
    run(python_bin, "-m", "venv", venv_path)

    return venv_path


################
# System utils #
################


def get_operating_system() -> OperatingSystem:
    """
    Find which operating system we are running on.
    """

    if sys.platform == "darwin":
        return OperatingSystem.MAC

    elif sys.platform.startswith("linux"):
        with open("/etc/os-release") as handle:
            platform_information = handle.read().lower()

            if "ubuntu" in platform_information:
                return OperatingSystem.UBUNTU

            elif "debian" in platform_information:
                return OperatingSystem.UBUNTU

            elif "fedora" in platform_information:
                return OperatingSystem.FEDORA

            if "arch" in platform_information:
                return OperatingSystem.ARCH

    raise Cancel(
        description="This script does not support your current system",
        help="Please follow the manual instructions for for setting up your system",
    )


def is_arm_mac() -> bool:
    """
    Check if we're currently running on an ARM/Apple Silicon Mac
    """

    return platform.system() == "Darwin" and platform.machine() == "arm64"


def get_installed_packages(system: OperatingSystem) -> Set[str]:
    """
    Get all system installed packages
    """

    if system == OperatingSystem.MAC:
        return {line.strip() for line in run("brew", "list", "--formula").splitlines()}

    if system == OperatingSystem.FEDORA:
        return {
            line.split()[0].strip()
            for line in run("dnf", "list", "installed").splitlines()
        }

    if system == OperatingSystem.UBUNTU:
        return {
            line.partition("/")[0]
            for line in run("apt", "list", "--installed").splitlines()
        }

    raise Cancel(
        description="This script does not support your current system",
        help="Please follow the manual instructions for for setting up your system",
    )


def get_installed_services(system: OperatingSystem) -> List[str]:
    """
    Get all installed system services. Will use find all services using
    brew list on mac, and systemctl on ubuntu and fedora.
    """

    if system.is_macos:
        return [
            line.strip().split()[0]
            for line in run("brew", "services", "list").splitlines()
        ]

    if system.is_linux:
        return [
            line.strip().split()[0]
            for line in run(
                "sudo", "systemctl", "list-units", "--type=service"
            ).splitlines()
            if ".service" in line
        ]

    return []
