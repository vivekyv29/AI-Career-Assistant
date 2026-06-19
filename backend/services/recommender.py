import json
from services.chatbot_service import ask_ollama

def recommend_jobs(skills):

    prompt = f"""
Based on these resume skills:

{', '.join(skills)}

Recommend the 5 most suitable jobs.

Return ONLY valid JSON.

Example:

[
  {{
    "role": "Machine Learning Engineer",
    "match": 95
  }},
  {{
    "role": "Data Scientist",
    "match": 90
  }}
]
"""

    try:

        result = ask_ollama(prompt)

        start = result.find("[")
        end = result.rfind("]") + 1

        if start == -1 or end == 0:
            raise Exception("No JSON found")

        jobs = json.loads(result[start:end])

        return jobs

    except Exception as e:

        print("JOB RECOMMENDATION ERROR =", e)

        return [
            {
                "role": "Software Engineer",
                "match": 70
            }
        ]