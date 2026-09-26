
# AI Resume Evaluator

An AI-powered resume evaluation system that compares a candidate's resume with a job description using Gemini AI.

## Features

- Resume and job description comparison
- Resume matching score from 0 to 100
- Identification of candidate strengths
- Missing skills detection
- Concise evaluation summary
- Structured JSON output
- Prompt engineering for accurate evaluation
- Error handling and input validation

## Technologies Used

- Python
- Google Gemini API
- JSON
- Prompt Engineering

## Project Structure

```text
AI-AI-Engineering-Task/
├── main.py
└── README.md
```

## How It Works

1. Accepts resume text and job description.
2. Sends the input to Gemini AI.
3. Evaluates the candidate's skills and qualifications.
4. Generates a matching score.
5. Returns strengths, missing skills, and a summary in JSON format.

## Output Format

```json
{
  "match_score": 85,
  "top_strengths": ["Python", "Problem Solving"],
  "missing_skills": ["SQL"],
  "summary": "The candidate has relevant technical skills."
}
```

## Adversarial Testing

The system is designed to handle:

- Empty resume input
- Missing job description
- Irrelevant resume content
- Prompt injection attempts
- Invalid AI responses
- Missing or incorrect JSON fields

## Security

- Resume and job description are treated as untrusted input.
- API keys should never be committed to GitHub.
- AI output should be validated before use.

## Future Improvements

- PDF resume upload
- Resume parsing
- Improved scoring accuracy
- Web-based user interface

## Author

Deepak
