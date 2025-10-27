#!/usr/bin/env python3
"""Verification script to check SCLI installation."""

import sys
from pathlib import Path

# Colors for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'


def check_file(path: Path, description: str) -> bool:
    """Check if a file exists."""
    if path.exists():
        print(f"{GREEN}✓{RESET} {description}: {path}")
        return True
    else:
        print(f"{RED}✗{RESET} {description}: {path} (NOT FOUND)")
        return False


def check_import(module_name: str, description: str) -> bool:
    """Check if a module can be imported."""
    try:
        __import__(module_name)
        print(f"{GREEN}✓{RESET} {description}: {module_name}")
        return True
    except ImportError as e:
        print(f"{RED}✗{RESET} {description}: {module_name} ({e})")
        return False


def main():
    """Run verification checks."""
    print(f"\n{BLUE}{'=' * 70}{RESET}")
    print(f"{BLUE}SCLI Installation Verification{RESET}")
    print(f"{BLUE}{'=' * 70}{RESET}\n")

    project_root = Path(__file__).parent
    all_checks_passed = True

    # Check project structure
    print(f"\n{YELLOW}Checking Project Structure...{RESET}\n")

    files_to_check = [
        (project_root / "scli" / "__init__.py", "Main package init"),
        (project_root / "scli" / "cli.py", "CLI entry point"),
        (project_root / "scli" / "core" / "config.py", "Configuration module"),
        (project_root / "scli" / "core" / "model_manager.py", "Model manager"),
        (project_root / "scli" / "core" / "conversation.py", "Conversation manager"),
        (project_root / "scli" / "plugins" / "base.py", "Plugin base"),
        (project_root / "scli" / "plugins" / "models" / "llama_cpp_plugin.py", "Llama.cpp plugin"),
        (project_root / "scli" / "ui" / "formatter.py", "UI formatter"),
        (project_root / "scli" / "ui" / "interactive.py", "Interactive UI"),
        (project_root / "requirements.txt", "Requirements file"),
        (project_root / "setup.py", "Setup script"),
        (project_root / "README.md", "README documentation"),
        (project_root / "LICENSE", "License file"),
    ]

    for file_path, description in files_to_check:
        if not check_file(file_path, description):
            all_checks_passed = False

    # Check dependencies
    print(f"\n{YELLOW}Checking Dependencies...{RESET}\n")

    dependencies = [
        ("typer", "CLI framework"),
        ("rich", "Terminal UI"),
        ("yaml", "YAML parser"),
        ("prompt_toolkit", "Interactive prompts"),
        ("pygments", "Syntax highlighting"),
    ]

    for module, description in dependencies:
        if not check_import(module, description):
            all_checks_passed = False

    # Check optional dependencies
    print(f"\n{YELLOW}Checking Optional Dependencies...{RESET}\n")

    optional_deps = [
        ("llama_cpp", "llama-cpp-python (REQUIRED for inference)"),
    ]

    for module, description in optional_deps:
        check_import(module, description)

    # Check directories
    print(f"\n{YELLOW}Checking Directories...{RESET}\n")

    dirs_to_check = [
        (project_root / "models", "Models directory"),
        (project_root / "data", "Data directory"),
        (project_root / "scli" / "core", "Core module directory"),
        (project_root / "scli" / "plugins", "Plugins directory"),
        (project_root / "scli" / "ui", "UI module directory"),
    ]

    for dir_path, description in dirs_to_check:
        if not check_file(dir_path, description):
            all_checks_passed = False

    # Summary
    print(f"\n{BLUE}{'=' * 70}{RESET}")
    if all_checks_passed:
        print(f"{GREEN}✓ All checks passed!{RESET}")
        print(f"\n{GREEN}SCLI is ready to use!{RESET}")
        print(f"\nNext steps:")
        print(f"  1. Install dependencies: pip install -r requirements.txt")
        print(f"  2. Install scli: pip install -e .")
        print(f"  3. Download a model: python download_models.py phi-3-mini")
        print(f"  4. Add the model: scli models add phi-3-mini ./models/phi-3-mini-q4.gguf --default")
        print(f"  5. Start chatting: scli chat")
    else:
        print(f"{RED}✗ Some checks failed!{RESET}")
        print(f"\n{YELLOW}Please ensure all files are present and dependencies are installed.{RESET}")
        return 1

    print(f"\n{BLUE}{'=' * 70}{RESET}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
