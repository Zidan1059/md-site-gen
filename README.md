# md-site-gen

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Build Status](https://img.shields.io/badge/tests-passing-brightgreen.svg)

A lightweight, zero-bloat static site generator written in Python. It converts a directory of Markdown files with YAML frontmatter into a styled HTML website with auto-generated navigation, an index page, and a built-in local preview server.

---

## Features

- **YAML Frontmatter Support:** Define custom page titles, dates, and metadata at the top of any `.md` file.
- **Extended Markdown Parsing:** Supports fenced code blocks, tables, and auto-generated tables of contents out of the box.
- **Jinja2 Templating:** Clean separation between content and HTML layout (`base.html`, `page.html`, `index.html`).
- **Auto-Generated Navigation:** Dynamically builds a top navigation bar and a central index page from your Markdown files.
- **Built-in Preview Server:** Spin up a local HTTP server immediately after building using the `--serve` flag.

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Zidan1059/md-site-gen.git
   cd md-site-gen
   ```

2. **Create a virtual environment and install in editable mode:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -e .
   ```

---

## Quick Start

1. **Add Markdown files** to the `content/` directory (see [Writing Content](#writing-content) below).
2. **Build the site and launch the local preview server:**
   ```bash
   sitegen --serve
   ```
3. Open your browser and navigate to `http://127.0.0.1:8000`.

---

## CLI Options

| Flag | Default | Description |
| :--- | :--- | :--- |
| `--content` | `content` | Path to the directory containing source `.md` files. |
| `--templates` | `templates` | Path to the directory containing Jinja2 HTML templates. |
| `--static` | `static` | Path to static assets (CSS, images) copied to the output folder. |
| `--output` | `dist` | Destination directory for the generated HTML site. |
| `--serve` | `False` | Start a local HTTP preview server after building. |
| `--port` | `8000` | Port number used by the local preview server. |

**Example with custom paths:**
```bash
sitegen --content ./docs --output ./public --serve --port 3000
```

---

## Writing Content

Place `.md` files inside `content/`. Optional YAML frontmatter between `---` markers sets page metadata; if omitted, the filename is automatically formatted as the page title.

```markdown
---
title: Getting Started
date: 2026-11-17
---

Welcome to your custom **static site generator**.

| Feature | Supported |
| :--- | :--- |
| Tables | Yes |
| Code Blocks | Yes |
```

---

## Project Structure

```text
md-site-gen/
├── content/              # Markdown source files
├── templates/            # Jinja2 HTML templates
│   ├── base.html
│   ├── index.html
│   └── page.html
├── static/               # CSS and static assets
│   └── style.css
├── sitegen/              # Core Python package
│   ├── __init__.py
│   ├── builder.py        # Markdown parsing and HTML generation
│   └── cli.py            # CLI argument parsing and preview server
├── tests/                # Unit tests
│   └── test_builder.py
├── .gitignore
├── LICENSE
├── pyproject.toml        # Package metadata and dependencies
└── README.md
```

---

## Running Tests

Install `pytest` and run the test suite to verify Markdown parsing and frontmatter extraction:

```bash
pip install pytest
pytest
```

---

## License

This project is licensed under the MIT License.
