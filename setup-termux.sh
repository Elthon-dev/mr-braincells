#!/data/data/com.termux/files/usr/bin/bash
echo "=== Mr. Braincells Termux Setup ==="

# Update packages
pkg update -y && pkg upgrade -y

# Install dependencies
pkg install -y python python-pip git curl wget ollama

# Install Python packages
pip install -r requirements.txt

# Setup CLI globally
chmod +x mr-braincells
cp mr-braincells $PREFIX/bin/mr-braincells 2>/dev/null || ln -s $(pwd)/mr-braincells $PREFIX/bin/mr-braincells 2>/dev/null

# Start ollama if available
if command -v ollama >/dev/null 2>&1; then
    ollama serve > /dev/null 2>&1 &
    sleep 5
    ollama pull llama3.2 2>/dev/null || true
    ollama pull mistral 2>/dev/null || true
    ollama pull deepseek-coder 2>/dev/null || true
    ollama pull cogito 2>/dev/null || true
fi

echo "=== Setup Complete ==="
echo "Run: mr-braincells"
echo "Connection credentials printed below:"
echo "--- CREDENTIALS ---"
echo "Ollama: http://localhost:11434"
echo "Models: $(ollama list 2>/dev/null | wc -l) available"
