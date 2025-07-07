#!/usr/bin/env python3
"""
Setup script for robust-average package.
"""

from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name="robust-average",
        version="0.1.4",
        description="A Python package that intelligently selects the most robust average for price analysis",
        author="Ben",
        author_email="bensha2019@outlook.com",
        packages=find_packages(),
        install_requires=[
            "numpy>=1.20.0",
            "pandas>=1.3.0",
            "scipy>=1.7.0",
        ],
        python_requires=">=3.8",
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Intended Audience :: Financial and Insurance Industry",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Topic :: Scientific/Engineering :: Information Analysis",
            "Topic :: Office/Business :: Financial",
        ],
        license="MIT",
    ) 