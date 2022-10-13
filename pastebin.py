import webbrowser
from tkinter import messagebox


def abrir():
    try:
        webbrowser.open("https://pastebin.com/")
    except Exception as e:
        messagebox.showerror("Erro", str(e))
