import pyttsx3 as ps
import speech_recognition as sr
import webbrowser as wb
import wikipedia as wp
import pytube as yt

engine = ps.init()
engine.setProperty("volume", 100)
engine.setProperty("rate", 120)

recogniser = sr.Recognizer()

def audio_input():
    with sr.Microphone() as source:
        print("Listening for wakeup word...")
        audio = recogniser.listen(source)
    try:
        text = recogniser.recognize_google(audio)
    except:
        text = ""
    return text

def speak(text):
    engine.say(text)
    engine.runAndWait()

def interogation_check(s):
    for i in s.split(" "):
        if i in ["what", "when", "how", "why", "where", "which", "about", "explain", "explanation", "who"]:
            return True
    return False

def search_browser(txt):
    query = ""
    split = " "
    if "about" in txt.split(" "):
        split = 'about'
    elif "explain" in txt.split(" "):
        split = 'explain'
    elif "on" in txt.split(" "):
        split = "on"
    for i in txt.split(split)[-1].split(" "):
        query += i + "+"
    wb.open("www.google.com/search?q=" + query)

def run():
    while True:
        wakeup = audio_input().lower()
        if "assistant" in wakeup:
            speak("Ask me")
            audio = audio_input().lower()
            if "play" in audio:
                song = audio.split("play")[-1]
                speak("Playing " + song)
                ready_query = ""
                for i in song.split(" "):
                    ready_query += i + "+"
                search_song = yt.Search(song)
                yt_id = "www.youtube.com/watch?v=" + str(search_song.results[0]).split("=")[-1][:-1]
                wb.open(yt_id)
            elif "open" in audio:
                if "youtube" in audio:
                    speak("Opening YouTube")
                    wb.open("www.youtube.com")
                if "google" in audio:
                    speak("Opening Google")
                    wb.open("www.google.com")
            elif interogation_check(audio):
                speak("Okay!")
                try:
                    data = wp.summary(audio, 5)
                    print(data)
                    speak("According to Wikipedia " + data)
                except:
                    speak("Opening in web browser")
                    search_browser(audio)
            elif 'exit' in audio or "quit" in audio:
                print("OK! Good bye!")
                speak("OK! Good bye.")
                exit()

if __name__ == '__main__':
    run()
