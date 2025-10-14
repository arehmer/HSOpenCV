import os
import pathlib

this_dir = pathlib.Path(__file__).resolve().parent
module_dir = this_dir.parents[1]
lib_dir = module_dir / 'lib' / 'python3' / 'Release'

print(lib_dir)

PYTHON_EXTENSIONS_PATHS = [lib_dir.as_posix()] + PYTHON_EXTENSIONS_PATHS
