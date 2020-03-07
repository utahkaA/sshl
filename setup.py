from setuptools import setup, find_packages

setup(
    name="sshl",
    version="0.0.1",
    install_requires=[],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    entry_points={
        "console_scripts": [
            "sshl=sshl.main:_main"
        ]
    }
)
