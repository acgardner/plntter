from setuptools import setup, find_packages


setup(
    name="plntter",
    version="0.0.1",
    author="Anthony Gardner",
    author_email="acgardner95@gmail.com",
    description="Portable Localization / Navigation Toolkit for Terrestrial / Extraterrestrial Roving",
    url="https://github.com/acgardner/plntter.git",
    license="MIT",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "matplotlib",
        "seaborn",
        "spiceypy"
    ],
)