# 🎙️ Project Nami - AI Voice Assistant & Telegram Auto-Responder

Welcome to **Project Nami**! This project is a smart, hybrid assistant system designed to make daily tasks and message handling completely automated using Artificial Intelligence.

---

## ❓ Why Is This Project Created? (Main Purpose)

In our daily digital life, we often get overwhelmed by managing multiple tasks on our computer while simultaneously keeping up with personal messages on messaging platforms like Telegram.

**The Main Purpose:**
* To build a hands-free personal desktop assistant that listens to your voice commands and helps you perform tasks instantly.
* To create an intelligent, background auto-responder for Telegram that automatically answers incoming private messages when you are busy or away.
* To combine both voice-based control and text messaging automation into one single, powerful project.

---

## 💡 How To Use This Project?

Since this project has two main features, you can run them either together or separately depending on what you need.

### 1. Daily Usage Steps:
1. **To use the Voice Assistant:**
   * Open your terminal and run `python main.py`.
   * Speak into your microphone (e.g., ask questions, request information, or trigger automated commands).
   * Nami will process your voice and reply back in spoken audio!

2. **To use Telegram Auto-Responder:**
   * Open a second terminal and run `python telegram_auto_reply.py`.
   * Whenever someone sends you a personal message on Telegram, Nami will automatically generate a helpful reply and send it on your behalf in real-time.

---

## ⚙️ How Is This Working? (Under the Hood)

Here is a simple step-by-step breakdown of how the magic happens:

1. **Voice Input to Text:** When you speak, `SpeechRecognition` captures your sound through the microphone and converts it into readable text.
2. **AI Brain Processing:** The converted text is sent to the **Groq AI Engine** (`brain.py`), which acts as Nami's intelligence. It processes your input in milliseconds and generates a smart response.
3. **Text to Speech Output:** `pyttsx3` takes the generated text response and speaks it out loud through your speakers.
4. **Telegram Messaging:** Simultaneously, `Pyrogram`/`Telethon` connects to your Telegram account using API sessions (`.session` files) and listens for new incoming messages, feeding them to the AI engine for instant replies.

---

## 🛠️ What Things & Information Were Used To Build This?

Here are all the key components, libraries, and tools used in making Project Nami:

### 1. Programming Language:
* **Python 3.x** - The primary language powering all logic and scripts.

### 2. Core Libraries & AI Tools:
* **Groq API (`groq`)**: Lightning-fast LLM API used for text generation and reasoning.
* **Speech Recognition (`SpeechRecognition`)**: Converts spoken human audio into string format.
* **Text-to-Speech Engine (`pyttsx3`)**: Converts AI text output into offline voice audio.
* **Telegram Client (`Pyrogram` / `Telethon`)**: Handles Telegram connectivity and automated message listeners.
* **Automation Helper (`PyWhatKit`)**: Used for desktop shortcuts, web searches, and messaging integrations.
* **Environment Security (`python-dotenv`)**: Safely stores sensitive passwords and API keys offline.

### 3. File Structure:
* `main.py` - Core Voice Assistant entry point.
* `telegram_auto_reply.py` - Telegram auto-reply listener engine.
* `brain.py` - Connects with Groq API to process prompts.
* `voice.py` - Audio input/output helper functions.
* `contacts.json` - Local dictionary for saved phone numbers and contact names.
* `.gitignore` - Protects sensitive `.env` and `.session` files from leaking on GitHub.

---

## 🚀 Can I Integrate or Change Anything in the Future?

**YES, ABSOLUTELY!** 🎉

This project is built with a modular structure, meaning you can easily extend, modify, or add new features in the future. Here are a few examples of what you can add next:

* **WhatsApp Integration:** Add automated replies or voice messaging support for WhatsApp.
* **Smart Home Control:** Connect IoT APIs to control lights, fans, or home devices via voice.
* **Custom GUI Dashboard:** Create a visual interface (using PyQt, Tkinter, or Streamlit) instead of running terminal commands.
* **More AI Models:** Swap out Groq or add multi-modal models (image analysis, PDF reader integration).
* **Calendar & Reminders:** Sync local voice commands with Google Calendar or Todoist APIs.

---

## 🔐 Security Notice

This repository is **completely secure**. All sensitive credentials like API Keys (`GROQ_API_KEY`) and Telegram User Sessions (`*.session`) are strictly hidden using `.env` and `.gitignore`. No private keys or personal details are exposed in the code.
