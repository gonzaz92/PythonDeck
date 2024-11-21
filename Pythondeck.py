import serial
import serial.tools.list_ports
import time
import pyautogui
import webbrowser
import win32console
import win32gui
from subprocess import Popen
from os import startfile
from obswebsocket import obsws, requests

def escena(a):
    client = obsws('localhost', 4455, '')
    client.connect()
    escena = a
    client.call(requests.SetCurrentProgramScene(sceneName=escena))
    client.disconnect()

def comando(a):
    try:
        escena(a)
    except:
        print('No funciona')

#Oculta el shell de pytho al abrir el script
ventana = win32console.GetConsoleWindow()
win32gui.ShowWindow(ventana,0)

# Detección de puerto
Puerto = serial.tools.list_ports.comports()

for ports in Puerto:
    if 'CH340' in str(ports):
        port = str(ports)[0:4]

#Conexión serial
Pythondeck = serial.Serial(port, 9600)
time.sleep(1)

#Funciones para el menú
def escritorio():
    if('Escritorio,BtnA' in deck):
        webbrowser.open('firefox')
    if('Escritorio,BtnB' in deck):
        pyautogui.hotkey('alt', 'r')
    if('Escritorio,BtnC' in deck):
        Popen('"C:/Program Files/TeamViewer/TeamViewer.exe"', shell=True)
    if('Escritorio,BtnD' in deck):
        Popen('C:/Program Files (x86)/Epic Games/Launcher/Portal/Binaries/Win32/EpicGamesLauncher.exe', shell=True)
    if('Escritorio,BtnE' in deck):
        Popen('C:/Program Files (x86)/Steam/steam.exe', shell=True)
    if('Escritorio,BtnF' in deck):
        Popen('C:/Users/golal/AppData/Local/Amazon Games/App/Amazon Games.exe', shell=True)
    if('Escritorio,BtnG' in deck):
        Popen('C:/Program Files/LibreOffice/program/soffice.exe', shell=True)
    if('Escritorio,BtnH' in deck):
        Popen('"D:/Riot Games/Riot Client/RiotClientServices.exe" --launch-product=league_of_legends --launch-patchline=live', shell=True)
    if('Escritorio,BtnI' in deck):
        Popen('C:/Program Files/MySQL/MySQL Workbench 8.0/MySQLWorkbench.exe', shell=True)
    if('Escritorio,btnJ' in deck):
        Popen('Notepad.exe', shell=True)
    if('Escritorio,but' in deck):
        pyautogui.hotkey('volumemute')
    if('Escritorio,izq' in deck):
        pyautogui.hotkey('volumedown')
    if('Escritorio,der' in deck):
        pyautogui.hotkey('volumeup')

def edicion():
    if('Edicion,BtnA' in deck):
        Popen('C:/Program Files/GIMP 2/bin/gimp-2.10.exe', shell=True)
    if('Edicion,BtnB' in deck):
        Popen('C:/Program Files/Blackmagic Design/DaVinci Resolve/Resolve.exe', shell=True)
    if('Edicion,BtnC' in deck):
        Popen('C:/Program Files/REAPER (x64)/reaper.exe', shell=True)
    if('Edicion,BtnD' in deck):
        Popen('C:/Program Files/Inkscape/bin/inkscape.exe', shell=True)
    if('Edicion,BtnE' in deck):
        Popen('C:/Program Files/darktable/bin/darktable.exe', shell=True)
    if('Edicion,BtnF' in deck):
        Popen('C:/Program Files/Krita (x64)/bin/krita.exe', shell=True)
    if('Edicion,BtnG' in deck):
        webbrowser.open('https://www.ilovepdf.com/es')
    if('Edicion,BtnH' in deck):
        Popen('D:/LDPlayer/LDPlayer9/dnplayer.exe', shell=True)
    if('Edicion,BtnI' in deck):
        pyautogui.hotkey('f15')
    if('Edicion,btnJ' in deck):
        pyautogui.hotkey('f16')
    if('Edicion,but' in deck):
        pyautogui.hotkey('f17')
    if('Edicion,izq' in deck):
        pyautogui.hotkey('f18')
    if('Edicion,der' in deck):
        pyautogui.hotkey('f19')

def obs():
    if('OBS,BtnA' in deck):
        comando('Apertura')
    if('OBS,BtnB' in deck):
        comando('League of Legend')
    if('OBS,BtnC' in deck):
        comando('LOL')
    if('OBS,BtnD' in deck):
        comando('Cam')
    if('OBS,BtnE' in deck):
        comando('Juegos Varios')
    if('OBS,BtnF' in deck):
        comando('Navegador')
    if('OBS,BtnG' in deck):
        comando('Pantalla')
    if('OBS,BtnH' in deck):
        comando('Celular')
    if('OBS,BtnI' in deck):
        pyautogui.hotkey('f21')
    if('OBS,btnJ' in deck):
        startfile('C:/Aplicaciones store/OBS Studio.lnk')
    if('OBS,but' in deck):
        pyautogui.hotkey('f22')
    if('OBS,izq' in deck):
        pyautogui.hotkey('f23')
    if('OBS,der' in deck):
        pyautogui.hotkey('f24')

def streaming():
    if('Streaming,BtnA' in deck):
        webbrowser.open('https://tv.movistar.com.ar/')
    if('Streaming,BtnB' in deck):
        webbrowser.open('https://www.primevideo.com/')
    if('Streaming,BtnC' in deck):
        webbrowser.open('https://play.max.com/')
    if('Streaming,BtnD' in deck):
        webbrowser.open('https://www.crunchyroll.com/es')
    if('Streaming,BtnE' in deck):
        webbrowser.open('https://www.youtube.com/')
    if('Streaming,BtnF' in deck):
        webbrowser.open('https://www.twitch.tv/')
    if('Streaming,BtnG' in deck):
        pyautogui.hotkey('right')
    if('Streaming,BtnH' in deck):
        pyautogui.hotkey('playpause')
    if('Streaming,BtnI' in deck):
        pyautogui.hotkey('left')
    if('Streaming,btnJ' in deck):
        pyautogui.hotkey('nexttrack')
    if('Streaming,but' in deck):
        pyautogui.hotkey('volumemute')
    if('Streaming,izq' in deck):
        pyautogui.hotkey('volumedown')
    if('Streaming,der' in deck):
        pyautogui.hotkey('volumeup')

def programacion():
    if('Programacion,BtnA' in deck):
        pyautogui.hotkey('ctrl', 'shift','e')
    if('Programacion,BtnB' in deck):
        pyautogui.hotkey('ctrl', 'b')
    if('Programacion,BtnC' in deck):
        pyautogui.hotkey('ctrl', 'h')
    if('Programacion,BtnD' in deck):
        pyautogui.hotkey('ctrl', 'shift', 'x')
    if('Programacion,BtnE' in deck):
        pyautogui.hotkey('ctrl', 'win', 'alt', 'n')
    if('Programacion,BtnF' in deck):
        pyautogui.hotkey('ctrl', 'shift', 'd')
    if('Programacion,BtnG' in deck):
        pyautogui.hotkey('ctrl', 'k')
        pyautogui.hotkey('ctrl', 'c')
    if('Programacion,BtnH' in deck):
        pyautogui.hotkey('ctrl', 'k')
        pyautogui.hotkey('ctrl', 'u')
    if('Programacion,BtnI' in deck):
        Popen('C:/Program Files (x86)/Thonny/thonny.exe', shell=True)
    if('Programacion,btnJ' in deck):
        Popen('C:/Users/golal/AppData/Local/Programs/Microsoft VS Code/Code.exe', shell=True)
    if('Programacion,but' in deck):
        Popen('C:/Program Files/Git/git-bash.exe', shell=True)
    if('Programacion,izq' in deck):
        pyautogui.hotkey('ctrl', 'k')
    if('Programacion,der' in deck):
        pyautogui.hotkey('ctrl', 'o')

def redes():
    if('Redes,BtnA' in deck):
        webbrowser.open('https://gmail.com/')
    if('Redes,BtnB' in deck):
        webbrowser.open('https://www.facebook.com/')
    if('Redes,BtnC' in deck):
        Popen('C:/Users/golal/AppData/Local/Discord/Update.exe --processStart Discord.exe', shell=True)
    if('Redes,BtnD' in deck):
        webbrowser.open('https://campus.uvq.edu.ar/')
    if('Redes,BtnE' in deck):
        webbrowser.open('https://login.yahoo.com/')
    if('Redes,BtnF' in deck):
        webbrowser.open('https://mail.enacom.gob.ar')
    if('Redes,BtnG' in deck):
        startfile('C:/Aplicaciones store/Whatsapp.lnk')
    if('Redes,BtnH' in deck):
        Popen('C:/Users/golal/AppData/Roaming/Telegram Desktop/Telegram.exe', shell=True)
    if('Redes,BtnI' in deck):
        webbrowser.open('https://plataforma.coderhouse.com/ingresar')
    if('Redes,btnJ' in deck):
        webbrowser.open('https://github.com/gonzaz92')
    if('Redes,but' in deck):
        pyautogui.hotkey('volumemute')
    if('Redes,izq' in deck):
        pyautogui.hotkey('volumedown')
    if('Redes,der' in deck):
        pyautogui.hotkey('volumeup')

while True:
    deck = Pythondeck.readline().decode('ascii')
    escritorio()
    edicion()
    obs()
    streaming()
    programacion()
    redes()
