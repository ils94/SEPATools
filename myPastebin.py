import webbrowser
from tkinter import messagebox, Toplevel, Frame, Label, LEFT, RIGHT, Entry, Button, X, W
import pastebin3
import os
import json
import pathlib
import gerarQRCodes
import setIcon
import cv2
import time
import datetime

user_home = "Z:/" + str(os.getlogin())

creds_arquivo = pathlib.Path(user_home + "/pastebin/creds.json")

creds_pasta = pathlib.Path(user_home + "/pastebin")

if not creds_pasta.exists():
    os.makedirs(user_home + "/pastebin")


def abrir():
    try:
        webbrowser.open("https://pastebin.com/")
    except Exception as e:
        messagebox.showerror("Erro", str(e))


def paste(text, root, x, y):
    try:
        if os.path.isfile("QRcode.jpeg"):
            data_criacao = os.path.getmtime("QRcode.jpeg")

            tempo = datetime.datetime.strptime(time.ctime(data_criacao), "%c")

            tempo_lista = str(tempo).split(" ")
            data = tempo_lista[0].split("-")
            nova_data = data[2] + "/" + data[1] + "/" + data[0]

            pergunta = messagebox.askyesno("QR Code existente encontrado",
                                           "Há um QR Code criado ás " + tempo_lista[1]
                                           + " no dia " + nova_data + ". Deseja abri-lo?")

            if pergunta:
                image = cv2.imread("QRcode.jpeg")
                cv2.imshow("QR code", image)
                cv2.waitKey(0)

            else:
                if creds_arquivo.exists():
                    with open(creds_arquivo) as js:
                        creds = json.load(js)

                    dev_key = creds["dev_key"]
                    user_name = creds["user_name"]
                    user_password = creds["user_password"]

                    api_user_key = pastebin3.api_user_key(dev_key=dev_key, user_name=user_name,
                                                          user_password=user_password)

                    rs = pastebin3.paste(dev_key=dev_key, code=text, user_key=api_user_key, expire_date="10M",
                                         private="public")

                    new_url = "https://pastebin.com/raw/" + rs.replace("https://pastebin.com/", "")

                    gerarQRCodes.gerar(new_url)

                else:
                    salvar_credenciais(root, x, y)
    except Exception as e:
        messagebox.showerror("Erro", str(e))


def salvar_credenciais(root, x, y):
    salvar_credenciais_janela = Toplevel(root)
    salvar_credenciais_janela.geometry("300x130+" + str(int(x)) + "+" + str(int(y)))
    salvar_credenciais_janela.resizable(False, False)
    salvar_credenciais_janela.attributes("-topmost", True)
    setIcon.icon(salvar_credenciais_janela, "cadeado.ico")
    salvar_credenciais_janela.title("Salvar Credenciais")

    def salvar():
        try:

            if entry_dev_key.get() == "" or entry_user_name.get() == "" or entry_user_password.get() == "":
                messagebox.showerror("Erro", "Preencha todos os campos.")
            else:
                data = {}

                data["dev_key"] = entry_dev_key.get()
                data["user_name"] = entry_user_name.get()
                data["user_password"] = entry_user_password.get()

                json_data = json.dumps(data)

                salvar_json = open(user_home + "/pastebin/creds.json", "w")
                salvar_json.write(str(json_data))
                salvar_json.close()

                messagebox.showinfo("Salvo", "As credenciais foram salvas com sucesso.")

                salvar_credenciais_janela.destroy()

        except Exception as e:
            messagebox.showerror("Erro", str(e))

    frame1 = Frame(salvar_credenciais_janela)
    frame1.pack(fill=X)

    label_dev_key = Label(frame1, text="Dev Key:", width=8, height=1, anchor=W)
    label_dev_key.pack(side=LEFT, padx=1, pady=5)

    entry_dev_key = Entry(frame1, width=35)
    entry_dev_key.pack(side=LEFT, padx=1, pady=5)

    frame2 = Frame(salvar_credenciais_janela)
    frame2.pack(fill=X)

    label_user_name = Label(frame2, text="Usuário:", width=8, height=1, anchor=W)
    label_user_name.pack(side=LEFT, padx=1, pady=5)

    entry_user_name = Entry(frame2, width=35)
    entry_user_name.pack(side=LEFT, padx=1, pady=5)

    frame3 = Frame(salvar_credenciais_janela)
    frame3.pack(fill=X)

    label_user_password = Label(frame3, text="Senha:", width=8, height=1, anchor=W)
    label_user_password.pack(side=LEFT, padx=1, pady=5)

    entry_user_password = Entry(frame3, width=35, show="*")
    entry_user_password.pack(side=LEFT, padx=1, pady=5)

    frame4 = Frame(salvar_credenciais_janela)
    frame4.pack(fill=X)

    button_salvar = Button(frame4, text="Salvar", width=10, height=1, command=salvar)
    button_salvar.pack(side=RIGHT, padx=5, pady=5)
