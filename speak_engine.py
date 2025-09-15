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