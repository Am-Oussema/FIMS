# FIMS – File Integrity Monitoring System
![Status](https://img.shields.io/badge/status-active-brightgreen)
[![Python CI (dev)](https://github.com/Am-Oussema/FIMS/actions/workflows/python-ci.yml/badge.svg?branch=dev)](https://github.com/Am-Oussema/FIMS/actions/workflows/python-ci.yml)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey)
![Type](https://img.shields.io/badge/type-CLI_tool-purple)


FIMS is a lightweight and efficient tool for detecting changes in files or folders  
by using **SHA-256 hashing** and comparing snapshots over time.

Ideal for developers, students, cybersecurity learners, or anyone needing fast and simple file change detection.

---

## 📌 Features

- 🧩 Create snapshots of any directory  
- 🔍 Compare a directory with its previous snapshot  
- 🚨 Detect **added**, **removed**, and **modified** files  
- 🗂 All snapshots stored locally in a JSON format  
- ⚡ Fast and minimal — no database or heavy dependencies  
- 🖥️ Cross-platform (Windows & Linux)
- 🔧 Exposed as a CLI command (fims)

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Am-Oussema/FIMS
cd FIMS
```

Install the package in development mode (recommended during development):

```bash
pip install -e .
```

This makes the `fims` command available globally.

---

## 🛠️ Usage

### ✔️ Create a snapshot

Using the installed CLI:

```bash
fims create --path "C:\path\to\folder"
```

Or using the Python script directly:

```bash
python src/fims/main.py create --path "C:\path\to\folder"
```

---

### ✔️ Compare directory with the last snapshot

Using the installed CLI:

```bash
fims compare --path "C:\path\to\folder"
```

Or with Python:

```bash
python src/fims/main.py compare --path "C:\path\to\folder"
```

---

### ✔️ List saved snapshots

CLI version:

```bash
fims list
```

Python version:

```bash
python src/fims/main.py list
```

---

## 📁 Project Structure

```
FIMS/
│
├── .github/
│   └── workflows/
│       └── python-ci.yml
│
├── src/
│   └── fims/
│       ├── hashing.py
│       ├── monitor.py
│       ├── storage.py
│       ├── main.py
│       └── __init__.py
│
├── tests/
│   └── test_hashing.py
│
├── snapshots/              # Auto-created after first snapshot
│
├── .gitignore
├── .flake8
├── requirements.txt
├── pyproject.toml
├── LICENSE
└── README.md

```

---

## 🧪 Testing

Run all tests:

```bash
pytest
```
Windows developers can use a custom temp directory:

```bash
python -m pytest -q --basetemp=.pytest_tmp
```
---

## 🔁 Continuous Integration (CI)

This project uses GitHub Actions for automated testing and style checks.
The workflow (.github/workflows/python-ci.yml) runs on every push or pull request and includes:

- Project installation
- Unit tests with pytest
- Linting with flake8
- Editable install with dev dependencies (.[dev])

You can view CI runs under the Actions tab on GitHub.

---

## 📜 License

Distributed under the **MIT License**.  
See the `LICENSE` file for more information.

---

## 👤 Author

**Oussema A.M**  
GitHub: [Am-Oussema](https://github.com/Am-Oussema)

---
