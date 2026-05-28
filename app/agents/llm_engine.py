import openai
import json
from app.core.config import settings

def get_client():
    client = openai.OpenAI(
        api_key=settings.GEMINI_API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
    return client


async def ask_llm_json(prompt):
    client = get_client()
    
    response = client.chat.completions.create(
        model="gemini-3.5-flash",
        messages=[
            {   "role": "system",
                "content": "You are an SRE expert in logs investigation."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response.choices[0].message.content
    cleaned = content.replace("```json", "").strip("` ")
    
    return json.loads(cleaned)