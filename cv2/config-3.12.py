from pathlib import Path

# __file__ is the path of the current file
current_dir = Path(__file__).parent
pyd_dir = current_dir / 'lib' 

PYTHON_EXTENSIONS_PATHS = [
    str(pyd_dir)
] + PYTHON_EXTENSIONS_PATHS
