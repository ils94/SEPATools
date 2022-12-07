import json
from tkinter import END, Toplevel, Entry, Label, Frame, X, LEFT, Button


def criar_json(root, x, y, text):
    criar_json_janela = Toplevel(root)
    criar_json_janela.geometry("500x60+" + str(int(x)) + "+" + str(int(y)))
    criar_json_janela.resizable(False, False)
    criar_json_janela.iconbitmap("icones/depreciacao.ico")
    criar_json_janela.title("Criar JSON")

    def criar():
        estrutura = {"nomeArquivo": nome_arquivo.get(),
                     "foraRelacao": "",
                     "relacao": text.get("1.0", "end"),
                     "anotacoes": ""}

        arquivo_json = json.dumps(estrutura)

        text.delete("1.0", END)
        text.insert("1.0", arquivo_json)

    frame1 = Frame(criar_json_janela)
    frame1.pack(fill=X)

    label_nome_arquivo = Label(frame1, text="Nome do Arquivo:", width=15, height=1)
    label_nome_arquivo.pack(side=LEFT, padx=2, pady=5)
    nome_arquivo = Entry(frame1, width=100)
    nome_arquivo.pack(side=LEFT, padx=2, pady=5)

    button_criar = Button(criar_json_janela, text="Criar", width=10, height=1, command=criar)
    button_criar.pack()

    criar_json_janela.mainloop()
