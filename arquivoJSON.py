import json
import myPastebin
import misc
import setIcon
from tkinter import Toplevel, Entry, Label, Frame, X, LEFT, Button, messagebox
import centralizarJanelas


def criar_json(text):
    toplevel = Toplevel()
    toplevel.geometry("250x60")
    toplevel.resizable(False, False)
    toplevel.attributes("-topmost", True)
    setIcon.icon(toplevel, "json.ico")
    toplevel.title("Criar JSON")
    centralizarJanelas.center_window(toplevel, 250, 60)

    def criar():

        novo_texto = ""

        if nome_arquivo.get() == "":
            messagebox.showerror("Erro", "É necessário escolher um nome para o arquivo.")
        else:

            lista = text.split("\n")

            for linha in lista:
                if linha != "":
                    novo_texto += linha + "\n"

            estrutura = {"nomeArquivo": nome_arquivo.get().upper(),
                         "foraRelacao": "",
                         "relacao": novo_texto.replace(",", ": "),
                         "anotacoes": ""}

            arquivo_json = json.dumps(estrutura)

            toplevel.destroy()

            myPastebin.checar_qrcode(arquivo_json)

    frame1 = Frame(toplevel)
    frame1.pack(fill=X)

    label_nome_arquivo = Label(frame1, text="Nome do Arquivo:", width=15, height=1)
    label_nome_arquivo.pack(side=LEFT, padx=2, pady=5)
    nome_arquivo = Entry(frame1, width=100)
    nome_arquivo.pack(side=LEFT, padx=2, pady=5)

    button_criar = Button(toplevel, text="Criar", width=10, height=1,
                          command=lambda: misc.multithreading(criar))
    button_criar.pack()

    toplevel.mainloop()
