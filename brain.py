import json
import os
from dotenv import load_dotenv
from groq import Groq
from send_whatsapp import send_whatsapp_message

load_dotenv()
client = Groq()

# Define the system personality and instructions
SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "You are Nami, a highly intelligent and friendly AI voice assistant. "
        "Always address the user as 'Master'. Keep your responses warm, concise, "
        "and conversational (1-3 sentences), as your replies will be spoken out loud."
    )
}

# Conversation history buffer to maintain context
conversation_history = [SYSTEM_PROMPT]

# Define tool functions for Groq Function Calling
tools = [
    {
        "type": "function",
        "function": {
            "name": "send_whatsapp_message",
            "description": "Sends a WhatsApp message to a contact saved in contacts.json.",
            "parameters": {
                "type": "object",
                "properties": {
                    "contact_name": {"type": "string", "description": "The name of the contact"},
                    "message_text": {"type": "string", "description": "The text message content"}
                },
                "required": ["contact_name", "message_text"]
            }
        }
    }
]

def process_user_command(user_text: str) -> str:
    global conversation_history
    
    # 1. Append user's input to conversation history
    conversation_history.append({"role": "user", "content": user_text})
    
    # Keep history focused (keep system prompt + last 10 messages)
    if len(conversation_history) > 11:
        conversation_history = [SYSTEM_PROMPT] + conversation_history[-10:]

    try:
        # 2. Call Groq LLM with full conversation context
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=conversation_history,
            tools=tools,
            tool_choice="auto"
        )

        response_message = response.choices[0].message

        # 3. Handle Tool Calls (WhatsApp Automation)
        if response_message.tool_calls:
            for tool_call in response_message.tool_calls:
                func_name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)

                if func_name == "send_whatsapp_message":
                    result = send_whatsapp_message(
                        contact_name=args.get("contact_name"),
                        message_text=args.get("message_text")
                    )
                    
                    # Add execution result back to history
                    conversation_history.append(response_message)
                    conversation_history.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result
                    })
                    
                    # Final response after tool execution
                    second_response = client.chat.completions.create(
                        model="openai/gpt-oss-120b",
                        messages=conversation_history
                    )
                    final_text = second_response.choices[0].message.content
                    conversation_history.append({"role": "assistant", "content": final_text})
                    return final_text
        
        # 4. Standard conversational reply
        reply_text = response_message.content
        conversation_history.append({"role": "assistant", "content": reply_text})
        return reply_text

    except Exception as e:
        print(f"Error in Brain module: {e}")
        return "I encountered an error processing that command."