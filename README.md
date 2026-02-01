AI-Powered Document & Multimedia Q&A Web App
🔍 Overview

This is a full-stack AI application that allows users to upload PDFs, audio, and video files, then interact with an AI chatbot to ask questions, get summaries, and jump to relevant timestamps in media.

Built as part of an SDE-1 Programming Assignment.

🚀 Features

📄 Upload PDF documents

🎵 Upload audio files

🎥 Upload video files

🤖 AI chatbot answers questions from uploaded content

📝 AI-generated summaries

⏱ Timestamp extraction for media

▶ Play media from relevant timestamp

🔐 JWT Authentication

🧠 Semantic search using FAISS vector database

🏗 Tech Stack

Backend

FastAPI

MongoDB

FAISS (Vector Search)

Whisper (Speech-to-Text)

JWT Authentication

PyTest (99% test coverage)

Frontend

React.js

Axios API integration

Infrastructure

Docker & Docker Compose

GitHub Actions CI/CD

🐳 Run with Docker
docker compose up --build


Frontend → http://localhost:3000

Backend API Docs → http://localhost:8000/docs

🧪 Run Tests
cd backend
pytest --cov=app --cov-report=term


Coverage: 99%

🔄 CI/CD

GitHub Actions automatically runs backend tests on every push.
