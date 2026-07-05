# ResumeIQ Lite – AI Resume Skill Gap Analyzer

ResumeIQ Lite is an AI-powered web application that analyzes a user's resume and identifies skill gaps based on their target job role.

The application accepts a resume in PDF format, extracts its text, and uses AI to analyze the candidate's existing skills, identify missing skills, and provide improvement suggestions.

This project demonstrates backend API development, PDF processing, AI API integration, prompt engineering, and frontend-backend communication.

---

## Features

- Upload resumes in PDF format
- Extract text automatically from uploaded resumes
- Analyze resume content using AI
- Identify skills already present in the resume
- Detect missing skills for a target job role
- Generate personalized improvement suggestions
- Display structured analysis results
- Simple and user-friendly web interface
- Backend API built using FastAPI

---

## Tech Stack

### Backend

- Python
- FastAPI
- Uvicorn

### Frontend

- HTML
- CSS
- JavaScript

### Resume Processing

- PyMuPDF (`fitz`)

### AI Integration

- Generative AI API
- Prompt engineering for structured resume analysis

---

## Project Structure

```text
ResumeIQ/
│
├── app/
│   └── Application logic and backend modules
│
├── static/
│   └── CSS and JavaScript files
│
├── templates/
│   └── HTML templates
│
├── main.py
├── .gitignore
└── README.md
```

---

## How It Works

The application follows this workflow:

```text
User Uploads Resume
        ↓
Frontend Sends Resume to Backend
        ↓
FastAPI Receives the PDF File
        ↓
PDF File is Read as Bytes
        ↓
Text is Extracted from the Resume
        ↓
Extracted Text is Sent for AI Analysis
        ↓
AI Identifies Skills and Skill Gaps
        ↓
Backend Returns Structured Results
        ↓
Results are Displayed to the User
```

### Step-by-Step Process

1. The user uploads a resume in PDF format.

2. The frontend sends the resume file and required input to the FastAPI backend.

3. The backend reads the uploaded PDF as bytes.

4. The resume parser extracts text from the PDF using PyMuPDF.

5. The extracted resume text is passed to the AI analysis module.

6. A structured prompt instructs the AI to analyze the resume and identify relevant skills and missing areas.

7. The AI response is processed by the backend.

8. The final analysis is returned to the frontend and displayed to the user.

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

Move into the project directory:

```bash
cd ResumeIQ
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

---

### 3. Activate the Virtual Environment

#### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

---

### 4. Install Required Dependencies

Install the dependencies required by the project.

Example:

```bash
pip install fastapi uvicorn pymupdf python-multipart python-dotenv
```

Also install the SDK required by the AI API used in the project.

---

### 5. Configure the API Key

Create a `.env` file in the appropriate project directory and add your API key.

Example:

```env
API_KEY=your_api_key_here
```

The environment variable name should match the variable used in the project code.

> Important: Never upload your `.env` file or API key to GitHub.

Make sure `.env` is included in `.gitignore`.

---

### 6. Run the Application

From the project root directory, run:

```bash
uvicorn main:app --reload
```

After the server starts, open the local address shown in the terminal.

The application will usually be available at:

```text
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates interactive API documentation.

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

This interface allows you to view and test the available API endpoints.

---

## Core Concepts Used

### File Upload Handling

The backend receives the uploaded PDF file through a FastAPI endpoint and reads its contents as bytes.

### PDF Text Extraction

The PDF bytes are processed using PyMuPDF to extract readable text from the resume.

### AI-Based Analysis

The extracted resume text is passed to an AI model along with structured instructions. The model analyzes the resume and generates skill-gap insights.

### Prompt Engineering

Structured prompts are used to guide the AI model and improve the consistency and usefulness of the generated analysis.

### Frontend-Backend Communication

JavaScript sends user input and resume data to the FastAPI backend. The backend processes the request and returns the analysis results.

---

## Learning Outcomes

Through this project, I gained practical experience with:

- Building REST APIs using FastAPI
- Handling file uploads in Python
- Working with asynchronous API routes
- Extracting text from PDF documents
- Integrating generative AI APIs
- Writing structured prompts for AI models
- Processing AI-generated responses
- Connecting a JavaScript frontend with a Python backend
- Organizing a full-stack Python project
- Managing environment variables and API keys
- Implementing basic error handling

---

## Future Improvements

The project can be extended with:

- ATS resume scoring
- Job description and resume comparison
- User authentication
- Resume analysis history
- Database integration
- Multiple resume format support
- Resume improvement recommendations
- Role-specific learning roadmaps
- Downloadable analysis reports
- Cloud deployment

---

## Disclaimer

ResumeIQ Lite provides AI-generated resume analysis and skill recommendations for educational and career-support purposes.

The generated analysis should be treated as guidance and does not guarantee employment, interview selection, or recruitment outcomes.

---

## Author

Developed as a full-stack AI-based project to demonstrate practical skills in:

- Python backend development
- FastAPI
- REST API development
- PDF processing
- AI API integration
- Prompt engineering
- Frontend-backend integration
