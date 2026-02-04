# claudepython

A Python project template with **uv**, **Jupyter notebooks**, and **Claude Code** — all running inside a GitHub Codespace. No local setup required.

![Open in GitHub Codespaces](https://github.com/codespaces/badge?style=flat-right&logo=codespaces&color=6e40c9&labelColor=fff)](https://codespaces.new/PulfordJ/claudepython)
![Python 3.12](https://img.shields.io/badge/Python-3.12-3572A5?style=flat-right&logo=python&logoColor=fff)

---

## What you get

| Tool | What it does |
|---|---|
| **uv** | Fast Python package manager — replaces pip entirely |
| **Jupyter** | Notebook editing and execution via the VS Code extension |
| **Claude Code** | AI coding assistant, available in the terminal (`claude`) |
| **Codespace** | All of the above spins up in a browser tab — nothing to install locally |

---

## Prerequisites

- A **GitHub account** (that's it for the Codespace path)
- For running locally: **Docker Desktop** + the **VS Code Dev Containers** extension

---

## Quick start

1. Click the **Open in GitHub Codespaces** badge above (or go to **Code → Codespaces** in this repo).
2. The container builds automatically — `uv sync` installs all dependencies and sets up the Jupyter kernel.
3. Open `notebooks/sample.ipynb` in the file explorer — it runs immediately.
4. Type `claude` in the integrated terminal to start Claude Code.

---

## Project layout

```
.
├── .devcontainer/
│   └── devcontainer.json   # Codespace / devcontainer definition
├── notebooks/
│   └── sample.ipynb        # Sample notebook (numpy, pandas, matplotlib)
├── src/
│   └── hello.py            # Sample Python module
├── pyproject.toml          # uv project config and dependencies
├── uv.lock                 # Locked dependency versions (committed for reproducibility)
├── .gitignore
└── README.md
```

---

## Common uv commands

```bash
uv add <package>            # add a runtime dependency
uv add --dev <package>      # add a dev dependency
uv run python src/hello.py  # run a script inside the managed venv
uv run pytest               # run tests
uv sync                     # install / update deps from pyproject.toml
```

Any package added with `uv add` is immediately available in notebooks — the Jupyter kernel points at the same `.venv`.

---

## Claude Code auth

Claude Code needs an API key. The cleanest way to provide it in a Codespace:

1. Go to [github.com/settings/codespaces](https://github.com/settings/codespaces)
2. Add a secret named `ANTHROPIC_API_KEY` with your key from [console.anthropic.com](https://console.anthropic.com/account/keys)

The secret is injected as an environment variable — nothing is stored in the repo.

---

## Local development

1. Clone the repo.
2. Open it in VS Code — it will prompt you to reopen inside the dev container.
3. Everything works identically to the Codespace experience.

---

## License

MIT
