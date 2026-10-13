import os
from groq import Groq

# Put your actual Groq API key here inside the quotes
GROQ_API_KEY = "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"

# Initialize Groq client directly with key
client = Groq(api_key=GROQ_API_KEY)

try:
    # Get all models available for your API key
    models_list = client.models.list()
    print("Available Models on your Groq Key:")
    for model in models_list.data:
        print(f" - {model.id}")

    # Pick the first available text model automatically
    selected_model = models_list.data[0].id
    print(f"\nTesting with model: {selected_model}")

    response = client.chat.completions.create(
        model=selected_model,
        messages=[
            {"role": "user", "content": "Hello! Confirm that you are ready to be my AI assistant."}
        ]
    )

    print("\nAI Response:", response.choices[0].message.content)

except Exception as e:
    print("\nError:", e)