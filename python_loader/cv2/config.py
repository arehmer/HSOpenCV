import os
import pathlib

this_dir = pathlib.Path(__file__).resolve().parent
module_dir = this_dir.parents[1]
bin_dir = module_dir / 'bin' / 'Release'

print(bin_dir)

BINARIES_PATHS = [bin_dir.as_posix()] + BINARIES_PATHS
