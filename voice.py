import sounddevice as sd
import scipy.io.wavfile as wav
import speech_recognition as sr
import edge_tts
import asyncio
import os

# 1. THE MOUTH (Text-to-Speech)
async def speak_text_async(text: str):
    voice = "en-US-AriaNeural"
    output_file = "response.mp3"
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)
    os.system(f"start {output_file}")

def speak(text: str):
    print(f"AI Speaking: \"{text}\"")
    asyncio.run(speak_text_async(text))

# 2. THE EAR (Microphone Recording)
def listen():
    sample_rate = 44100
    duration = 5  # Listens for 5 seconds
    filename = "temp_input.wav"
    
    print("\n🎤 Listening... Speak now!")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()
    print("Processing speech...")
    
    wav.write(filename, sample_rate, recording)
    
    recognizer = sr.Recognizer()
    user_text = None
    
    # Process file and close handle before cleanup
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
        try:
            user_text = recognizer.recognize_google(audio)
            print(f"You said: \"{user_text}\"")
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
        except sr.RequestError:
            print("Speech recognition service is unreachable.")
            
    # Safely delete temporary file after closing handle
    if os.path.exists(filename):
        try:
            os.remove(filename)
        except PermissionError:
            pass
            
    return user_text

if __name__ == "__main__":
    speak("Hello Deep! What message would you like to send?")
    spoken_command = listen()
    if spoken_command:
        speak(f"I heard you say: {spoken_command}")