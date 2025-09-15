import speech_recognition as sr
import pyttsx3

def speak(text):
    print(f"🟡 Responding: {text}")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🟢 Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"🗣️ You said: {command}")
            return command
        except:

            return None


#Updated

import pyttsx3
import sounddevice as sd
import queue
import vosk
import json

# ---------- Text to Speech ----------
def speak(text):
    print(f"🟡 Responding: {text}")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# ---------- Speech to Text (Offline with Vosk) ----------
q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

def listen():
    model = vosk.Model("model")  # folder where vosk model is stored
    samplerate = 16000  # required by vosk
    device = None  # use default microphone

    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device,
                           dtype='int16', channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        print("🟢 Listening (offline)... Speak now!")

        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")
                if text:
                    print(f"🗣️ You said: {text}")
                    return text.lower()
