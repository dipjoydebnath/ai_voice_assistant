from voice import speak, listen
from brain import process_user_command

def run_assistant():
    # 1. AI Greets You Out Loud
    speak("Hello Deep! I am listening. Tell me what you would like to do.")
    
    # 2. AI Listens to Your Voice
    user_voice_input = listen()
    
    if user_voice_input:
        speak(f"Processing your command: {user_voice_input}")
        
        # 3. Brain Analyzes Command & Triggers WhatsApp if requested
        ai_response = process_user_command(user_voice_input)
        
        # 4. AI Speaks Result Back
        if ai_response:
            speak(ai_response)
    else:
        speak("I didn't hear any command. Please try running again.")

if __name__ == "__main__":
    run_assistant()