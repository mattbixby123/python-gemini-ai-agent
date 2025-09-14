# Python Gemini AI Agent

A command-line AI agent powered by Google's Gemini API that provides intelligent responses to user queries.

## Features

- 🤖 Powered by Google's Gemini 2.0 Flash model
- 💬 Simple command-line interface
- 📊 Verbose mode with token usage statistics
- 🔐 Secure API key management with environment variables

## Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) package manager
- Google Gemini API key

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/python-gemini-ai-agent.git
   cd python-gemini-ai-agent
   ```

2. **Set up virtual environment:**
   ```bash
   uv venv
   source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   uv add google-genai==1.12.1 python-dotenv==1.1.0
   ```

4. **Configure environment variables:**
   Create a `.env` file in the project root:
   ```bash
   echo "GEMINI_API_KEY=your_actual_api_key_here" > .env
   ```

   > ⚠️ **Important**: Never commit your `.env` file to version control. It's already included in `.gitignore`.

## Usage

### Basic Usage
```bash
uv run main.py "What is the color of the sky?"
```

### Verbose Mode
Get additional information about token usage:
```bash
uv run main.py "What is the color of the sky?" --verbose
```

### Example Output
```
The sky appears blue to us on a clear day due to Rayleigh scattering...
```

With verbose mode:
```
The sky is blue.
User prompt: What is the color of the sky?
Prompt tokens: 8
Response tokens: 6
```

## Project Structure

```
aiAgent/
├── .env                 # Environment variables (not tracked)
├── .gitignore          # Git ignore rules
├── .venv/              # Virtual environment (not tracked)
├── main.py             # Main application entry point
├── pyproject.toml      # Project configuration
└── README.md           # This file
```

## API Reference

The agent uses the Gemini 2.0 Flash model (`gemini-2.0-flash-001`) for generating responses.

### Command Line Arguments

- **Positional argument**: Your question or prompt
- **`--verbose`**: Display token usage statistics

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Troubleshooting

### Common Issues

**Import errors in VS Code:**
- Ensure VS Code is using the correct Python interpreter from `.venv`
- Use `Cmd+Shift+P` → "Python: Select Interpreter" → select `.venv/bin/python`

**API key issues:**
- Verify your `.env` file contains `GEMINI_API_KEY=your_key`
- Check that your API key is valid and has proper permissions

**uv command not found:**
- Install uv: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Restart your terminal or source your shell profile

## Roadmap

- [ ] Add conversation history support
- [ ] Implement different model options
- [ ] Add configuration file support
- [ ] Create interactive mode
- [ ] Add response formatting options

---

Built with ❤️ using Google's Gemini API and Python