import os
from pathlib import Path

this_dir = Path.cwd()
module_dir = this_dir.parents[1]
lib_dir = module_dir / 'lib' / 'python3' / 'Release'

PYTHON_EXTENSIONS_PATHS = [lib_dir.as_posix()] + PYTHON_EXTENSIONS_PATHS
