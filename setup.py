import os
from setuptools import setup, find_packages

with open(os.path.join(".", "src", "backend", "meta.py"), "r") as f:
    exec(f.read())


def dependencies(requirmentsFile):
    with open(requirmentsFile, "r") as f:
        dependencies = f.readlines()
        return [
            dependency
            for dependency in dependencies
            if len(dependency.strip()) > 0 and not dependency.strip().startswith("-e")
        ]


setup(
    name="githubnav",
    version=VERSION,
    description="Search for repositories on GitHub",
    author="Usman Zubair",
    author_email="uzubair@gmail.com",
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=dependencies("requirements.txt"),
    extras_require={"devel": dependencies("requirements-devel.txt")},
    python_requires=">=3.7.6",
    include_package_data=True,
)
