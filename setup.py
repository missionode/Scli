"""Setup script for scli."""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
this_directory = Path(__file__).parent
long_description = ""
readme_file = this_directory / "README.md"
if readme_file.exists():
    long_description = readme_file.read_text(encoding="utf-8")

# Read requirements
requirements_file = this_directory / "requirements.txt"
requirements = []
if requirements_file.exists():
    requirements = requirements_file.read_text().strip().split('\n')

setup(
    name="scli",
    version="1.0.0",
    author="SCLI Contributors",
    description="Offline CLI Assistant powered by open-source small language models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/scli",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "scli=scli.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="cli ai llm offline assistant chatbot language-model",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/scli/issues",
        "Source": "https://github.com/yourusername/scli",
    },
)
