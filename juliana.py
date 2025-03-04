import pyttsx3, speech_recognition, pywhatkit, wikipedia
import subprocess as sp
import datetime as dt

name = "juliana"
listener = speech_recognition.Recognizer()
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
        with speech_recognition.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            cont = listener.listen(source, timeout = 10)
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
    m = "No se encontró el sitio. ¿Desea abrir una aplicación?"
    talk(m)
    print(m)
    respuesta = int(input("1. Sí  2. No\n"))
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

def hora(g):
    h = dt.datetime.now().strftime("%I")
    m = dt.datetime.now().strftime("%M")
    s = dt.datetime.now().strftime("%S")
    p = dt.datetime.now().strftime("%p")
    print(f"Son las {h}: {m}: {s} {p}")
    talk(f"Son las {h} y {m}, con {s} segundos {p}")
    return False

def día(g):
    now = ahora = dt.datetime.now()
    semana = {"Monday":"Lunes", "Tuesday":"Martes", "Wednesday":"Miércoles", "Thursday":"Jueves",
            "Friday":"Viernes", "Saturday":"Sábado", "Sunday":"Domingo"}
    meses = {1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio",
             7: "julio", 8: "agosto", 9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"}
    for dia in semana:
        if dia in semana:
            dia = semana[dia]
    for mes in meses:
        if mes in meses:
            mes = meses[now.month]
    print(f"Hoy es {dia}, {now.day} de {mes} de {now.year}")
    talk(f"Hoy es {dia}, {now.day} de {mes} de {now.year}")
    return False

def temporizador(g):
    tiempo_str = g.replace("temporizador de", "").strip()
    try:
        if "minutos" in tiempo_str:
            minutos = int(tiempo_str.replace("minutos", "").strip())
            seg = min * 60
            m = f"Temporizador de {minutos} minutos iniciado"
        elif "segundos" in tiempo_str:
            seg = int(tiempo_str.replace("segundos", "").strip())
            m = f"Temporizador de {seg} segundos iniciado"   
        print(m)
        talk(m)
    except:
        talk("No se ha especificado un tiempo válido.")
        return False

    
    hora = dt.datetime.now() + dt.timedelta(seconds=seg)
    while dt.datetime.now() < hora:
        pass

    talk("¡Tiempo cumplido!")
    print("¡Tiempo cumplido!")
    return False
            
def cerrar(g):
    print("Adiós :)")
    talk("Adiós")
    return True

comandos = {"reproduce":reproduce, "qué es":busqueda, "abre":abrir, "hora":hora, "día":día, "temporizador":temporizador, "vete":cerrar}

def juliana():
    talk("Hola, soy Juliana, ¿en qué puedo ayudarte?")
    while True:
        g = listen()
        cerrar = False
        for  key in comandos:
            if key in g:
                if key == "vete":
                    cerrar = comandos[key](g)
                else:  
                    cerrar = comandos[key](g)
                    m = "¿En qué más puedo ayudarte?"
                    talk(m)
                    print(m)
        if cerrar:
            break

if __name__ == "__main__":
    juliana()

"""Referencias: Daniiee - YouTube"
