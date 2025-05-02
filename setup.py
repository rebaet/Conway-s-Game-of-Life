from setuptools import setup, find_packages

setup(
    name="conways-game-of-life-pygame",
    version="1.0.0",
    description="A Python implementation of Conway's Game of Life using Pygame.",
    author="Rubaiyet Masum",
    author_email="rubaiyetdhk@gmail.com",
    url="https://github.com/rebaet/conways-game-of-life-pygame",
    packages=find_packages(),
    install_requires=[
        "pygame>=2.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)