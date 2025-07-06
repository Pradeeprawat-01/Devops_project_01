<h1 align="center">♾️ DevOps Project 1</h1>

<h1 align="center">🚀 Flask CI/CD Project with Jenkins, Docker & GitHub  </h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9-blue?logo=python" />
  <img src="https://img.shields.io/badge/Docker-Automation-2496ED?logo=docker" />
  <img src="https://img.shields.io/badge/Jenkins-CI/CD-FF6C37?logo=jenkins" />
  <img src="https://img.shields.io/badge/Flask-WebApp-black?logo=flask" />
</p>

---

## 📖 Overview

This project is a complete **CI/CD pipeline** using:

- 🌐 **Flask** (Python Web Framework)
- 🐳 **Docker** (Containerization)
- ⚙️ **Jenkins** (Build Automation)
- 💾 **GitHub** (Source Control)
- ✅ **Pytest** (Testing Framework)

It **automatically builds, tests, dockerizes**, and **deploys** your Flask app when new code is pushed to GitHub.

---

## 🛠️ Tech Stack

| Tool       | Purpose                         |
|------------|---------------------------------|
| **Flask**  | Backend framework               |
| **Docker** | Containerization                |
| **Jenkins**| CI/CD automation                |
| **GitHub** | Source code & webhook trigger   |
| **Pytest** | Testing and validation          |

---

## 📁 Project Structure

```bash
devops_projects/
├── app.py           🎯 Main Flask Application
├── test_app.py      ✅ Unit Tests with Pytest
├── messages.txt     📝 Stores Form Messages
├── Dockerfile       🐳 Docker Instructions
├── .gitignore       🚫 Ignore Cache, Logs
└── README.md        📘 Project Guide

🔄 CI/CD Pipeline Flow

A[GitHub Push] --> B[Jenkins Polls SCM]
B --> C[Clone Repo]
C --> D[Run Tests with Pytest]
D --> E[Docker Build Image]
E --> F[Push Image to DockerHub]
F --> G[Stop Old Container]
G --> H[Run New Container on :5000]

🔧 Jenkins Shell Commands
sudo docker build -t pradeep228/web:v${BUILD_NUMBER} .
sudo docker push pradeep228/web:v${BUILD_NUMBER}
sudo docker rm -f myflaskapp
sudo docker run -dit --name myflaskapp -p 5000:5000 pradeep228/web:v${BUILD_NUMBER}

✨ BUILD_NUMBER adds versioning
🚀 Automates testing, building & deployment
🔁 Removes old containers before launching new ones

🔁 SCM Polling Enabled
🕒 Jenkins checks GitHub for changes every minute
📦 New push triggers:
→ Clone → Test → Build → Push → Deploy
⚙️ No manual steps, just pure CI/CD automation!

✅ Final Output
🧪 Flask app gets tested via Pytest

🐳 Docker image is built & pushed to DockerHub

🚀 App deployed on port localhost:5000

🔄 Fully automated deployment from GitHub push

🔗 Repository
👉 GitHub Repository – DevOps Project

👨‍💻 Author
Pradeep Singh Rawat
DevOps • Python • Docker • CI/CD
💬 Open to collaborate & contribute


🙌 Let’s Connect
If you’re learning DevOps, I’d love to connect!
📬 DM me or raise an issue for help!

🔥 CI/CD is not just a skill — it's a superpower for modern developers
