# Quick Start Guide

Get SCLI up and running in 5 minutes!

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
pip install -e .
```

## Step 2: Download a Model

Choose and download a model based on your hardware:

### For Low-End Devices (2-4GB RAM)
```bash
python download_models.py qwen2.5-0.5b
# Or
python download_models.py tinyllama
```

### For Mid-Range Devices (4-8GB RAM)
```bash
python download_models.py phi-3-mini
# Or
python download_models.py qwen2.5-3b
```

## Step 3: Add the Model to SCLI

After downloading, add the model:

```bash
# For Phi-3 Mini
scli models add phi-3-mini ./models/phi-3-mini-4k-instruct-q4.gguf --default

# For TinyLlama
scli models add tinyllama ./models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf --default

# For Qwen2.5 3B
scli models add qwen2.5-3b ./models/qwen2.5-3b-instruct-q4_k_m.gguf --default

# For Qwen2.5 0.5B
scli models add qwen2.5-0.5b ./models/qwen2.5-0.5b-instruct-q4_k_m.gguf --default
```

## Step 4: Start Chatting!

```bash
scli chat
```

That's it! You're now running a fully offline AI assistant.

## Quick Commands Reference

```bash
# Start chat
scli chat

# Single query
scli query "What is Python?"

# List models
scli models list

# Switch model (in chat)
/switch <model-name>

# Get help
scli --help
scli chat --help
```

## Troubleshooting

### "Model not found" error
- Check that the model file exists in the `models/` directory
- Verify the path when adding the model

### Out of memory
- Use a smaller model (qwen2.5-0.5b or tinyllama)
- Close other applications
- Reduce context_length in config

### Slow responses
- Use a smaller model
- Increase n_threads in configuration
- Consider using GPU acceleration if available

## Next Steps

- Read the full [README.md](README.md) for advanced features
- Customize your configuration in `~/.scli/config.yaml`
- Try different models for different tasks
- Enable GPU acceleration for faster inference

## Need Help?

- Check [README.md](README.md) for detailed documentation
- Open an issue on GitHub
- Join our community discussions

Happy chatting! 🚀
