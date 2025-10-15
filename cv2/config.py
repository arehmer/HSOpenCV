import os
from pathlib import Path

# __file__ is the path of the current file
current_dir = Path(__file__).parent
dll_dir = current_dir / 'bin' / 'Release'

BINARIES_PATHS = [
    str(dll_dir)
] + BINARIES_PATHS
