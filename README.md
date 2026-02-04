# claudepython

A Python project template that runs in **GitHub Codespaces** with:

| Tool | Role |
|---|---|
| **uv** | Package manager (replaces pip) |
| **Python 3.12** | Runtime |
| **Jupyter** (VS Code extension) | Notebook editing & execution |
| **Claude Code** | AI coding assistant in the terminal |

---

## Quick start

1. Open a Codespace from the repo's **Code -> Codespaces** menu (or click the badge below once the repo is public/shared).
2. The container builds automatically — `uv sync` runs, installs all deps, and sets up the Jupyter kernel.
3. Open `notebooks/sample.ipynb` in the file explorer — it just works.
4. Type `claude` in the terminal to start Claude Code.

---

## Project layout

```
.
├── .devcontainer/
│   └── devcontainer.json   # Codespace definition
├── notebooks/
│   └── sample.ipynb        # Sample notebook
├── src/
│   └── hello.py            # Sample module
├── pyproject.toml          # uv project config + deps
├── .gitignore
└── README.md
```

---

## Common uv commands

```bash
uv add <package>            # add a dependency
uv add --dev <package>      # add a dev dependency
uv run python src/hello.py  # run a script inside the managed venv
uv run pytest               # run tests
uv sync                     # install/update deps from pyproject.toml
```

---

## Adding packages to notebooks

```bash
uv add pandas numpy matplotlib   # already in pyproject.toml
uv sync                          # refresh the venv
```

The notebook kernel points at `.venv/bin/python`, so any package installed via `uv add` is immediately available.

---

## Local development (without Codespaces)

Requires **Docker Desktop** and the **VS Code Dev Containers** extension.

1. Clone the repo.
2. Open in VS Code — it will prompt you to reopen in a container.
3. Everything else is identical to the Codespace experience.
