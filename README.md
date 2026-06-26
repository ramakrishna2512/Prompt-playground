# 🧪 Prompt Playground

A Streamlit app for saving, organizing, and testing multiple system prompts against local LLMs via [Ollama](https://ollama.com/) — useful for comparing how different prompt versions behave before committing to one.

## Features

- Save multiple system prompts and keep them around for reuse
- Test any saved prompt against a local Ollama model
- Swap models without changing your prompt library

## Prerequisites

1. Install [Ollama](https://ollama.com/).
2. Pull the model(s) you want to test with, e.g. `ollama pull llama3`.

## Installation

```bash
git clone https://github.com/ramakrishna2512/Prompt-playground.git
cd Prompt-playground
python -m venv venv && source venv/bin/activate   # optional but recommended
pip install -r requirements.txt
```

## Usage

```bash
streamlit run app.py
```

## Stack

`Streamlit` `Python` `Ollama`

## Related

Part of a broader set of local-LLM tooling — see the [AI Agents Suite](https://github.com/ramakrishna2512/ai-agents-hub) for single-purpose agents built the same way.

