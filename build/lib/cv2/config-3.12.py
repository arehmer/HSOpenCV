from pathlib import Path

# __file__ is the path of the current file
current_dir = Path(__file__).parent
pyd_dir = current_dir / 'lib' / 'python3' / 'Release'

PYTHON_EXTENSIONS_PATHS = [
    pyd_dir.as_posix()
] + PYTHON_EXTENSIONS_PATHS
