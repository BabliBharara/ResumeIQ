import os
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI


client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

def analyze_with_ai(resume_text, job_description):

    prompt = f"""
You are an ATS Resume Analyzer.

Resume:
{resume_text}

Job Description:
{job_description}

Return only:

ATS Score: __/100

Matched Skills:
- ...

Missing Skills:
- ...

Suggestions:
- ...
"""

    response = client.chat.completions.create(
        model="google/gemma-4-31b-it:free",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content