from pynput.keyboard import Key, Listener
from PIL import Image, ImageTk
import threading
import tkinter as tk
import pygame

def open_image():
    try:
        window = tk.Toplevel()
        window.title("JOHN CENA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        window.geometry("620x400")
        window.configure(background='gray')

        # Define o ícone da janela
        window.iconbitmap("app\medias\JC_icone.ico")

        # Abre a imagem original
        original_image = Image.open("app/medias/JC_image.jpg")

        # Redimensiona a imagem para se ajustar à janela
        resized_image = original_image.resize((620, 400), Image.ANTIALIAS)

        img = ImageTk.PhotoImage(resized_image)
        panel = tk.Label(window)
        panel.configure(image=img)
        panel.pack(side="bottom", fill="both", expand="yes")
        panel.image = img  # Armazena a imagem como atributo do objeto Label

        window.attributes("-topmost", True)

        # Reproduz o áudio
        pygame.mixer.init()
        pygame.mixer.music.load("app/medias/Jhon_cena.mp3")
        pygame.mixer.music.play()

        window.mainloop()
    except Exception as e:
        print()

def on_press(key):
    try:
        KEY = key.char.lower()
        if KEY in ['c', 'e', 'n', 'a']:
            for _ in range(20):
                thread = threading.Thread(target=open_image)
                thread.start()
    except:
        pass
    return True

with Listener(on_press=on_press) as listener:
    listener.join()
