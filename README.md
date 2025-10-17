<picture align="center">
  <img alt="HSPy Logo)" src="images/HSOpenCV_Logo.png">
</picture>

-----------------

# HSOpenCV: OpenCV with thermal imaging algorithms for HTPA devices
HSOpenCV is a Python library developed by Heimann Sensor that extends the native OpenCV Python bindings with customized algorithms for Heimann Sensor Thermopile Arrays (HTPA). OpenCV’s core algorithms are implemented in C++, and HSOpenCV provides Python access to additional person detection and thermal processing algorithms specifically designed for HTPA devices. This integration allows developers to use both standard OpenCV functions and Heimann Sensor’s HTPA-specific algorithms within the same Python environment, enabling efficient prototyping and seamless integration into existing computer vision workflows.

# Installation
This library can either be installed using the prebuilt pip wheel located in the `dist` folder or installing from source using the `setup.py` located in the parent folder of the repository. Both variants are described below.

## Installing pre-built pip-wheel
A wheel is a prebuilt binary distribution - essentially, the compiled and ready-to-install form of a package. Pip just unpacks the wheel and places files directly into site-packages. No compilation, no setup.py execution. The caveat is, that the environment the wheel was built with must match the environment it is installed to. If no compatible wheel exists, pip falls back to building from source (setup.py).

Prerequisites: The wheel in `dist` was built using
- Python 3.12.x ([Download Python](https://www.python.org/downloads/))
- Numpy 1.26.4
The environment the wheel is installed to needs to match these specifications.

To install the wheel to your environment activate the environment you want to install to and do
```sh
  pip install ./path/to/HSOpenCV/dist/HSOpenCV-4.12.0-py3.whl
```
## Installing from source
Installing from `setup.py` installs the source distribution (the raw Python code). The `setup.py` script compiles any C/C++ or Cython extensions and then copies the resulting files into your Python environment's site-packages directory. It lets you build against your specific environment and works even if no prebuilt wheels are available.

Prerequisites:
- Numpy < 2.x.x: OpenCV still has issues with more recent numpy version.

To install to your environment activate the environment you want to install to and do
```sh
  pip install ./path/to/HSOpenCV/
```
## Check installation
1. In the shell start the python interpreter via

   ```sh
   python
   ```
2. Then try to import HSOpenCV by typing

   ```sh
   import cv2
   ```
   If no error message occurs, installation was successful.
