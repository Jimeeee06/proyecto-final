import speech_recognition as sr
import pyttsx3, pywhatkit

name = "juliana"
listener = sr.Recognizer()
engine = pyttsx3.init() #inicia pyttsx3
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id) #voz en español

def talk(texto):
    engine.say(texto)
    engine.runAndWait #habla y espera

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando")
            cont = listener.listen(source)
            g = listener.recognize_google(cont) #guarda lo escuchado
            g = g.lower()
            if name in g:
                g = g.replace(name, "")
    except:
        pass
    return g
def juliana():
    g = listen()
    if "reproduce" in g:
        cancion = g.replace("reproduce", "")
        t = "Reproduciendo " + cancion
        print(t)
        talk(t)
        pywhatkit.playonyt(cancion)

if __name__ == "__main__":
    juliana()