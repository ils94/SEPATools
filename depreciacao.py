from tkinter import filedialog, Toplevel, Frame, X, LEFT, Button, messagebox, END, Text
import misc
import pandas as pd
from io import StringIO


def calcular(root, x, y, text):
    calcular_janela = Toplevel(root)
    calcular_janela.attributes("-topmost", True)
    calcular_janela.geometry("500x100+" + str(int(x)) + "+" + str(int(y)))
    calcular_janela.resizable(False, False)
    calcular_janela.iconbitmap("icones/depreciacao.ico")
    calcular_janela.title("Calcular Depreciação")

    def limpeza(entry):
        try:
            novoTexto = ""

            cabecalho = ""

            rodape = ""

            split_1 = entry.get("1.0", "end").split("\n")

            for cabecalho1 in split_1[0:17]:
                cabecalho += cabecalho1 + "\n"

            for rodape1 in split_1[40:43]:
                rodape += rodape1 + "\n"

            limpo = entry.get("1.0", "end").replace(cabecalho, "").replace(rodape, "").split("\n")

            for linha in limpo:
                if "PA0365" in linha:
                    limpo.remove(linha)

            del limpo[-1]

            del limpo[-1]

            del limpo[-1]

            novoTexto += "a;b;c;d;e;f;g;h;i;j;k;l;m;n;o;p;q;r;s;\n"

            for novaLinha in limpo:
                novoTexto += novaLinha + "\n"

            return novoTexto
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def IO(texto):
        try:
            Stringio = StringIO(texto)

            df = pd.read_csv(Stringio, sep=";")

            df1 = df[["b", "m"]]

            df2 = df1.to_csv(header=None, index=False, sep=";")

            resultado = str(df2).replace("\r", "")

            resultado = resultado.replace(",", ".")

            return resultado
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def iniciar():
        try:
            if entry_lista_1 and entry_lista_2:

                text.delete("1.0", "end")

                patrimonios_1 = []

                patrimonios_2 = []

                depreciacao_total = 0

                relacao_1 = IO(limpeza(entry_lista_1))

                relacao_2 = IO(limpeza(entry_lista_2))

                relacao_1_array = relacao_1.split("\n")

                relacao_2_array = relacao_2.split("\n")

                relacao_1_array.remove("")
                relacao_2_array.remove("")

                for i in relacao_1_array:
                    filtro_1 = i.split(";")

                    if filtro_1[1] != "0.00":
                        patrimonios_1.append(filtro_1[0])

                for j in relacao_2_array:
                    filtro_2 = j.split(";")

                    if filtro_2[1] == "0.00":
                        patrimonios_2.append(filtro_2[0])

                temp = [x for x in patrimonios_1 if x in patrimonios_2]

                counter = 0

                for valor in relacao_1_array:
                    filtro_3 = valor.split(";")

                    if filtro_3[0] in temp:
                        counter = counter + 1

                        depreciacao_total = depreciacao_total + float(filtro_3[1])

                        text.insert("end", filtro_3[0] + " - R$ " + str(filtro_3[1]) + "\n")

                text.insert("1.0", "Total Achados: " + str(counter) + "\n\n")

                text.insert("end", "\nDepreciação Total: R$ " + str(round(depreciacao_total, 2)))
            else:
                messagebox.showerror("Erro", "Informe os dois arquivos.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def abrir(entry):
        entry.delete(0, END)
        entry.insert(END, filedialog.askopenfilename(defaultextension=".csv", filetypes=[("Arquivo CSV", "*.csv")]))

    frame1 = Frame(calcular_janela)
    frame1.pack(fill=X, pady=2)

    entry_lista_1 = Text(frame1, height=1)
    entry_lista_1.pack(side=LEFT, padx=5)

    frame2 = Frame(calcular_janela)
    frame2.pack(fill=X, pady=2)

    entry_lista_2 = Text(frame2, height=1)
    entry_lista_2.pack(side=LEFT, padx=5)

    button_calcular = Button(calcular_janela, text="Calcular", height=1, width=10,
                             command=lambda: misc.multithreading(iniciar()))
    button_calcular.pack(side=LEFT, pady=5, padx=5)

    entry_lista_1.insert(END, "Primeiro mês")
    entry_lista_2.insert(END, "Segundo mês")

    calcular_janela.mainloop()
