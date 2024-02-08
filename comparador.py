from tkinter import Toplevel, END, Frame, LEFT, Text, Button, RIGHT, messagebox
from io import StringIO
import pandas as pd
import misc
import setIcon
import arquivoCSV
import filtrar
import centralizarJanelas


def comparar():
    toplevel = Toplevel()
    toplevel.geometry("500x500")
    toplevel.resizable(False, False)
    setIcon.icon(toplevel, "compare.ico")
    toplevel.title("Comparador")
    centralizarJanelas.center_window(toplevel, 500, 500)

    def filtro(text):
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
        except Exception:
            if "PA0155" in text.get("1.0", END):
                filtrar.selecao_bens_patrimonios(text)
            else:
                filtrar.termo_patrimonio(text)

    def comparar(texto1, texto2):
        text_relacao_3.delete("1.0", END)

        list1 = texto1.split("\n")
        list2 = texto2.split("\n")

        set1 = set(list1)
        set2 = set(list2)

        missing = list(sorted(set1 - set2))

        for element in missing:
            text_relacao_3.insert("1.0", element + "\n")

    frame_1 = Frame(toplevel)
    frame_1.pack(side=LEFT, padx=1)

    text_relacao_1 = Text(frame_1, width=20, height=28)
    text_relacao_1.pack()

    button_limpar_1 = Button(frame_1, text="Filtrar", width=10, height=2,
                             command=lambda: filtro(text_relacao_1))
    button_limpar_1.pack(side=LEFT, pady=5)

    frame_2 = Frame(toplevel)
    frame_2.pack(side=LEFT, padx=1)

    text_relacao_2 = Text(frame_2, width=20, height=28)
    text_relacao_2.pack()

    button_limpar_2 = Button(frame_2, text="Filtrar", width=10, height=2,
                             command=lambda: filtro(text_relacao_2))
    button_limpar_2.pack(side=LEFT, pady=5)

    frame_3 = Frame(toplevel)
    frame_3.pack(side=LEFT, padx=1)

    text_relacao_3 = Text(frame_3, width=20, height=28)
    text_relacao_3.pack()

    button_comparar = Button(frame_3, text="Comparar", width=10, height=2,
                             command=lambda: comparar(text_relacao_1.get("1.0", END), text_relacao_2.get("1.0", END)))
    button_comparar.pack(side=LEFT, pady=5)

    salvar_csv_button = Button(frame_3, text="Para CSV", width=10, height=2,
                               command=lambda: misc.multithreading(arquivoCSV.salvar(text_relacao_3.get("1.0", END))))
    salvar_csv_button.pack(side=RIGHT, pady=5)
