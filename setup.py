import os

from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

__version__ = "0.0.2"


def build_cgal() -> str:
    # Build CGAL and return the include directory
    os.system(
        "cd cgal; mkdir build; cd build; "
        "cmake -DCMAKE_INSTALL_PREFIX=. -DCMAKE_BUILD_TYPE=Release ..; "
        "make install -j4;"
    )
    return os.path.join(os.getcwd(), "cgal", "build", "include")


ext_modules = [
    Pybind11Extension(
        "simple_cgal",
        ["src/delaunay.cpp"],
        include_dirs=[build_cgal()],
        extra_link_args=["-lgmp"],  # Linker flags
    ),
]

setup(
    name="simple_cgal",
    version=__version__,
    author="Keith Roberts & Guillaume Gay",
    author_email="keithrbt0gmail.com",
    description="A simple wrapper to perform delaunay in cgal with pybind11 and CMake",
    long_description="",
    ext_modules=ext_modules,
    # Currently, build_ext only provides an optional "highest supported C++
    # level" feature, but in the future it may provide more features.
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.7",
)
