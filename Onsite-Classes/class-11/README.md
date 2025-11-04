# Class 11 — Working with LLM CLIs

In this class, we explored command‑line interfaces (CLIs) and SDKs for working with modern Large Language Models (LLMs). We looked at tools like Gemini, Claude, and Qwen, how to configure API keys, and how to run models from your terminal and scripts.

## Tools Discussed

- Gemini (Google) — API and SDKs (Python/Node)
- Claude (Anthropic) — SDKs and community CLIs
- Qwen (Alibaba) — SDKs and agent tooling
- General CLI patterns: auth, config, prompts, streaming, and piping

---

## Gemini Installation

Below are practical steps to install and configure Gemini with Python and Node.js. Choose the stack you prefer; both require an API key from Google AI Studio.

### Prerequisites

- A Google account and access to Google AI Studio
- An API key from AI Studio
- Python 3.9+ or Node.js 18+

### 1) Get a Gemini API Key

1. Go to AI Studio: https://aistudio.google.com
2. Create a new API key (note it down).

### 2) Save the API Key as an Environment Variable

Use the name `GEMINI_API_KEY`.

- Windows (PowerShell):
  - Current shell only: `$env:GEMINI_API_KEY = "<your_api_key>"`
  - Persist for your user: `[Environment]::SetEnvironmentVariable("GEMINI_API_KEY", "<your_api_key>", "User")`

- macOS/Linux (bash/zsh):
  - Current shell only: `export GEMINI_API_KEY=<your_api_key>`
  - Persist: add the line above to your `~/.bashrc`, `~/.zshrc`, or `~/.profile` and reload the shell.

### 3) Python Setup

1. Install the official SDK:
   ```bash
   pip install google-generativeai
   ```
2. Quick verification (save as `check_gemini.py` and run `python check_gemini.py`):
   ```python
   import os
   import google.generativeai as genai

   key = os.getenv("GEMINI_API_KEY")
   if not key:
       raise SystemExit("Set GEMINI_API_KEY before running.")

   genai.configure(api_key=key)
   print("Gemini SDK installed and API key configured.")
   ```

### 4) Node.js Setup

1. Initialize a project (optional):
   ```bash
   npm init -y
   ```
2. Install the official SDK:
   ```bash
   npm install @google/generative-ai
   ```
3. Quick verification (save as `check-gemini.mjs` and run `node check-gemini.mjs`):
   ```js
   import process from 'node:process';
   import { GoogleGenerativeAI } from '@google/generative-ai';

   const key = process.env.GEMINI_API_KEY;
   if (!key) throw new Error('Set GEMINI_API_KEY before running.');

   const genAI = new GoogleGenerativeAI(key);
   console.log('Gemini SDK installed and API key configured.');
   ```

### Common Issues

- Invalid key or missing env var: ensure `GEMINI_API_KEY` is set in the same shell.
- Proxy/firewall restrictions: your environment must allow outbound HTTPS to Google APIs.
- Python: upgrade tooling if installs fail: `python -m pip install --upgrade pip setuptools wheel`.
- Node: ensure Node 18+ and a clean `npm` cache if dependency resolution errors occur.

---

## Claude and Qwen (Brief)

- Claude (Anthropic): use the official Python/JS SDKs; community CLIs exist but vary. You’ll still need an Anthropic API key.
- Qwen (Alibaba Cloud): use the official SDKs or agent framework; requires appropriate credentials depending on the service.

For each vendor, the setup pattern mirrors Gemini: obtain an API key, save it as an environment variable, install the SDK/CLI, and verify with a minimal script.

---

## Browser Game

A simple browser version of the Number Guessing game is included.

- Open `web/index.html` in your browser (double‑click it or drag it into a tab).
- Guess a number between 1–100. The page will tell you if you’re too high or too low and count attempts.
- Click “🔁 Play again” to restart at any time.
