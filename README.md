# FIMS – File Integrity Monitoring System
![Status](https://img.shields.io/badge/status-active-brightgreen)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-yellow)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey)
![Type](https://img.shields.io/badge/type-CLI_tool-purple)


FIMS is a lightweight and efficient tool for detecting changes in files or folders  
by using **SHA-256 hashing** and comparing snapshots over time.

It is designed for developers, students, and cybersecurity beginners who want a
simple and reliable way to monitor file integrity on their system.

---

## 📌 Features

- 🧩 Create snapshots of any directory  
- 🔍 Compare a directory with its previous snapshot  
- 🚨 Detect **added**, **removed**, and **modified** files  
- 🗂 All snapshots stored locally in a JSON format  
- 🖥️ Can be used from CLI using `fims` or with Python (`python main.py`)
- ⚡ Fast and minimal — no database or heavy dependencies  

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
│   README.md
│   pyproject.toml
│   requirements.txt
│   .gitignore
│   LICENSE
│
├── src/
│   └── fims/
│       ├── hashing.py
│       ├── monitor.py
│       ├── storage.py
│       ├── main.py
│       └── __init__.py
│
└── tests/
    └── test_hashing.py
```

---

## 🧪 Testing

To run unit tests:

```bash
pytest
```

---

## 📄 License

Distributed under the **MIT License**.  
See the `LICENSE` file for more information.

---

## 👤 Author

**Oussema A.M**  
GitHub: [Am-Oussema](https://github.com/Am-Oussema)

---
