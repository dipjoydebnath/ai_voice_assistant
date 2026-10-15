import json
from voice import speak, listen_smart, stop_speaking
from brain import process_user_command

# All phonetic variations for Nami
WAKE_WORDS = ["nami", "nani", "naomi", "now me", "mami", "hey", "hello", "enemy"]

# Action keywords that bypass wake-word checks
ACTION_KEYWORDS = ["message", "send", "whatsapp", "tell", "what", "who", "call", "can", "could", "please"]

#All Exit Keywords that Nami understands
EXIT_KEYWORDS = ["stop", "bye", "exit", "quit", "that's all", "never mind", "nothing"]

def get_contact_triggers():
    """Load contact names from contacts.json to use as automatic triggers."""
    try:
        with open("contacts.json", "r") as f:
            contacts = json.load(f)
            return [name.lower() for name in contacts.keys()]
    except Exception:
        return []

def is_wake_word_detected(phrase: str) -> bool:
    phrase_clean = phrase.lower().strip()
    
    # 1. Check if wake word is present
    for word in WAKE_WORDS:
        if word in phrase_clean:
            return True
            
    # 2. Check if action word is present (e.g. "send", "message")
    for action in ACTION_KEYWORDS:
        if action in phrase_clean:
            return True
            
    # 3. Check if any saved contact name is mentioned (e.g. "rajarshi")
    contacts = get_contact_triggers()
    for contact in contacts:
        if contact in phrase_clean:
            return True
            
    return False

def clean_wake_word(phrase: str) -> str:
    cleaned = phrase.lower()
    for word in WAKE_WORDS:
        cleaned = cleaned.replace(word, "").strip()
    return cleaned

def run_assistant():
    print("\n=== Nami AI Assistant Active ===")
    print("Speak naturally or call NAMI to trigger...\n")
    
    while True:
        heard_phrase = listen_smart(duration=4)
        
        if heard_phrase:
            if is_wake_word_detected(heard_phrase):
                print(f"-> TRIGGERED BY PHRASE: '{heard_phrase}'")
                stop_speaking()
                
                command = clean_wake_word(heard_phrase)
                
                # If only the wake word was spoken, prompt for command
                if not command or command in ACTION_KEYWORDS:
                    speak("Yes Master? I am listening.")
                    command = listen_smart(duration=5)
                
                # Conversation and Tool Loop
                while command:
                    print(f"\n👤 Master: '{command}'")
                    print("🧠 Nami Thinking...")
                    
                    ai_response = process_user_command(command)
                    
                    if ai_response:
                        speak(ai_response)
                    
                    print("\n🎤 Listening for follow-up...")
                    command = listen_smart(duration=5)
            else:
                print(f"[Debug] Heard phrase '{heard_phrase}', but no trigger keyword matched.")

if __name__ == "__main__":
    run_assistant()


