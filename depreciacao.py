from tkinter import Toplevel, Frame, X, Y, LEFT, RIGHT, Button, messagebox, END, Text, Scrollbar
import misc
import pandas as pd
from io import StringIO
import pyperclip

resultado_tudo = ""
resultado_patrimonio = ""
resultado_valores = ""
resultado_depreciacao = ""
resultado_achados = ""
resultado_patrimonio_valores = ""


def calcular(root, x, y):
    calcular_janela = Toplevel(root)
    calcular_janela.geometry("500x500+" + str(int(x)) + "+" + str(int(y)))
    calcular_janela.resizable(False, False)
    calcular_janela.iconbitmap("icones/depreciacao.ico")
    calcular_janela.title("Calcular Depreciação")

    def botoes_valores(text, valor):
        text.delete("1.0", "end")
        text.insert("1.0", valor)

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
            messagebox.showerror("Erro em Limpeza", str(e))

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
            messagebox.showerror("Error no IO", str(e))

    def iniciar():

        global resultado_tudo, resultado_patrimonio, resultado_valores, resultado_depreciacao, resultado_achados, resultado_patrimonio_valores

        try:
            if entry_lista_1 and entry_lista_2:

                tudo["state"] = "normal"
                patrimonio["state"] = "normal"
                valores["state"] = "normal"

                resultado_text.delete("1.0", "end")

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

                        resultado_patrimonio_valores += filtro_3[0] + " - R$ " + str(filtro_3[1]) + "\n"

                        resultado_patrimonio += filtro_3[0] + "\n"

                        resultado_valores += str(filtro_3[1]) + "\n"

                resultado_achados = "Total Achados: " + str(counter)

                resultado_depreciacao = resultado_depreciacao = "Depreciação Total: R$ " + str(
                    round(depreciacao_total, 2))

                resultado_tudo = resultado_achados + "\n\n" + resultado_depreciacao + "\n\n" + resultado_patrimonio_valores

                resultado_text.insert("1.0", resultado_tudo)
            else:
                messagebox.showerror("Erro", "Informe os dois arquivos.")
        except Exception as e:
            messagebox.showerror("Error em Iniciar", str(e))

    frame1 = Frame(calcular_janela)
    frame1.pack(fill=X, pady=2)

    entry_lista_1 = Text(frame1, height=1)
    entry_lista_1.pack(side=LEFT, padx=5)

    frame2 = Frame(calcular_janela)
    frame2.pack(fill=X, pady=2)

    entry_lista_2 = Text(frame2, height=1)
    entry_lista_2.pack(side=LEFT, padx=5)

    frame3 = Frame(calcular_janela)
    frame3.pack(fill=X, pady=2, padx=3)

    tudo = Button(frame3, text="Tudo", height=1, width=5,
                  command=lambda: botoes_valores(resultado_text, resultado_tudo))
    tudo.pack(side=LEFT, padx=2)
    tudo["state"] = "disabled"

    patrimonio = Button(frame3, text="Só patrimônios", height=1, width=15,
                        command=lambda: botoes_valores(resultado_text, resultado_patrimonio))
    patrimonio.pack(side=LEFT, padx=2)
    patrimonio["state"] = "disabled"

    valores = Button(frame3, text="Só valores", height=1, width=10,
                     command=lambda: botoes_valores(resultado_text, resultado_valores))
    valores.pack(side=LEFT, padx=2)
    valores["state"] = "disabled"

    button_calcular = Button(frame3, text="Calcular", height=1, width=10,
                             command=lambda: misc.multithreading(iniciar()))
    button_calcular.pack(side=RIGHT, padx=2)

    frame4 = Frame(calcular_janela)
    frame4.pack()

    resultado_text = Text(frame4, height=24, width=58)
    resultado_text.pack(side=LEFT, padx=5, pady=2)

    text_scrollbar = Scrollbar(frame4, command=resultado_text.yview, orient="vertical")
    text_scrollbar.pack(fill=Y, side=RIGHT)

    resultado_text.configure(yscrollcommand=text_scrollbar.set)

    copiar = Button(calcular_janela, text="Copiar", height=1, width=10,
                    command=lambda: pyperclip.copy(resultado_text.get("1.0", "end")))
    copiar.pack(side=LEFT, pady=2, padx=5)

    entry_lista_1.insert(END, "Primeiro mês")
    entry_lista_2.insert(END, "Segundo mês")

    calcular_janela.mainloop()
