# CodeSage 🤖💻
> Autonomous pull request auditor, concurrency bug detector, and AST refactoring agent.

## 🚀 Overview
CodeSage integrates directly into GitHub & GitLab CI/CD pipelines. It computes semantic syntax trees using Tree-sitter, detects memory leaks, race conditions, and SQL injection flaws, and uses DeepSeek-Coder-V2 to synthesize verified patches tested in isolated Docker containers.

## 🛠️ Tech Stack
- **Engine**: Python 3.11+, DeepSeek-Coder-V2, Tree-sitter AST
- **API & Webhook Gateway**: FastAPI, GitHub Apps API, PostgreSQL
- **Sandbox Execution**: Docker SDK for ephemeral test validation

## ⚡ Quick Start (Arch Linux)
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --port 8000 --reload
```
