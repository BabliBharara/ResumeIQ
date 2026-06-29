from fastapi import FastAPI, Request ,UploadFile,File,Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.parser import extract_text
from fastapi.responses import PlainTextResponse
from app.ai import analyze_with_ai

# from fastapi.responses import Request
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"),name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    pdf_bytes = await resume.read()

    resume_text = extract_text(pdf_bytes)

    result = analyze_with_ai(
        resume_text,
        job_description
    )

    return {
        "result": result
    }