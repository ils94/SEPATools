import json
import myPastebin
import misc
import setIcon
from tkinter import Toplevel, Entry, Label, Frame, X, LEFT, Button, messagebox


def criar_json(root, x, y, text):
    criar_json_janela = Toplevel(root)
    criar_json_janela.geometry("250x60+" + str(int(x)) + "+" + str(int(y)))
    criar_json_janela.resizable(False, False)
    criar_json_janela.attributes("-topmost", True)
    setIcon.icon(criar_json_janela, "json.ico")
    criar_json_janela.title("Criar JSON")

    def criar():

        novo_texto = ""

        if nome_arquivo.get() == "":
            messagebox.showerror("Erro", "É necessário escolher um nome para o arquivo.")
        else:

            lista = text.split("\n")

            for linha in lista:
                if linha is not "":
                    novo_texto += linha + "\n"

            estrutura = {"nomeArquivo": nome_arquivo.get().upper(),
                         "foraRelacao": "",
                         "relacao": novo_texto.replace(",", ": "),
                         "anotacoes": ""}

            arquivo_json = json.dumps(estrutura)

            criar_json_janela.destroy()

            myPastebin.paste(arquivo_json, root, x, y)

    frame1 = Frame(criar_json_janela)
    frame1.pack(fill=X)

    label_nome_arquivo = Label(frame1, text="Nome do Arquivo:", width=15, height=1)
    label_nome_arquivo.pack(side=LEFT, padx=2, pady=5)
    nome_arquivo = Entry(frame1, width=100)
    nome_arquivo.pack(side=LEFT, padx=2, pady=5)

    button_criar = Button(criar_json_janela, text="Criar", width=10, height=1,
                          command=lambda: misc.multithreading(criar))
    button_criar.pack()

    criar_json_janela.mainloop()
