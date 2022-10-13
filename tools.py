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

janela_width = 500
janela_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (janela_width / 2)
y = (screen_height / 2) - (janela_height / 2)

root.resizable(False, False)
root.geometry("500x500+" + str(int(x)) + "+" + str(int(y)))
root.iconbitmap('icones/tools.ico')
root.title("SEPATools")


def comparador():
    comparador_janela = Toplevel(root)
    comparador_janela.geometry("500x500+" + str(int(x)) + "+" + str(int(y)))
    comparador_janela.resizable(False, False)
    comparador_janela.iconbitmap("icones/compare.ico")
    comparador_janela.title("Comparador")

    def limpar(texto, campo):
        try:
            Stringio = StringIO(texto)

            df = pd.read_csv(Stringio)
            df.sort_values(by=["Patrimônio"], inplace=True)
            df["Patrimônio"] = df["Patrimônio"].apply(lambda x: '{0:0>6}'.format(x))

            df1 = df[["Patrimônio"]]

            df2 = df1.to_csv(header=None, index=False)

            campo.delete("1.0", END)
            campo.insert("1.0", str(df2).replace("\r", ""))
        except Exception as e:
            erro(e)

    def comparar(texto1, texto2):

        text_relacao_3.delete("1.0", END)

        list1 = texto1.split("\n")
        list2 = texto2.split("\n")

        set1 = set(list1)
        set2 = set(list2)

        missing = list(sorted(set1 - set2))

        for element in missing:
            text_relacao_3.insert("1.0", element + "\n")

    frame_1 = Frame(comparador_janela)
    frame_1.pack(side=LEFT, padx=1)

    text_relacao_1 = Text(frame_1, width=20, height=28)
    text_relacao_1.pack()

    button_limpar_1 = Button(frame_1, text="Filtrar", width=10, height=2,
                             command=lambda: limpar(text_relacao_1.get("1.0", END), text_relacao_1))
    button_limpar_1.pack(side=LEFT, pady=5)

    frame_2 = Frame(comparador_janela)
    frame_2.pack(side=LEFT, padx=1)

    text_relacao_2 = Text(frame_2, width=20, height=28)
    text_relacao_2.pack()

    button_limpar_2 = Button(frame_2, text="Filtrar", width=10, height=2,
                             command=lambda: limpar(text_relacao_2.get("1.0", END), text_relacao_2))
    button_limpar_2.pack(side=LEFT, pady=5)

    frame_3 = Frame(comparador_janela)
    frame_3.pack(side=LEFT, padx=1)

    text_relacao_3 = Text(frame_3, width=20, height=28)
    text_relacao_3.pack()

    button_comparar = Button(frame_3, text="Comparar", width=10, height=2,
                             command=lambda: comparar(text_relacao_1.get("1.0", END), text_relacao_2.get("1.0", END)))
    button_comparar.pack(side=LEFT, pady=5)

    salvar_csv_button = Button(frame_3, text="Para CSV", width=10, height=2,
                               command=lambda: multithreading(arquivoCSV(text_relacao_3.get("1.0", END))))
    salvar_csv_button.pack(side=RIGHT, pady=5)

    comparador_janela.mainloop()


def erro(e):
    messagebox.showerror("Erro", e)


def multithreading(funcao):
    x = threading.Thread(target=funcao)
    x.setDaemon(True)
    x.start()


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
    try:
        Stringio = StringIO(text.get("1.0", END))

        df = pd.read_csv(Stringio)
        df.sort_values(by=["Patrimônio"], inplace=True)
        df["Patrimônio"] = df["Patrimônio"].apply(lambda x: '{0:0>6}'.format(x))

        df1 = df[["Patrimônio"]]

        df2 = df1.to_csv(header=None, index=False)

        resultado = str(df2).replace("\r", "")

        text.delete("1.0", END)
        text.insert("1.0", resultado)

        pyperclip.copy(resultado)
    except Exception as e:
        erro(e)


def materialPatrimonio():
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

        resultado = str(df2).replace("\r", "")

        text.delete("1.0", END)
        text.insert("1.0", resultado)

        pyperclip.copy(str(df2))
    except Exception as e:
        erro(e)


def marcaPatrimonio():
    try:
        Stringio = StringIO(text.get("1.0", END))

        df = pd.read_csv(Stringio, sep=",")
        df.sort_values(by=["Patrimônio"], inplace=True)
        df["Patrimônio"] = df["Patrimônio"].apply(lambda x: '{0:0>6}'.format(x))

        df1 = df[["Marca", "Patrimônio"]]

        df2 = df1.to_csv(header=None, index=False)

        resultado = str(df2).replace("\r", "")

        text.delete("1.0", END)
        text.insert("1.0", resultado)

        pyperclip.copy(str(df2))
    except Exception as e:
        erro(e)


def arquivoCSV(texto):
    try:
        saida = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Arquivo CSV", "*.csv")])

        arquivo = open(saida, "wb")
        arquivo.write(bytes(texto, "utf-8"))
        arquivo.close()

        pergunta = messagebox.askyesno("Concluído", "Abrir arquivo?")

        if pergunta:
            os.startfile(saida)
    except Exception as e:
        erro(e)


def depreciacao():
    file_1 = filedialog.askopenfilename()

    file_2 = filedialog.askopenfilename()

    patrimonios_1 = []

    patrimonios_2 = []

    depreciacao_total = 0

    with open(file_1, "r") as f1:
        relacao_1 = f1.read()

    with open(file_2, "r") as f2:
        relacao_2 = f2.read()

    relacao_1_array = relacao_1.split("\n")

    relacao_2_array = relacao_2.split("\n")

    for i in relacao_1_array:
        filtro_1 = i.split(",")

        if filtro_1[1] != "0":
            patrimonios_1.append(filtro_1[0])

    for j in relacao_2_array:
        filtro_2 = j.split(",")

        if filtro_2[1] == "0":
            patrimonios_2.append(filtro_2[0])

    temp = [x for x in patrimonios_1 if x in patrimonios_2]

    counter = 0

    for valor in relacao_1_array:
        filtro_3 = valor.split(",")

        if filtro_3[0] in temp:
            counter = counter + 1

            depreciacao_total = depreciacao_total + float(filtro_3[1])

            text.insert("end", filtro_3[0] + " - R$ " + str(filtro_3[1]) + "\n")

    text.insert("1.0", "Total Achados: " + str(counter) + "\n\n")

    text.insert("end", "\nDepreciação Total: R$ " + str(round(depreciacao_total, 2)))


menubar = Menu(root)

menu_1 = Menu(menubar, tearoff=0)

menu_1.add_command(label="Mostrar QR code apenas", command=lambda: multithreading(apenasGerarQRCode))
menu_1.add_command(label="Gerar QR code sem brasão", command=lambda: multithreading(gerarQrCodeSemBrasao))
menu_1.add_command(label="Gerar QR code com brasão", command=lambda: multithreading(gerarQRCodeComBrasao))

menubar.add_cascade(label="QR Code", menu=menu_1)

menu_2 = Menu(menubar, tearoff=0)

menu_2.add_command(label="Apenas patrimônio", command=lambda: multithreading(apenasPatrimonio))
menu_2.add_command(label="Material + Patrimônio", command=lambda: multithreading(materialPatrimonio))
menu_2.add_command(label="Marca + Patrimônio", command=lambda: multithreading(marcaPatrimonio))

menubar.add_cascade(label="Padronizar", menu=menu_2)

menu_3 = Menu(menubar, tearoff=0)

menu_3.add_command(label="Abrir pastebin.com", command=lambda: multithreading(pasteBin))
menu_3.add_command(label="Salvar para um arquivo CSV", command=lambda: multithreading(arquivoCSV(text.get("1.0", END))))
menu_3.add_command(label="Abrir Comparador", command=comparador)
menu_3.add_command(label="Depreciação", command=lambda: multithreading(depreciacao))

menubar.add_cascade(label="Outros", menu=menu_3)

root.config(menu=menubar)

frame_text_widget = Frame(root)
frame_text_widget.pack()

text = Text(frame_text_widget, height=26, width=58)
text.pack(side=LEFT, pady=5, padx=5)

text_scrollbar = Scrollbar(frame_text_widget, command=text.yview, orient="vertical")
text_scrollbar.pack(fill=Y, side=RIGHT, pady=5)

text.configure(yscrollcommand=text_scrollbar.set)

button_copiar = Button(root, text="Copiar", width=10, height=2, command=lambda: pyperclip.copy(text.get("1.0", END)))
button_copiar.pack(side=LEFT, padx=5, pady=5)

button_copiar = Button(root, text="Apagar", width=10, height=2, command=lambda: text.delete("1.0", END))
button_copiar.pack(side=RIGHT, padx=5, pady=5)

root.mainloop()
