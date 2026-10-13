import json
import pywhatkit

def load_contacts():
    """Reads saved phone numbers from contacts.json"""
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: contacts.json file not found.")
        return {}

def send_whatsapp_message(contact_name: str, message_text: str):
    """Looks up a contact and sends a WhatsApp message instantly"""
    contacts = load_contacts()
    clean_name = contact_name.lower().strip()
    
    if clean_name in contacts:
        phone_number = contacts[clean_name]
        print(f"Found contact: '{contact_name}' -> {phone_number}")
        print(f"Sending message: \"{message_text}\"...")
        
        # Opens WhatsApp Web and sends the message
        # wait_time=15 gives WhatsApp Web time to load in browser
        pywhatkit.sendwhatmsg_instantly(phone_number, message_text, wait_time=15, tab_close=True)
        print("Message sent successfully!")
        return f"Successfully sent message to {contact_name}"
    else:
        error_msg = f"Contact '{contact_name}' not found in contacts.json"
        print(error_msg)
        return error_msg

if __name__ == "__main__":
    # Test sending a message (Make sure to put a valid number in contacts.json first!)
    send_whatsapp_message("rajarshi", "Today I am coming to meet you")