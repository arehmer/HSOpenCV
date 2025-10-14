import os

# This file runs before importing the native extension; it’s used to seed DLL paths.
# We resolve a private ".libs" directory inside the installed cv2 package.

_pkg_dir = os.path.dirname(os.path.abspath(__file__))
_dll_dir = os.path.join(_pkg_dir, ".libs")

# On Windows, make the bundled DLLs discoverable prior to loading cv2.pyd
if os.name == "nt" and os.path.isdir(_dll_dir):
    add_dll_dir = getattr(os, "add_dll_directory", None)
    if callable(add_dll_dir):
        add_dll_dir(_dll_dir)  # Python 3.8+ secure DLL directory
    else:
        os.environ["PATH"] = _dll_dir + os.pathsep + os.environ.get("PATH", "")

# Tell the upstream loader our binaries directory (keeps its prepend logic intact)
BINARIES_PATHS = [_dll_dir] + BINARIES_PATHS
