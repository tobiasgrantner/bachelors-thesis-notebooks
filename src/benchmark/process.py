import subprocess
from subprocess import CompletedProcess, DEVNULL
from typing import Callable


def run(
    command: str, shell=True, check=True, stdout=DEVNULL, stderr=None, **kwargs
) -> CompletedProcess[bytes]:
    return subprocess.run(
        command, shell=shell, check=check, stdout=stdout, stderr=stderr, **kwargs
    )


def runnable(command: str) -> Callable[[], CompletedProcess[bytes]]:
    def callable(*_) -> CompletedProcess[bytes]:
        return run(command, shell=True, check=True, stdout=DEVNULL, stderr=None)

    return callable
