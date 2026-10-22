# Offline Chatbot with Ollama

A beginner-friendly terminal chatbot that runs a local language model with [Ollama](https://ollama.com/) and Python. It demonstrates conversation history, message roles, and the context-window concept.

> **Privacy note:** Once the model is downloaded, prompts are sent to the local Ollama service rather than a hosted model API. Ollama still needs to be running on your computer. Downloading the model requires an internet connection.

## Project files

```text
offline-chatbot-ollama/
├── offline_chatbot.py   # Chatbot source code
├── NOTES.md             # Code flow and learning notes
└── README.md            # Setup and usage instructions
```

## Requirements

- Windows, macOS, or Linux
- Python 3.10 or newer
- Ollama installed
- Enough RAM and disk space for the model you choose
- Internet connection to install packages and download the model

The example uses `qwen2.5:14b`. A 14B model can be demanding, so if it runs too slowly or does not fit your hardware, choose a smaller model and update `MODEL_NAME` in `offline_chatbot.py` to match.

## 1. Install Ollama

1. Open the official website: <https://ollama.com/>
2. Download and install Ollama for your operating system.
3. Open a new terminal and check that Ollama is available:

   ```bash
   ollama --version
   ```

Ollama normally runs a local service at `http://localhost:11434`.

## 2. Download the model

In a terminal, run:

```bash
ollama pull qwen2.5:14b
```

This downloads the model files. It may take time and disk space.

Check the models installed locally:

```bash
ollama list
```

You can also test the model directly:

```bash
ollama run qwen2.5:14b
```

Type a message to test it. Use `Ctrl+D` on macOS/Linux or `Ctrl+Z`, then Enter, on Windows to exit the interactive session. The exact exit behavior may vary by terminal.

If you choose a different model, use that exact model tag in the Python file too.

## 3. Create a Python virtual environment (recommended)

Open a terminal in this project folder.

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

If PowerShell blocks activation, you can use Command Prompt instead:

```bat
.venv\Scripts\activate.bat
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

## 4. Install the Python package

```bash
python -m pip install openai
```

The project uses the `openai` Python library, but the client is configured to send requests to Ollama's local OpenAI-compatible endpoint.

## 5. Run the chatbot

Make sure Ollama is running and the model has been downloaded. Then run:

```bash
python offline_chatbot.py
```

Example:

```text
Offline Chatbot started (model: qwen2.5:14b)
Type 'e' or 'exit' to quit.

You: Hi, my name is Vishal.
AI: Hello Vishal! How can I help you?

You: What is my name?
AI: Your name is Vishal.
```

The actual answer may differ. The example only illustrates how conversation history can provide context.

Enter `e` or `exit` to quit the program.

## How does memory work?

The `messages` list stores user messages and assistant replies in Python. Before every request, the program sends the conversation history to the model. This lets the model respond using earlier messages from the current session.

The model does not gain permanent memory from this list. Restarting the program clears the list, and a long conversation can eventually reach the model's context-window limit.

See [`NOTES.md`](NOTES.md) for the full code flow, roles, context-window explanation, and limitations.

## Troubleshooting

### `Connection error` or connection refused

- Check that Ollama is installed and running.
- Run `ollama list` in a terminal.
- Confirm the local service address in the code is `http://localhost:11434/v1`.

### Model not found

Run:

```bash
ollama pull qwen2.5:14b
ollama list
```

Make sure `MODEL_NAME` in `offline_chatbot.py` exactly matches the installed model tag.

### The model is slow or the computer runs out of memory

A 14B model may be too large for some computers. Pull a smaller Ollama model, then change `MODEL_NAME` in `offline_chatbot.py` to the model tag you installed. Model speed depends on hardware and model configuration.

### Python cannot import `openai`

Activate your virtual environment and run:

```bash
python -m pip install openai
```

## Upload this project to GitHub

1. Create a new, empty repository on GitHub, for example `offline-chatbot-ollama`.
2. Put `offline_chatbot.py`, `NOTES.md`, and `README.md` in the same project folder.
3. Open a terminal in that folder and run:

   ```bash
   git init
   git add offline_chatbot.py NOTES.md README.md
   git commit -m "Add local Ollama chatbot with conversation history"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/offline-chatbot-ollama.git
   git push -u origin main
   ```

Replace `YOUR-USERNAME` with your GitHub username and use the URL of your own repository.

## Security and privacy

- Do not commit API keys, passwords, or other secrets.
- The `"ollama"` API key string is a placeholder for this local configuration, not a personal API key.
- This code does not call a hosted OpenAI API; its configured endpoint is the local Ollama service.
- Model downloads and Python package installation do require internet access.

## Learning goals

After studying this project, you should understand:

- How to connect Python to a local model through Ollama
- How chat messages use `role` and `content`
- Why both user messages and assistant replies are stored
- How resending history creates conversational context
- What a context window is, and why conversation history is not unlimited
