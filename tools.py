import os
import threading
import webbrowser
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import cv2
from io import StringIO
import pyperclip

import pandas as pd

import qrcode
from PIL import Image

root = Tk()
root.resizable(False, False)
root.geometry("500x500")
root.iconbitmap('icones/tools.ico')
root.title("SEPATools")

copia = ""


def apagar():
    text.delete("1.0", END)


def copiar():
    global copia
    pyperclip.copy(copia)


def erro(e):
    messagebox.showerror("Erro", e)


def multithreading(funcao):
    threading.Thread(target=funcao).start()


def pasteBin():
    try:
        webbrowser.open("https://pastebin.com/")
    except Exception as e:
        erro(e)


def apenasGerarQRCode():
    try:
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4, )
        qr.add_data(text.get("1.0", END))
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

        img.save("QRcode.jpeg")

        image = cv2.imread("QRcode.jpeg")
        cv2.imshow("QR code", image)
        cv2.waitKey(0)

    except Exception as e:
        erro(e)


def gerarQrCodeSemBrasao():
    try:
        salvar = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes=[("JPG files", "*.jpg")])

        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4, )
        qr.add_data(text.get("1.0", END))
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        img.save(salvar)

        pergunta = messagebox.askyesno("QR code criado", "Abrir o arquivo?")

        if pergunta:
            os.startfile(salvar)

    except Exception as e:
        erro(e)


def gerarQRCodeComBrasao():
    try:
        salvar = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes=[("JPG files", "*.jpg")])

        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4, )
        qr.add_data(text.get("1.0", END))
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

        brasao = Image.open('icones/brasao.ico')
        brasao.thumbnail((60, 60))

        brasaopos = ((img.size[0] - brasao.size[0]) // 2, (img.size[1] - brasao.size[1]) // 2)

        img.paste(brasao, brasaopos)

        img.save(salvar)

        pergunta = messagebox.askyesno("QR code criado", "Abrir o arquivo?")

        if pergunta:
            os.startfile(salvar)
    except Exception as e:
        erro(e)


def apenasPatrimonio():
    global copia
    try:
        Stringio = StringIO(text.get("1.0", END))

        df = pd.read_csv(Stringio)

        df.sort_values(by=["Patrimônio"], inplace=True)

        df["Patrimônio"] = df["Patrimônio"].apply(lambda x: '{0:0>6}'.format(x))

        df1 = df[["Patrimônio"]]

        df2 = df1.to_csv(header=None, index=False)

        text.delete("1.0", END)

        text.insert("1.0", str(df2))

        pyperclip.copy(str(df2))

        copia = str(df2)

    except Exception as e:
        erro(e)


def materialPatrimonio():
    global copia
    try:
        Stringio = StringIO(text.get("1.0", END))

        df = pd.read_csv(Stringio, sep=",")

        df.sort_values(by=["Patrimônio"], inplace=True)

        df["Material"] = df["Material"].str.replace("\d+", "").str.replace(" - ", "").str.replace(".",
                                                                                                  "").replace(
            "-", "").str[:30]

        df["Patrimônio"] = df["Patrimônio"].apply(lambda x: '{0:0>6}'.format(x))

        df1 = df[["Material", "Patrimônio"]]

        df2 = df1.to_csv(header=None, index=False)

        text.delete("1.0", END)

        text.insert("1.0", str(df2))

        pyperclip.copy(str(df2))

        copia = str(df2)
    except Exception as e:
        erro(e)


def marcaPatrimonio():
    global copia
    try:
        Stringio = StringIO(text.get("1.0", END))

        df = pd.read_csv(Stringio, sep=",")

        df.sort_values(by=["Patrimônio"], inplace=True)

        df["Patrimônio"] = df["Patrimônio"].apply(lambda x: '{0:0>6}'.format(x))

        df1 = df[["Marca", "Patrimônio"]]

        df2 = df1.to_csv(header=None, index=False)

        text.delete("1.0", END)

        text.insert("1.0", str(df2))

        pyperclip.copy(str(df2))

        copia = str(df2)
    except Exception as e:
        erro(e)


def arquivoCSV():
    global copia

    try:
        saida = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Arquivo CSV", "*.csv")])

        arquivo = open(saida, "wb")
        arquivo.write(bytes(copia, "utf-8"))
        arquivo.close()

        pergunta = messagebox.askyesno("Concluído", "Abrir arquivo?")

        if pergunta:
            os.startfile(saida)

    except Exception as e:
        erro(e)


menubar = Menu(root)

menu1 = Menu(menubar, tearoff=0)

menu1.add_command(label="Mostrar QR code apenas", command=lambda: multithreading(apenasGerarQRCode))
menu1.add_command(label="Gerar QR code sem brasão", command=lambda: multithreading(gerarQrCodeSemBrasao))
menu1.add_command(label="Gerar QR code com brasão", command=lambda: multithreading(gerarQRCodeComBrasao))

menubar.add_cascade(label="QR Code", menu=menu1)

menu2 = Menu(menubar, tearoff=0)

menu2.add_command(label="Apenas patrimônio", command=lambda: multithreading(apenasPatrimonio))
menu2.add_command(label="Material + Patrimônio", command=lambda: multithreading(materialPatrimonio))
menu2.add_command(label="Marca + Patrimônio", command=lambda: multithreading(marcaPatrimonio))

menubar.add_cascade(label="Padronizar", menu=menu2)

menu3 = Menu(menubar, tearoff=0)

menu3.add_command(label="Abrir pastebin.com", command=lambda: multithreading(pasteBin))
menu3.add_command(label="Salvar para um arquivo CSV", command=lambda: multithreading(arquivoCSV))

menubar.add_cascade(label="Outros", menu=menu3)

root.config(menu=menubar)

text = Text(root, height=27)
text.pack(pady=5, padx=5)

button_copiar = Button(root, text="Copiar", width=10, height=2, command=copiar)
button_copiar.pack(side=LEFT, padx=5, pady=5)

button_copiar = Button(root, text="Apagar", width=10, height=2, command=apagar)
button_copiar.pack(side=RIGHT, padx=5, pady=5)

root.mainloop()