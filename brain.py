import os
import json
from groq import Groq
from send_whatsapp import send_whatsapp_message

# Ensure your Groq API key is set
os.environ["GROQ_API_KEY"] = "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"  # Replace with your actual Groq key

client = Groq()

# 1. Define the tool/function structure for Groq LLM
tools = [
    {
        "type": "function",
        "function": {
            "name": "send_whatsapp_message",
            "description": "Sends a WhatsApp message to a specific contact saved in the contacts dictionary.",
            "parameters": {
                "type": "object",
                "properties": {
                    "contact_name": {
                        "type": "string",
                        "description": "The name of the contact (e.g., Rahul, Mom, Rohit)."
                    },
                    "message_text": {
                        "type": "string",
                        "description": "The exact text message content to send."
                    }
                },
                "required": ["contact_name", "message_text"]
            }
        }
    }
]

def process_user_command(user_prompt: str):
    """Passes user command to Groq LLM and executes tools if requested."""
    print(f"\nUser Command: '{user_prompt}'")
    
    # Send user prompt to Groq model with tool definitions
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",  # Using the model verified on your key
        messages=[{"role": "user", "content": user_prompt}],
        tools=tools,
        tool_choice="auto"
    )

    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    # Check if LLM decided to invoke a tool
    if tool_calls:
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)

            if function_name == "send_whatsapp_message":
                print(f"-> Brain decided to call tool: {function_name}")
                print(f"   Extracted Arguments: {function_args}")
                
                # Execute the actual Python function from send_whatsapp.py
                result = send_whatsapp_message(
                    contact_name=function_args.get("contact_name"),
                    message_text=function_args.get("message_text")
                )
                return result
    else:
        # If it's just regular conversation (e.g., "How are you?")
        return response_message.content

if __name__ == "__main__":
    # Test 1: Casual question (No tool call needed)
    reply1 = process_user_command("Who are you?")
    print("AI Answer:", reply1)

    # Test 2: WhatsApp Command (Triggers function calling automatically!)
    reply2 = process_user_command("Send a message to Rajarshi saying Today I am coming to meet you")
    print("AI Answer:", reply2)