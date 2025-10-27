# SCLI - Offline CLI Assistant

A powerful offline command-line AI assistant powered by open-source small language models. SCLI runs completely offline, ensuring privacy and independence from cloud services.

## Features

- **Fully Offline**: Works without internet connection
- **Small LLM Support**: Optimized for efficient small language models (Phi-3, TinyLlama, Qwen, etc.)
- **Pluggable Architecture**: Easy to add, remove, or upgrade models
- **Interactive Chat**: Rich terminal interface with markdown rendering and syntax highlighting
- **Conversation History**: Save and resume conversations
- **Multiple Backends**: Extensible plugin system for different model types
- **Resource Efficient**: Supports quantized models for low-memory devices

## Installation

### Prerequisites

- Python 3.8 or higher
- 4GB+ RAM (8GB recommended for 3B parameter models)
- Models in GGUF format (downloaded separately)

### Install from Source

```bash
# Clone the repository
git clone https://github.com/yourusername/scli.git
cd scli

# Install dependencies
pip install -r requirements.txt

# Install scli
pip install -e .
```

### Install llama-cpp-python

For CPU-only systems:
```bash
pip install llama-cpp-python
```

For GPU acceleration (CUDA):
```bash
CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python
```

For Apple Silicon (Metal):
```bash
CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python
```

## Quick Start

### 1. Download a Model

Download a GGUF model from Hugging Face. Recommended models:

**Small & Fast (1-2GB RAM)**
- [TinyLlama 1.1B](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF)
- [Qwen2.5 0.5B](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF)

**Balanced (3-4GB RAM)**
- [Phi-3 Mini 3.8B](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf)
- [Qwen2.5 3B](https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-GGUF)

Example download:
```bash
# Create models directory
mkdir -p models

# Download using wget or curl
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4.gguf -O models/phi-3-mini-q4.gguf
```

### 2. Add the Model

```bash
scli models add phi-3-mini ./models/phi-3-mini-q4.gguf --default
```

### 3. Start Chatting

```bash
scli chat
```

## Usage

### Interactive Chat Mode

Start an interactive chat session:

```bash
scli chat
```

With specific model:
```bash
scli chat --model tinyllama
```

With custom system prompt:
```bash
scli chat --system "You are a helpful coding assistant"
```

With custom temperature:
```bash
scli chat --temperature 0.8
```

### Single Query Mode

Send a single query:

```bash
scli query "What is Python?"
```

With options:
```bash
scli query "Explain recursion" --model phi-3-mini --temperature 0.5 --max-tokens 500
```

### Interactive Commands

Within the chat interface, you can use these commands:

- `/help` - Show help message
- `/models` - List available models
- `/switch <model>` - Switch to a different model
- `/clear` - Clear current conversation
- `/save` - Save current conversation
- `/history` - Show conversation history
- `/exit` or `/quit` - Exit the application

### Model Management

**List all models:**
```bash
scli models list
```

**Add a model:**
```bash
scli models add <name> <path> [options]

# Examples:
scli models add phi-3 ./models/phi-3-mini-q4.gguf --default
scli models add tinyllama ./models/tinyllama.gguf --context 2048 --temperature 0.7
```

**Remove a model:**
```bash
scli models remove <name>
```

**Show model info:**
```bash
scli models info phi-3-mini
```

### Configuration Management

**Show current configuration:**
```bash
scli config show
```

**Set default model:**
```bash
scli config set-default <model-name>
```

### Conversation History

**List recent conversations:**
```bash
scli history list --limit 20
```

**Clear all history:**
```bash
scli history clear
```

## Configuration

Configuration is stored in `~/.scli/config.yaml`. You can manually edit this file or use the CLI commands.

### Example Configuration

```yaml
default_model: "phi-3-mini"

models:
  phi-3-mini:
    path: "./models/phi-3-mini-q4.gguf"
    type: "llama.cpp"
    parameters:
      context_length: 4096
      temperature: 0.7
      top_p: 0.9
      top_k: 40
      repeat_penalty: 1.1
      n_threads: 4
      n_gpu_layers: 0
      max_tokens: 512

inference:
  max_tokens: 2048
  stream: true
  stop_sequences: []

ui:
  color_scheme: "monokai"
  show_model_name: true
  markdown_rendering: true
  syntax_highlighting: true

history:
  max_conversations: 100
  auto_save: true
  save_path: "./data/history.db"
```

### Configuration Options

**Model Parameters:**
- `context_length`: Model context window size
- `temperature`: Sampling temperature (0.0-2.0, higher = more creative)
- `top_p`: Nucleus sampling parameter (0.0-1.0)
- `top_k`: Top-k sampling parameter
- `repeat_penalty`: Repetition penalty (1.0 = no penalty)
- `n_threads`: Number of CPU threads (null = auto-detect)
- `n_gpu_layers`: Number of layers to offload to GPU (0 = CPU only)
- `max_tokens`: Default maximum tokens to generate

## Performance Tuning

### CPU Optimization

```yaml
parameters:
  n_threads: 8  # Set to your CPU core count
  n_gpu_layers: 0
```

### GPU Acceleration

For CUDA:
```yaml
parameters:
  n_gpu_layers: 35  # Adjust based on your GPU memory
```

### Memory Management

For low-memory systems, use smaller quantized models:
- Q4_K_M: Good quality, ~4GB RAM
- Q4_0: Lower quality, ~3GB RAM
- Q3_K_M: Acceptable quality, ~2.5GB RAM

## Supported Models

SCLI supports any GGUF format model compatible with llama.cpp. Popular options:

### Recommended Models

| Model | Size | RAM | Speed | Quality | Best For |
|-------|------|-----|-------|---------|----------|
| TinyLlama 1.1B | ~700MB | 2GB | ⚡⚡⚡ | ⭐⭐ | Quick responses |
| Phi-3 Mini 3.8B | ~2.3GB | 4GB | ⚡⚡ | ⭐⭐⭐⭐ | Balanced use |
| Qwen2.5 3B | ~2.0GB | 4GB | ⚡⚡ | ⭐⭐⭐⭐ | Coding tasks |
| Gemma 2B | ~1.5GB | 3GB | ⚡⚡⚡ | ⭐⭐⭐ | General chat |

## Extending SCLI

### Adding a Custom Plugin

Create a new plugin in `scli/plugins/models/`:

```python
from scli.plugins.base import ModelPlugin, ModelInfo

class CustomPlugin(ModelPlugin):
    def load_model(self) -> bool:
        # Your loading logic
        pass

    def generate(self, prompt: str, **kwargs):
        # Your generation logic
        pass

    # Implement other required methods...
```

Register the plugin in `model_manager.py`:

```python
PLUGIN_REGISTRY = {
    'llama.cpp': LlamaCppPlugin,
    'custom': CustomPlugin,
}
```

## Troubleshooting

### Model Loading Fails

- Check if the model file exists and path is correct
- Ensure you have enough RAM
- Verify the model is in GGUF format
- Try reducing `n_gpu_layers` if using GPU

### Slow Generation

- Reduce `max_tokens`
- Use a smaller quantized model (Q4, Q3)
- Increase `n_threads` for CPU
- Enable GPU acceleration with `n_gpu_layers`

### Out of Memory

- Use a smaller model
- Reduce `context_length`
- Close other applications
- Use higher quantization (Q4_0, Q3_K_M)

## Development

### Project Structure

```
scli/
├── scli/
│   ├── core/              # Core functionality
│   │   ├── config.py      # Configuration management
│   │   ├── model_manager.py
│   │   └── conversation.py
│   ├── plugins/           # Model plugins
│   │   ├── base.py        # Plugin interface
│   │   └── models/
│   │       └── llama_cpp_plugin.py
│   ├── ui/                # User interface
│   │   ├── formatter.py
│   │   └── interactive.py
│   └── cli.py             # CLI entry point
├── models/                # Model storage
├── data/                  # Conversation history
├── requirements.txt
└── setup.py
```

### Running Tests

```bash
pytest tests/
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

MIT License - see LICENSE file for details

## Acknowledgments

- [llama.cpp](https://github.com/ggerganov/llama.cpp) - Fast LLM inference
- [Hugging Face](https://huggingface.co) - Model distribution
- All contributors to the open-source LLM community

## Support

- Issues: [GitHub Issues](https://github.com/yourusername/scli/issues)
- Discussions: [GitHub Discussions](https://github.com/yourusername/scli/discussions)

---

**Built with ❤️ for offline AI enthusiasts**
