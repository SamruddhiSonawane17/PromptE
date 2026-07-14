from openai import OpenAI

client = OpenAI(
    api_key="api_key",
    base_url="https://openrouter.ai/api/v1",
)

prompt = "Explain DSA in simple words."

temperatures = [0.0, 0.3, 0.7, 1.0]

for temp in temperatures:
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=temp,0
        max_tokens=300,   # Increased from 150
    )

    print("=" * 60)
    print(f"Temperature: {temp}")
    print("=" * 60)

    if response.choices and response.choices[0].message.content:
        print(response.choices[0].message.content)
    else:
        print("No response received.")