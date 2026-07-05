# ResumeIQ Lite – AI Resume Skill Gap Analyzer

ResumeIQ Lite is an AI-powered resume analysis web application that helps users identify skill gaps in their resumes based on their target job role. The application extracts text from an uploaded PDF resume, analyzes the content using AI, and provides structured feedback to help users improve their resume and job readiness.

## Features

* Upload and analyze resumes in PDF format
* Extract resume text automatically
* AI-powered resume analysis
* Identify existing technical and professional skills
* Detect missing skills based on the target job role
* Generate personalized improvement suggestions
* Simple and responsive user interface
* Fast API-based communication between frontend and backend

## Tech Stack

**Frontend**

* HTML
* CSS
* JavaScript

**Backend**

* Python
* FastAPI
* Uvicorn

**Resume Processing**

* PyMuPDF (fitz)

**AI Integration**

* Generative AI API for resume analysis and skill-gap identification

## Project Structure

```text
ResumeIQ-Lite/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── backend/
│   ├── main.py
│   ├── parser.py
│   ├── ai.py
│   └── prompts.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## How It Works

1. The user uploads a resume in PDF format.
2. The frontend sends the resume file and target job role to the backend API.
3. The backend reads the uploaded PDF file as bytes.
4. PyMuPDF extracts text from the resume.
5. The extracted resume text and target role are sent to the AI analysis module.
6. The AI analyzes the candidate's skills and identifies missing skills.
7. The backend returns structured analysis results.
8. The frontend displays the results to the user.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd ResumeIQ-Lite
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the API Key

Create a `.env` file in the backend directory and add your AI API key:

```text
API_KEY=your_api_key_here
```

Do not upload the `.env` file or expose your API key publicly.

### 6. Run the Backend Server

```bash
uvicorn main:app --reload
```

The backend server will start locally.

### 7. Run the Frontend

Open `index.html` using a local development server such as Live Server.

## API Workflow

```text
User Uploads Resume
        ↓
Frontend JavaScript
        ↓
FastAPI Endpoint
        ↓
PDF Text Extraction
        ↓
AI Resume Analysis
        ↓
Structured Response
        ↓
Results Displayed to User
```

## Learning Outcomes

This project demonstrates practical knowledge of:

* Building REST APIs using FastAPI
* Handling file uploads in Python
* Processing PDF documents
* Connecting frontend and backend applications
* Working with asynchronous API routes
* Integrating generative AI APIs
* Prompt engineering for structured AI responses
* Error handling and API response management

## Future Improvements

* User authentication and profile management
* Resume analysis history
* Database integration
* ATS compatibility score
* Job description and resume comparison
* Resume improvement recommendations
* Cloud deployment
* Exportable analysis reports

## Disclaimer

ResumeIQ Lite provides AI-generated suggestions for educational and career-support purposes. The analysis should be treated as guidance and does not guarantee employment or selection in any recruitment process.

## Author

Developed as a full-stack AI-based project demonstrating resume processing, REST API development, frontend-backend integration, and generative AI integration.
