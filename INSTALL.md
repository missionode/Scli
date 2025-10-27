# SCLI Installation Guide

Complete installation instructions for SCLI - Offline CLI Assistant.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- 4GB+ RAM (8GB recommended for 3B parameter models)
- 5GB+ free disk space (for models)

### Check Python Version

```bash
python --version
# or
python3 --version
```

If Python is not installed:
- **Ubuntu/Debian**: `sudo apt install python3 python3-pip`
- **macOS**: `brew install python3`
- **Windows**: Download from https://python.org

## Installation Steps

### 1. Clone or Download the Project

If you already have the project, skip this step. Otherwise:

```bash
git clone https://github.com/yourusername/scli.git
cd scli
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- typer - CLI framework
- rich - Beautiful terminal output
- pyyaml - Configuration management
- prompt-toolkit - Interactive input
- pygments - Syntax highlighting

### 3. Install llama-cpp-python

**For CPU-only systems (most common):**
```bash
pip install llama-cpp-python
```

**For NVIDIA GPU acceleration (CUDA):**
```bash
CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python
```

**For Apple Silicon (M1/M2/M3 Macs):**
```bash
CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python
```

**For AMD ROCm (AMD GPUs):**
```bash
CMAKE_ARGS="-DLLAMA_HIPBLAS=on" pip install llama-cpp-python
```

### 4. Install SCLI

```bash
pip install -e .
```

The `-e` flag installs in "editable" mode, allowing you to modify the code if needed.

### 5. Verify Installation

```bash
python verify_installation.py
```

You should see all checks passed (✓).

### 6. Test SCLI

```bash
scli --help
```

You should see the SCLI help message with available commands.

## Post-Installation

### Download a Model

Choose a model based on your hardware:

**Low-end devices (2-4GB RAM):**
```bash
python download_models.py qwen2.5-0.5b
# or
python download_models.py tinyllama
```

**Mid-range devices (4-8GB RAM):**
```bash
python download_models.py phi-3-mini
# or
python download_models.py qwen2.5-3b
```

### Add Model to SCLI

After downloading:

```bash
# Example for Phi-3 Mini
scli models add phi-3-mini ./models/phi-3-mini-4k-instruct-q4.gguf --default
```

Replace with your downloaded model name and path.

### Start Using SCLI

```bash
scli chat
```

## Troubleshooting

### "pip: command not found"

Install pip:
```bash
# Ubuntu/Debian
sudo apt install python3-pip

# macOS
python3 -m ensurepip

# Windows
python -m ensurepip
```

### "CMAKE_ARGS not working"

Make sure you have cmake installed:
```bash
# Ubuntu/Debian
sudo apt install cmake

# macOS
brew install cmake

# Windows
# Download from https://cmake.org/download/
```

### "No module named 'typer'" (or other module)

Reinstall dependencies:
```bash
pip install --upgrade -r requirements.txt
```

### "Permission denied" when installing

Use user installation:
```bash
pip install --user -r requirements.txt
pip install --user -e .
```

### llama-cpp-python installation fails

Try installing build dependencies first:

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install build-essential cmake python3-dev
pip install llama-cpp-python
```

**macOS:**
```bash
xcode-select --install
brew install cmake
pip install llama-cpp-python
```

### Out of memory when loading model

- Use a smaller model (qwen2.5-0.5b or tinyllama)
- Close other applications
- Consider using higher quantization (Q4_0 or Q3_K_M variants)

## Platform-Specific Notes

### Termux (Android)

```bash
pkg install python cmake clang
pip install -r requirements.txt
pip install llama-cpp-python
pip install -e .
```

### Windows Subsystem for Linux (WSL)

Follow Ubuntu/Debian instructions above.

### Docker

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt
RUN pip install -e .

CMD ["scli", "chat"]
```

## Uninstallation

To remove SCLI:

```bash
pip uninstall scli
```

To also remove dependencies:

```bash
pip uninstall typer rich pyyaml prompt-toolkit pygments llama-cpp-python
```

## Updating

To update SCLI to the latest version:

```bash
cd scli
git pull  # if using git
pip install --upgrade -r requirements.txt
pip install -e .
```

## Getting Help

If you encounter issues:

1. Check the [README.md](README.md) for detailed information
2. Review the [QUICKSTART.md](QUICKSTART.md) guide
3. Run `python verify_installation.py` to check for problems
4. Open an issue on GitHub with your error message

## Next Steps

After successful installation:

1. Read [QUICKSTART.md](QUICKSTART.md) for quick setup
2. Download and configure a model
3. Start chatting with `scli chat`
4. Explore advanced features in [README.md](README.md)

---

**Happy chatting with your offline AI assistant!** 🎉
