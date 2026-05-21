Markdown
# SmartFlow-AI

Translate complex business descriptions into structured, automated workflows with clear sequential steps, actor badges, bottleneck detection, and AI optimization blueprints.

This repository contains both the FastAPI Python Backend and the Angular Standalone Frontend.

---

## 🏗️ System Architecture

The application implements a clean, decoupled client-server pattern:

* **Angular Client (Frontend):** Handles user input text, loading state spinners, and structural template rendering.
* **FastAPI Server (Backend):** Manages the incoming analysis requests and validates structured payload models.

---

## 📁 Repository Directory Structure

SmartFlow-AI/
├── smartflow-backend/         # Python FastAPI Application
│   ├── main.py                # Server routing and CORS policies
│   └── schemas.py             # Data validation models
└── smartflow-frontend/        # Angular Modern Client Application
├── src/
│   └── app/
│       ├── components/
│       │   └── dashboard/
│       │       ├── dashboard.ts     # Component logic & API call
│       │       ├── dashboard.html   # UI layout rendering template
│       │       └── dashboard.css    # Layout styling sheets
│       └── services/
│           └── workflow.service.ts  # HTTP client data handler
└── angular.json


---

## ⚡ Quick Start Setup

### 1. Backend Setup (FastAPI)
Navigate to the backend directory, configure a python sandbox environment, and spin up the server:

```bash
cd smartflow-backend

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install required dependencies
pip install fastapi uvicorn pydantic anthropic python-dotenv

# Boot the local backend server
python main.py
The backend server will run on http://127.0.0.1:8000

2. Frontend Setup (Angular)
In a secondary terminal window, set up and run your frontend application:

Bash
cd smartflow-frontend

# Install dependencies
npm install

# Launch the development compiler server
ng serve
Open your web browser and navigate directly to: http://localhost:4200

🎯 Features Demonstrated
Decoupled Architecture: Frontend and backend communicate cleanly over asynchronous local REST API requests.

Cross-Origin Configuration (CORS): Fully whitelisted connection to completely prevent local browser security blocks.

Modern Angular Core Templates: Utilizes standalone routing, FormsModule, and explicit *ngFor loop rendering optimizations.

Fail-Safe Processing Flow: Built-in validation structural fallbacks to guarantee robust presentation and visual tracking displays.
