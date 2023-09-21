import serial
import serial.tools.list_ports
import time
import pyautogui
import webbrowser
import win32console
import win32gui

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
        pyautogui.hotkey('win', 'r')
        pyautogui.write('C:/Users/golal/AppData/Local/Programs/Microsoft VS Code/Code.exe')
        pyautogui.hotkey('enter')
    if('Escritorio,BtnD' in deck):
        pyautogui.hotkey('win', 'r')
        pyautogui.write('C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe')
        pyautogui.hotkey('enter')
    if('Escritorio,BtnE' in deck):
        pyautogui.hotkey('win', 'r')
        pyautogui.write('C:/Program Files (x86)/Steam/steam.exe')
        pyautogui.hotkey('enter')
    if('Escritorio,BtnF' in deck):
        pyautogui.hotkey('win', 'r')
        pyautogui.write('C:/Users/golal/AppData/Local/Amazon Games/App/Amazon Games.exe')
        pyautogui.hotkey('enter')
    if('Escritorio,BtnG' in deck):
        pyautogui.hotkey('win', 'r')
        pyautogui.write('soffice')
        pyautogui.hotkey('enter')
    if('Escritorio,BtnH' in deck):
        pyautogui.hotkey('win', 'r')
        pyautogui.write('"D:/Riot Games/Riot Client/RiotClientServices.exe" --launch-product=league_of_legends --launch-patchline=live')
        pyautogui.hotkey('enter')
    if('Escritorio,BtnI' in deck):
        pyautogui.hotkey('win', 'r')
        pyautogui.write('C:/Program Files/MySQL/MySQL Workbench 8.0/MySQLWorkbench.exe')
        pyautogui.hotkey('enter')
    if('Escritorio,btnJ' in deck):
        pyautogui.hotkey('win', 'r')
        pyautogui.write('Notepad')
        pyautogui.hotkey('enter')
    if('Escritorio,but' in deck):
        pyautogui.hotkey('volumemute')
    if('Escritorio,izq' in deck):
        pyautogui.hotkey('volumedown')
    if('Escritorio,der' in deck):
        pyautogui.hotkey('volumeup')

def edicion():
    if('Edicion,BtnA' in deck):
        pyautogui.hotkey('win', 'r')
        pyautogui.write('Photoshop')
        pyautogui.hotkey('enter')
    if('Edicion,BtnB' in deck):
        pyautogui.hotkey('win', 'r')
        pyautogui.write('"Adobe Premiere Pro"')
        pyautogui.hotkey('enter')
    if('Edicion,BtnC' in deck):
        pyautogui.hotkey('win', 'r')
        pyautogui.write('"Adobe Audition"')
        pyautogui.hotkey('enter')
    if('Edicion,BtnD' in deck):
        pyautogui.hotkey('win', 'r')
        pyautogui.write('Illustrator')
        pyautogui.hotkey('enter')
    if('Edicion,BtnE' in deck):
        pyautogui.hotkey('win', 'r')
        pyautogui.write('AfterFX')
        pyautogui.hotkey('enter')
    if('Edicion,BtnF' in deck):
        pyautogui.hotkey('win', 'r')
        pyautogui.write('C:/Program Files/Blackmagic Design/DaVinci Resolve/Resolve.exe')
        pyautogui.hotkey('enter')
    if('Edicion,BtnG' in deck):
        webbrowser.open('https://www.ilovepdf.com/es')
    if('Edicion,BtnH' in deck):
        pyautogui.hotkey('win', 'r')
        pyautogui.write('D:/LDL/LDPlayer/LDPlayer4.0/dnplayer.exe')
        pyautogui.hotkey('enter')
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
        pyautogui.hotkey('f13')
    if('OBS,BtnB' in deck):
        pyautogui.hotkey('f14')
    if('OBS,BtnC' in deck):
        pyautogui.hotkey('f15')
    if('OBS,BtnD' in deck):
        pyautogui.hotkey('f16')
    if('OBS,BtnE' in deck):
        pyautogui.hotkey('f17')
    if('OBS,BtnF' in deck):
        pyautogui.hotkey('f18')
    if('OBS,BtnG' in deck):
        pyautogui.hotkey('f19')
    if('OBS,BtnH' in deck):
        pyautogui.hotkey('f20')
    if('OBS,BtnI' in deck):
        pyautogui.hotkey('f21')
    if('OBS,btnJ' in deck):
        pyautogui.hotkey('win', 'r')
        pyautogui.write('C:/Program Files/obs-studio/bin/64bit/obs64.exe')
        pyautogui.hotkey('enter')
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
        webbrowser.open('https://play.hbomax.com/page/urn:hbo:page:home')
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

def redes():
    if('Redes,BtnA' in deck):
        webbrowser.open('https://gmail.com/')
    if('Redes,BtnB' in deck):
        webbrowser.open('https://www.facebook.com/')
    if('Redes,BtnC' in deck):
        pyautogui.hotkey('win', 'r')
        pyautogui.write('C:/Users/golal/AppData/Local/Discord/Update.exe --processStart Discord.exe')
        pyautogui.hotkey('enter')
    if('Redes,BtnD' in deck):
        webbrowser.open('https://campus.uvq.edu.ar/')
    if('Redes,BtnE' in deck):
        webbrowser.open('https://login.yahoo.com/')
    if('Redes,BtnF' in deck):
        webbrowser.open('https://mail.enacom.gob.ar')
    if('Redes,BtnG' in deck):
        pyautogui.hotkey('win', 'r')
        pyautogui.write('C:/Aplicaciones store/Whatsapp.lnk')
        pyautogui.hotkey('enter')
    if('Redes,BtnH' in deck):
        pyautogui.hotkey('win', 'r')
        pyautogui.write('C:/Users/golal/AppData/Roaming/Telegram Desktop/Telegram.exe')
        pyautogui.hotkey('enter')
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
    redes()
