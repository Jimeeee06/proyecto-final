import speech_recognition as sr
import subprocess as sp
import pyttsx3, pywhatkit, wikipedia, os

name = "juliana"
listener = sr.Recognizer()
engine = pyttsx3.init() #inicia pyttsx3
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id) #voz en español
engine.setProperty("volumen", 1) #volumen
wikipedia.set_lang("es") #idioma de wikipedia

sites = {'google':'google.com', 'youtube':'youtube.com', 'whatsapp':'web.whatsapp.com', 'sia':'sia.unal.edu.co', 'correo':'mail.google.com'} #estos son los sitios que puede abrir juliana


def talk(texto):
    engine.say(texto)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando . . .")
            listener.adjust_for_ambient_noise(source)
            cont = listener.listen(source)
            g = listener.recognize_google(cont, language="es-ES")
            g = g.lower()
            if name in g:
                g = g.replace(name, "")
            return g
    except Exception as e:
        return "No puedo escucharte"

def juliana():
    while True:
        g = listen()  # Actualizamos la variable g en cada iteración
        if "reproduce" in g:
            cancion = g.replace("reproduce", "")
            t = "Reproduciendo " + cancion
            print(t)
            talk(t)
            pywhatkit.playonyt(cancion)
        elif "qué es" in g:
            busqueda = g.replace("qué es", "")
            info = wikipedia.summary(busqueda, 1)
            print("Según wikipedia: " + info)
            talk("Según wikipedia " + info)
        elif "abre" in g:
            for sitio in sites:
                if sitio in g:
                    sp.call(f'start opera.exe {sites[sitio]}', shell=True)
                    a = f"Abriendo {sitio}"
                    talk(a)
                    print(a)
        elif "vete" in g:
            talk("Adiós")
            print("Adiós :)")
            break
    

if __name__ == "__main__":
    juliana()
