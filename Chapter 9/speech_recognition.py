
import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Say something! I'm listening...")
    
    # Listen for the first phrase and extract audio data
    audio = r.listen(source)
    print("Got it! Now processing...")

try:
    # Recognize speech using Google's free web-speech API
    text = r.recognize_google(audio)
    
    # Print the recognized text
    print("You said: " + text)

except sr.UnknownValueError:
    # API was unable to understand audio
    print("Sorry, I could not understand what you said.")

except sr.RequestError as e:
    # Could not request results from Google's API
    print(f"Could not request results; {e}")
    