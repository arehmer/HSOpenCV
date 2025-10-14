import os

# Make sure the package directory itself is searched first for the .pyd
PYTHON_EXTENSIONS_PATHS = [
    os.path.dirname(os.path.abspath(__file__)),
] + PYTHON_EXTENSIONS_PATHS
