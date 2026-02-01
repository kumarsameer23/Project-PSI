🧠 AI-Powered Document & Multimedia Q&A Web Application

An intelligent full-stack system that allows users to upload PDFs, audio, and video files and interact with an AI chatbot to ask questions, generate summaries, and jump to relevant timestamps in multimedia content.

Built as part of an SDE-1 Programming Assignment to demonstrate real-world AI integration, backend engineering, frontend development, testing, and DevOps practices.

🎥 Demo Video

👉 Watch the full project walkthrough:
https://drive.google.com/file/d/1Kmk8Y0XPj1_At3i4kUgsmCo8iL8PPuPn/view?usp=sharing

The demo covers:

Running the app using Docker

Uploading video/audio/PDF files

AI-based question answering

Timestamp extraction and media playback

AI-generated summaries

Backend test coverage (99%)

GitHub Actions CI/CD pipeline

🚀 Key Features
📂 File Support

Upload PDF documents

Upload audio files

Upload video files

🤖 AI Capabilities

Contextual chatbot Q&A based on uploaded content

Semantic search using vector embeddings (FAISS)

Automatic transcription of audio/video using Whisper

AI-generated summaries

⏱ Smart Media Navigation

Extracts timestamps related to AI answers

One-click playback from relevant moment in audio/video

🔐 Authentication

Secure JWT-based login system

🧪 Quality & Reliability

99% backend test coverage

Unit tests for routes, services, and AI logic

🐳 DevOps & Deployment

Fully Dockerized backend and database

Multi-container setup using Docker Compose

CI/CD pipeline using GitHub Actions

🏗 Tech Stack
Backend

FastAPI – Web framework

MongoDB – Data storage

Whisper – Speech-to-text transcription

FAISS – Vector similarity search

JWT – Authentication

PyTest – Automated testing

Frontend

React.js – User interface

Axios – API communication

Infrastructure

Docker & Docker Compose – Containerization

GitHub Actions – CI/CD automation

🐳 Run the Project with Docker
1️⃣ Clone the Repository
git clone https://github.com/kumarsameer23/Project-PSI.git
cd Project-PSI

2️⃣ Start All Services
docker compose up --build

3️⃣ Access the App

Frontend:
👉 http://localhost:3000

Backend API Docs (Swagger):
👉 http://localhost:8000/docs

🧪 Run Backend Tests
cd backend
pytest --cov=app --cov-report=term


Test Coverage: 99%

🔄 CI/CD Pipeline

This project uses GitHub Actions to automatically:

Install dependencies

Run backend tests

Check test coverage

Every push to the repository triggers the CI workflow.

📁 Project Structure
backend/        → FastAPI app, AI services, tests
frontend/       → React user interface
docker-compose.yml

🎯 Learning Highlights

This project demonstrates:

Real-world integration of AI + backend systems

Handling multimedia processing pipelines

Implementing semantic search with embeddings

Writing high-coverage automated tests

Building a production-style Docker setup

Setting up CI/CD pipelines

👤 Author

Sameer Kumar
SDE-1 Assignment Submission
