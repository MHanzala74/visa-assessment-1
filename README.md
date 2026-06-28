# Visa Assessment Backend

A modular RESTful backend for an AI-powered visa assessment system built with FastAPI and LangChain.

## Tech Stack

- **Framework:** FastAPI
- **AI / LLM:** LangChain, LangChain-OpenAI
- **Database:** Supabase (PostgreSQL via psycopg2)
- **Authentication:** JWT, bcrypt, python-jose
- **PDF Processing:** pypdf
- **Data Validation:** Pydantic
- **Server:** Uvicorn

## Project Structure

```
visa-assessment-1/
├── core/           # App configuration and dependencies
├── database/       # Database connection and queries
├── routes/         # API route handlers
│   ├── auth_routes.py
│   ├── visa_routes.py
│   ├── profile_routes.py
│   ├── graph_routes.py
│   └── cv_routes.py
├── schemas/        # Pydantic request/response models
├── services/       # Business logic layer
├── main.py         # App entry point
└── requirements.txt
```

## Features

- JWT-based authentication (register, login)
- Visa eligibility assessment via LLM pipeline
- CV/PDF parsing and processing
- User profile management
- Graph generation for assessment results

## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload
```

## API Health Check

```
GET /health
```

Returns `{ "message": "Visa assessment backend running" }`
