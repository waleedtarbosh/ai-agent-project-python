<p align="center">
  <img src="assets/logo.png" alt="Boot.dev Logo" width="280" />
</p>

<h1 align="center">🤖 AI Agent Project</h1>

<p align="center">
  <img src="assets/profile.webp" alt="Boot.dev Profile Avatar" width="120" style="border-radius: 50%;" />
</p>

<p align="center">
  <strong>An autonomous AI coding agent that finds and fixes bugs — all by itself.</strong><br/>
  Powered by Google Gemini 2.5 Flash &amp; built as part of the <a href="https://www.boot.dev/">Boot.dev</a> curriculum.
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white" alt="Python 3.12+" /></a>
  <a href="https://ai.google.dev/"><img src="https://img.shields.io/badge/Google%20Gemini-2.5--flash-4285F4?logo=google&logoColor=white" alt="Google Gemini" /></a>
  <a href="https://docs.astral.sh/uv/"><img src="https://img.shields.io/badge/uv-package%20manager-5C4EE5" alt="uv" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License" /></a>
</p>

---

## 🏆 Course Completion Certificate

This project was completed as part of the **Boot.dev** backend development curriculum.

<p align="center">
  <a href="https://www.boot.dev/certificates/c72ee9f4-a798-49ca-8068-ccd8e5832750">
    <img src="https://qvault-webapp-dynamic-assets.storage.googleapis.com/certificates/c72ee9f4-a798-49ca-8068-ccd8e5832750.jpeg" alt="Boot.dev Course Completion Certificate" width="700" />
  </a>
</p>

<p align="center">
  <em>🔗 <a href="https://www.boot.dev/certificates/c72ee9f4-a798-49ca-8068-ccd8e5832750">View Certificate →</a></em>
</p>

---

## 📚 Course Chapters Completed

**What will you learn?**  
Write a toy agentic code editor in Python, similar to Claude Code or Cursor's Agent Mode. Understand how agents work from scratch by using the Google Gemini API to create an LLM-powered code agent. You'll use function calling and feedback loops to build an agent that can find and fix bugs in a real project!

### Chapter List
1. **LLMs** — Learn how LLMs work and send prompts to the Gemini API using the Python client library
2. **Functions** — Write the functions your AI agent will need to modify files and run Python code
3. **Function Calling** — Give your AI agent the ability to call functions based on its system prompt and context window
4. **Agents** — Give your tool a proper feedback loop to make it truly "agentic" and fix a real bug

---

## 📖 Table of Contents

- [Course Chapters Completed](#-course-chapters-completed)
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Tool Functions Reference](#-tool-functions-reference)
- [Sample Target Codebase](#-sample-target-codebase)
- [Testing](#-testing)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

- **Autonomous Bug Fixing** — Describe a bug in natural language; the agent investigates, patches code, and verifies the fix automatically.
- **Agentic Tool-Use Loop** — Implements a multi-turn function-calling loop (up to 20 iterations) where the LLM decides which tool to invoke next.
- **Sandboxed Execution** — All file reads, writes, and code execution are restricted to a configurable working directory to prevent unintended side effects.
- **Four Built-in Tools** — The agent can list directory contents, read files, write/overwrite files, and execute Python scripts.
- **Verbose Mode** — Optional `--verbose` flag to trace every tool call and intermediate response for debugging.
- **File Truncation Safety** — Large files are automatically truncated at 10,000 characters to stay within LLM context limits.

---

## 🧠 How It Works

```
┌──────────────┐     prompt      ┌──────────────────┐
│   CLI Input  │ ──────────────► │  Google Gemini    │
│  (main.py)   │                 │  2.5 Flash Model  │
└──────────────┘                 └────────┬─────────┘
                                          │
                              function_call │ (tool use)
                                          ▼
                                 ┌────────────────┐
                                 │ call_function() │
                                 │  (dispatcher)   │
                                 └───────┬────────┘
                                         │
                    ┌────────────────────┼────────────────────┐
                    │                    │                    │
            ┌───────▼──────┐   ┌────────▼───────┐   ┌───────▼──────┐
            │ get_files_info│   │get_file_content│   │  write_file  │
            │              │   │                │   │              │
            └──────────────┘   └────────────────┘   └──────────────┘
                                                     ┌───────▼──────┐
                                                     │run_python_file│
                                                     └──────────────┘
```

1. The user provides a natural-language prompt (e.g., *"the calculator tests are failing, fix the bug"*).
2. `main.py` sends the prompt plus a system instruction to **Gemini 2.5 Flash** with the four tool schemas registered.
3. The model returns one or more **function calls** instead of (or before) a text answer.
4. `call_function.py` dispatches each call to the matching Python function, executes it inside the sandboxed working directory, and returns the result.
5. The result is appended to the conversation history and sent back to the model.
6. Steps 3–5 repeat (up to 20 iterations) until the model responds with final text, indicating the task is complete.

---

## 🛠 Tech Stack

<p align="center">
  <img src="assets/git.svg" alt="Git" width="40" height="40" />&nbsp;&nbsp;&nbsp;
  <img src="assets/github.svg" alt="GitHub" width="40" height="40" />&nbsp;&nbsp;&nbsp;
  <img src="assets/linux.svg" alt="Linux" width="40" height="40" />&nbsp;&nbsp;&nbsp;
  <img src="assets/ubuntu.svg" alt="Ubuntu" width="40" height="40" />&nbsp;&nbsp;&nbsp;
  <img src="assets/terminal.svg" alt="Terminal" width="40" height="40" />
</p>

| Category           | Technology                                                                  |
| ------------------ | --------------------------------------------------------------------------- |
| **Language**        | Python 3.12+                                                                |
| **LLM**            | Google Gemini 2.5 Flash (via `google-genai` SDK v1.12.1)                    |
| **AI SDK**          | [`google-genai`](https://pypi.org/project/google-genai/) 1.12.1             |
| **Legacy SDK**      | [`google-generativeai`](https://pypi.org/project/google-generativeai/) ≥ 0.8.6 |
| **Env Management**  | [`python-dotenv`](https://pypi.org/project/python-dotenv/) 1.1.0           |
| **Package Manager** | [uv](https://docs.astral.sh/uv/)                                           |
| **Version Control** | <img src="assets/git.svg" alt="" width="14" height="14" /> Git / <img src="assets/github.svg" alt="" width="14" height="14" /> GitHub |
| **OS / Shell**      | <img src="assets/linux.svg" alt="" width="14" height="14" /> Linux · <img src="assets/ubuntu.svg" alt="" width="14" height="14" /> Ubuntu · <img src="assets/terminal.svg" alt="" width="14" height="14" /> Terminal |
| **Testing**         | `unittest` (standard library)                                               |

---

## 🚀 Getting Started

### Prerequisites

| Requirement        | Minimum Version | Install Guide                                                                    |
| ------------------ | --------------- | -------------------------------------------------------------------------------- |
| **Python**         | 3.12            | [python.org](https://www.python.org/downloads/)                                  |
| **uv**             | latest          | [docs.astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/)    |
| **Gemini API Key** | —               | [aistudio.google.com](https://aistudio.google.com/app/apikey)                    |

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/ai-agent-project-python.git
cd ai-agent-project-python

# 2. Install dependencies with uv
uv sync

# 3. Copy the example environment file and add your API key
cp .env.example .env    # Linux / macOS
copy .env.example .env  # Windows
```

### Environment Variables

Create a `.env` file in the project root (or edit the one copied above). The following variable is **required**:

```dotenv
# .env
GEMINI_API_KEY=your_gemini_api_key_here
```

| Variable        | Required | Description                                                                                           |
| --------------- | -------- | ----------------------------------------------------------------------------------------------------- |
| `GEMINI_API_KEY` | ✅ Yes   | Your Google Gemini API key. Obtain one free at [AI Studio](https://aistudio.google.com/app/apikey).    |

---

## 💻 Usage

Run the agent by passing a natural-language prompt as a CLI argument:

```bash
# Basic usage
uv run python main.py "the calculator tests are failing, find and fix the bug"

# With verbose output (shows every tool call and intermediate result)
uv run python main.py --verbose "the subtract function returns wrong results"
```

The agent will autonomously:
1. 📂 Explore the `./calculator` directory structure
2. 📄 Read the relevant source files
3. 🐛 Identify the bug
4. ✏️ Write a fix using `write_file`
5. ✅ Run the tests to verify the fix
6. 💬 Report the result

### Example Session (Verbose)

```
--- Iteration 1 ---
Calling function: get_files_info({'directory': '.'})
-> {'result': '- README.md: file_size=12 bytes, is_dir=False\n- lorem.txt: ...'}

--- Iteration 2 ---
Calling function: get_file_content({'file_path': 'pkg/calculator.py'})
-> {'result': 'from collections.abc import Callable\n\nclass Calculator: ...'}

--- Iteration 3 ---
Calling function: write_file({'file_path': 'pkg/calculator.py', 'content': '...'})
-> {'result': 'Successfully wrote to "pkg/calculator.py" (1923 characters written)'}

--- Iteration 4 ---
Calling function: run_python_file({'file_path': 'tests.py'})
-> {'result': 'STDOUT:\n..........\n------\nRan 9 tests in 0.001s\n\nOK'}

Final Response:
I found and fixed the bug in the calculator...
```

---

## 📁 Project Structure

```
ai-agent-project-python/
│
├── assets/                    # 🖼️  Project images & icons
│   ├── logo.png               #    Boot.dev logo
│   ├── profile.webp           #    Profile avatar
│   ├── git.svg                #    Git icon
│   ├── github.svg             #    GitHub icon
│   ├── linux.svg              #    Linux icon
│   ├── terminal.svg           #    Terminal icon
│   └── ubuntu.svg             #    Ubuntu icon
│
├── functions/                 # 🔧 Tool implementations (sandboxed file I/O)
│   ├── get_files_info.py      #    List directory contents with size & type info
│   ├── get_file_content.py    #    Read a file (with truncation at MAX_CHARS)
│   ├── write_file.py          #    Write or overwrite a file
│   └── run_python_file.py     #    Execute a Python script in a subprocess
│
├── calculator/                # 🧮 Sample target codebase the agent operates on
│   ├── main.py                #    CLI entry point for the calculator app
│   ├── tests.py               #    Unit tests (unittest) for the calculator
│   ├── lorem.txt              #    Test fixture file
│   ├── README.md              #    Stub README
│   └── pkg/
│       ├── calculator.py      #    Core infix expression evaluator
│       └── render.py          #    JSON output formatter
│
├── main.py                    # ⭐ Entry point — CLI arg parsing & agentic loop
├── config.py                  # Global constants (MAX_CHARS = 10,000)
├── prompts.py                 # System prompt for the Gemini model
├── call_function.py           # Tool dispatcher — schema registry & function router
│
├── test_get_file_content.py   # Manual test script for get_file_content
├── test_get_files_info.py     # Manual test script for get_files_info
├── test_run_python_file.py    # Manual test script for run_python_file
├── test_write_file.py         # Manual test script for write_file
│
├── .env.example               # Template for required environment variables
├── .gitignore                 # Git ignore rules
├── .python-version            # Pins Python to 3.12
├── pyproject.toml             # Project metadata & dependencies (uv/PEP 621)
└── uv.lock                   # Lockfile for deterministic installs
```

---

## 🔧 Tool Functions Reference

The agent has access to four tools. Each tool enforces **directory sandboxing** — all paths are resolved relative to a `working_directory` (default: `./calculator`) and any attempt to escape it is rejected.

| Tool                 | Description                                                                                       |
| -------------------- | ------------------------------------------------------------------------------------------------- |
| `get_files_info`      | Lists all files and subdirectories, returning each item's name, size in bytes, and type.          |
| `get_file_content`    | Reads and returns file contents. Files larger than **10,000 characters** are automatically truncated. |
| `write_file`          | Writes (or overwrites) a file. Parent directories are created automatically if needed.            |
| `run_python_file`     | Executes a Python file in a subprocess with optional args. Enforces a **30-second timeout**.      |

---

## 🧮 Sample Target Codebase

The `calculator/` directory ships as a built-in sample project for the agent to operate on. It contains:

- An **infix expression evaluator** (`calculator/pkg/calculator.py`) that supports `+`, `-`, `*`, `/` with correct operator precedence.
- A **CLI wrapper** (`calculator/main.py`) that accepts expressions like `"3 * 4 + 5"` and outputs JSON.
- **9 unit tests** (`calculator/tests.py`) covering arithmetic, edge cases, and error handling.

You can intentionally introduce bugs into the calculator code and then ask the agent to find and fix them!

---

## 🧪 Testing

### Agent Tool Tests

Manual test scripts are provided for each tool function:

```bash
uv run python test_get_files_info.py
uv run python test_get_file_content.py
uv run python test_write_file.py
uv run python test_run_python_file.py
```

### Calculator Unit Tests

```bash
cd calculator
python -m unittest tests.py -v
```

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** this repository
2. **Create a feature branch:**
   ```bash
   git checkout -b feat/my-new-feature
   ```
3. **Make your changes** and ensure all tests pass
4. **Commit** with a descriptive message:
   ```bash
   git commit -m "feat: add support for parenthesized expressions"
   ```
5. **Push** to your fork and open a **Pull Request**

### Guidelines

- Follow [PEP 8](https://peps.python.org/pep-0008/) style conventions
- Add tests for any new tool functions
- Keep tool functions sandboxed — never allow file access outside the working directory


---

## 👨‍💻 About Me

**Waleed Tarbosh** — Aspiring developer, currently learning backend development through Boot.dev.

- 🐙 **GitHub:** [@waleedtarbosh](https://github.com/waleedtarbosh)
- 📧 **Email:** [waleedtarbush@gmail.com](mailto:waleedtarbush@gmail.com)
- 🎓 **Boot.dev Profile:** [View Certificate](https://www.boot.dev/certificates/c72ee9f4-a798-49ca-8068-ccd8e5832750)
---



## 📄 License

This project is distributed under the **MIT License**. See [`LICENSE`](LICENSE) for details.

---

<p align="center">
  <img src="assets/logo.png" alt="Boot.dev" width="120" /><br/>
  Built with ❤️ as part of the <a href="https://www.boot.dev/">Boot.dev</a> curriculum<br/><br/>
  <a href="https://www.boot.dev/certificates/c72ee9f4-a798-49ca-8068-ccd8e5832750">
    🏆 View My Certificate
  </a>
</p>

<p align="center">
  <a href="#-ai-agent-project">⬆️ Back to Top</a>
</p>