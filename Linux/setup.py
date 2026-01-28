import os
import setuptools


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def collect_module_typing_stub_files(root_module_path):
    stub_files = []
    for module_path, _, files in os.walk(root_module_path):
        stub_files.extend(
            map(lambda p: os.path.join(module_path, p),
                filter(lambda f: f.endswith(".pyi"), files))
        )
    return stub_files
    
def collect_dll_files(root_module_path):
    dll_files = []
    for module_path, _, files in os.walk(root_module_path):
        dll_files.extend(
            map(lambda p: os.path.join(module_path, p),
                filter(lambda f: f.endswith(".dll"), files))
        )
    return dll_files
    
def collect_pyd_files(root_module_path):
    pyd_files = []
    for module_path, _, files in os.walk(root_module_path):
        pyd_files.extend(
            map(lambda p: os.path.join(module_path, p),
                filter(lambda f: f.endswith(".pyd"), files))
        )
    return pyd_files


def main():
    os.chdir(SCRIPT_DIR)

    package_name = 'opencv'
    package_version = os.environ.get('OPENCV_VERSION', '4.12.0')  # TODO

    long_description = 'Open Source Computer Vision Library Python bindings'  # TODO

    root_module_path = os.path.join(SCRIPT_DIR, "cv2")
    py_typed_path = os.path.join(root_module_path, "py.typed")
    #typing_stub_files = []
    #if os.path.isfile(py_typed_path):
    #    typing_stub_files = collect_module_typing_stub_files(root_module_path)
    #    if len(typing_stub_files) > 0:
    #        typing_stub_files.append(py_typed_path)
    
    dll_files = collect_dll_files(root_module_path)
    pyd_files = collect_pyd_files(root_module_path)
    typing_stub_files = collect_module_typing_stub_files(root_module_path)
    
    package_data = typing_stub_files + dll_files + pyd_files
    
    setuptools.setup(
        name=package_name,
        version=package_version,
        url='https://github.com/opencv/opencv',
        license='Apache 2.0',
        description='OpenCV python bindings',
        long_description=long_description,
        long_description_content_type="text/markdown",
        packages=setuptools.find_packages(),
        package_data={
            "cv2": package_data
        },
        include_package_data = True,
        maintainer="OpenCV Team",
        install_requires="numpy==1.26.4",
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Intended Audience :: Information Technology",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: MacOS",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: POSIX",
            "Operating System :: Unix",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Programming Language :: Python :: 3.13",
            "Programming Language :: C++",
            "Programming Language :: Python :: Implementation :: CPython",
            "Topic :: Scientific/Engineering",
            "Topic :: Scientific/Engineering :: Image Recognition",
            "Topic :: Software Development",
        ],
    )


if __name__ == '__main__':
    main()
