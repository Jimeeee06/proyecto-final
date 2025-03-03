import speech_recognition as sr
import subprocess as sp
import pyttsx3, pywhatkit, wikipedia, os

name = "juliana"
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
rate = engine.setProperty('rate', 200)
engine.setProperty("voices", voices[0].id)
engine.setProperty("volumen", 1)
wikipedia.set_lang("es")

def talk(texto):
    engine.say(texto)
    engine.runAndWait()

def listen():
    print("Escuchando . . .")
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            cont = listener.listen(source, timeout = 5)
            g = listener.recognize_google(cont, language="es-ES")
            g = g.lower()
            if name in g:
                g = g.replace(name, "")
            return g
    except Exception as e:
        print("No te escuché, ¿podrías repetirlo?")
        talk("No te escuché, ¿podrías repetirlo?")
        return "No te escuché, ¿podrías repetirlo?"

def reproduce(g):
    cancion = g.replace("reproduce", "")
    t = "Reproduciendo " + cancion
    print(t)
    talk(t)
    pywhatkit.playonyt(cancion)
    return False

def busqueda(g):
    busqueda = g.replace("qué es", "")
    info = wikipedia.summary(busqueda, 1)
    print("Según wikipedia: " + info)
    talk("Según wikipedia " + info)
    return False

def abrir(g):
    sites = {'google':'google.com', 'youtube':'youtube.com', 'whatsapp':'web.whatsapp.com',
             'sia':'sia.unal.edu.co', 'correo':'mail.google.com'}
    for sitio in sites:
        if sitio in g:
            sp.call(f'start opera.exe {sites[sitio]}', shell=True)
            a = f"Abriendo {sitio}"
            talk(a)
            print(a)
            return False
        else:
            m = "No se encontró el sitio. ¿Desea abrir una aplicación?"
            talk(m)
            print(m)
            respuesta = int(input("1. Sí  2. No\n"))
            talk("Presiona 1 para abrir una aplicación o 2 para no hacerlo.")
            if respuesta == 1:
                a = g.replace("abre", "")
                comando = f'start {a}.exe'
                sp.call(comando, shell=True)
                m = f"Abriendo {a}"
                talk(m)
                print(m)
                return False
            else:
                talk("No se abrirá ninguna aplicación.")
                return False
def cerrar(g):
    print("Adiós :)")
    talk("Adiós")
    return True

comandos = {"reproduce":reproduce, "qué es":busqueda, "abre":abrir, "vete":cerrar}


def juliana():
    talk("Hola, soy Juliana, ¿en qué puedo ayudarte?")
    while True:
        g = listen()
        cerrar = False
        for  key in comandos:
            if key in g:
                cerrar = comandos[key](g)
        if cerrar:
            break
    

if __name__ == "__main__":
    juliana()

"""Referencias: Daniiee - YouTube"""
