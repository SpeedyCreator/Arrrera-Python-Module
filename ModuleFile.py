import os
import webbrowser

def RepertoireDev():
    webbrowser.open("/home/baptistep/Developement/")

def RepertoireDoc():
    webbrowser.open("/home/baptistep/Documents/")
def RepertoireImage():
    webbrowser.open("/home/baptistep/Images/")
def RepertoireMusique():
    webbrowser.open("/home/baptistep/Musique/")
def RepertoireTelechargement():
    webbrowser.open("/home/baptistep/Téléchargements/")
def RepertoireVideo():
    webbrowser.open("/home/baptistep/Vidéos/")

def DriveSecondaire():
    webbrowser.open("https://drive.google.com/drive/u/1/my-drive?hl=fr")
def DocsSecondaire():
    webbrowser.open("https://docs.google.com/presentation/u/1/")
def SlidesSecondaire():
    webbrowser.open("https://docs.google.com/presentation/u/1/")
def SheetsSecondaire():
    webbrowser.open("https://docs.google.com/spreadsheets/u/1/")

def DrivePrincipale():
    webbrowser.open("https://drive.google.com/drive/u/0/my-drive?hl=fr")
def DocsPrincipale():
    webbrowser.open("https://docs.google.com/presentation/u/0/")
def SlidesPrincipale():
    webbrowser.open("https://docs.google.com/presentation/u/0/")
def SheetsPrincipale():
    webbrowser.open("https://docs.google.com/spreadsheets/u/0/")

def FileSearch(name,path):
    for dirpath, dirname, filename in os.walk(path):
        if name in filename:
            return os.path.join(dirpath, name)