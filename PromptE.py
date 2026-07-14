from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

prompt = "Explain DSA in simple words."

temperatures = [0.0, 0.3, 0.7, 1.0]

for temp in temperatures:
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=temp,
        max_tokens=300
    )

    print(f"\nTemperature: {temp}")
    print(response.choices[0].message.content)