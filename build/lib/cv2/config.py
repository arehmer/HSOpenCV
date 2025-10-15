import os
from pathlib import Path

# __file__ is the path of the current file
current_dir = Path(__file__).parent
dll_dir = current_dir / 'bin' / 'Release'

BINARIES_PATHS = [
    dll_dir.as_posix()
] + BINARIES_PATHS