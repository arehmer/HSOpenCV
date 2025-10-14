import os
from pathlib import Path

this_dir = Path.cwd()
module_dir = this_dir.parents[1]
bin_dir = module_dir / 'bin' / 'Release'

BINARIES_PATHS = [bin_dir.as_posix()] + BINARIES_PATHS
