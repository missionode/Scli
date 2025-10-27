#!/usr/bin/env python3
"""Utility script to download popular models for SCLI."""

import sys
import subprocess
from pathlib import Path

# Popular models with download links
MODELS = {
    "phi-3-mini": {
        "name": "Phi-3 Mini 3.8B (Q4_K_M)",
        "url": "https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4.gguf",
        "filename": "phi-3-mini-4k-instruct-q4.gguf",
        "size": "~2.3GB",
        "description": "Microsoft's Phi-3 Mini, excellent for general chat and coding"
    },
    "tinyllama": {
        "name": "TinyLlama 1.1B (Q4_K_M)",
        "url": "https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
        "filename": "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
        "size": "~700MB",
        "description": "Fast and lightweight, good for quick responses"
    },
    "qwen2.5-3b": {
        "name": "Qwen2.5 3B (Q4_K_M)",
        "url": "https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-GGUF/resolve/main/qwen2.5-3b-instruct-q4_k_m.gguf",
        "filename": "qwen2.5-3b-instruct-q4_k_m.gguf",
        "size": "~2.0GB",
        "description": "Excellent for coding tasks and long context"
    },
    "qwen2.5-0.5b": {
        "name": "Qwen2.5 0.5B (Q4_K_M)",
        "url": "https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/qwen2.5-0.5b-instruct-q4_k_m.gguf",
        "filename": "qwen2.5-0.5b-instruct-q4_k_m.gguf",
        "size": "~350MB",
        "description": "Ultra-lightweight, runs on any device"
    }
}


def print_available_models():
    """Print available models."""
    print("\n" + "=" * 70)
    print("Available Models for Download")
    print("=" * 70)

    for key, info in MODELS.items():
        print(f"\n[{key}]")
        print(f"  Name: {info['name']}")
        print(f"  Size: {info['size']}")
        print(f"  Description: {info['description']}")

    print("\n" + "=" * 70)


def download_model(model_key: str, models_dir: Path = Path("./models")):
    """Download a model.

    Args:
        model_key: Key of the model to download
        models_dir: Directory to save the model
    """
    if model_key not in MODELS:
        print(f"Error: Model '{model_key}' not found!")
        print_available_models()
        return False

    model_info = MODELS[model_key]
    models_dir.mkdir(parents=True, exist_ok=True)
    output_path = models_dir / model_info['filename']

    if output_path.exists():
        print(f"\nModel already exists at: {output_path}")
        overwrite = input("Overwrite? (y/N): ").lower().strip()
        if overwrite != 'y':
            print("Cancelled.")
            return False

    print(f"\nDownloading {model_info['name']}...")
    print(f"Size: {model_info['size']}")
    print(f"URL: {model_info['url']}")
    print(f"Destination: {output_path}")
    print("\nThis may take a while depending on your connection...\n")

    try:
        # Try wget first
        result = subprocess.run(
            ["wget", "-O", str(output_path), model_info['url']],
            check=True
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        # Fallback to curl
        try:
            result = subprocess.run(
                ["curl", "-L", "-o", str(output_path), model_info['url']],
                check=True
            )
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("\nError: Neither wget nor curl is available!")
            print("Please install wget or curl to download models.")
            print(f"\nAlternatively, manually download from:\n{model_info['url']}")
            return False

    print(f"\n✓ Successfully downloaded to: {output_path}")
    print(f"\nTo add this model to SCLI, run:")
    print(f"  scli models add {model_key} {output_path} --default")

    return True


def main():
    """Main entry point."""
    print("\n" + "=" * 70)
    print("SCLI Model Downloader")
    print("=" * 70)

    if len(sys.argv) < 2:
        print("\nUsage: python download_models.py <model-key> [output-dir]")
        print_available_models()
        print("\nExample:")
        print("  python download_models.py phi-3-mini")
        print("  python download_models.py tinyllama ./my-models")
        sys.exit(1)

    model_key = sys.argv[1]
    models_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("./models")

    success = download_model(model_key, models_dir)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
