import sounddevice as sd
import soundfile as sf
import numpy as np
import speech_recognition as sr
import edge_tts
import asyncio
import os

# 1. THE MOUTH (TTS Output via sounddevice)
async def speak_text_async(text: str):
    voice = "en-US-AriaNeural"
    output_file = "response.wav"
    
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)
    
    if os.path.exists(output_file):
        data, samplerate = sf.read(output_file)
        sd.play(data, samplerate)
        sd.wait()
        
        try:
            os.remove(output_file)
        except PermissionError:
            pass

def stop_speaking():
    sd.stop()

def speak(text: str):
    print(f"\n🤖 NAMI Speaking: \"{text}\"")
    stop_speaking()
    asyncio.run(speak_text_async(text))

# 2. THE EAR (Microphone recording using sounddevice instead of PyAudio)
def listen_smart(duration=4, sample_rate=44100):
    """Records mic audio using sounddevice and passes it to SpeechRecognition."""
    print("\n🎤 Listening... Speak now!")
    
    # Record audio directly into memory using sounddevice
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()
    print("Processing speech...")
    
    # Save audio temporarily
    temp_filename = "temp_voice.wav"
    sf.write(temp_filename, recording, sample_rate)
    
    recognizer = sr.Recognizer()
    user_text = ""
    
    if os.path.exists(temp_filename):
        with sr.AudioFile(temp_filename) as source:
            audio = recognizer.record(source)
            try:
                user_text = recognizer.recognize_google(audio).lower()
                print(f"👤 Heard: \"{user_text}\"")
            except (sr.UnknownValueError, sr.RequestError):
                pass
        
        try:
            os.remove(temp_filename)
        except PermissionError:
            pass
            
    return user_text

if __name__ == "__main__":
    speak("Voice engine ready.")