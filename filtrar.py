from io import StringIO
from tkinter import END, messagebox
import pandas as pd


def apenasPatrimonio(text):
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
    except Exception as e:
        messagebox.showerror("Erro", str(e))


def materialPatrimonio(text):
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
    except Exception as e:
        messagebox.showerror("Erro", str(e))


def marcaPatrimonio(text):
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
    except Exception as e:
        messagebox.showerror("Erro", str(e))


def filtrarPorTermo(text):
    try:
        novo_texto = ""

        cabecalho = ""

        assinatura = """"Autorizo a saída do material acima relacionado




                        Em ____/___/_______",,,,,,,,,,,,,," 




                         Em ____/___/_______",,"Material Vistoriado 




                         Em ____/___/_______",,,,,
"          ____________________________________ 
                        Ass./Carimbo Patrimônio",,,,,,,,,,,,,,"         ____________________________________  
                                   Ass.Portador
     Nome:
   Identidade:",,"          ____________________________________ 
                                        Portaria",,,,,"""

        lista_entry = text.get("1.0", "end").split("\n")

        for linha in lista_entry[0:17]:
            cabecalho += linha + "\n"

        lista = text.get("1.0", "end").replace(cabecalho, "").replace(assinatura, "").split("\n")

        for linha in lista:
            if "PA0096" in linha:
                lista.remove(linha)

        del lista[-1]

        del lista[-1]

        del lista[-1]

        nova_lista = list(filter(None, lista))

        novo_texto += "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u\n"

        for linha in nova_lista:
            novo_texto += linha + "\n"

        Stringio = StringIO(novo_texto)

        df = pd.read_csv(Stringio, sep=",")

        df["i"] = df["i"].str.replace("\d+", "").str.replace(" - ", "").str.replace(".", "").replace("-", "").str[:20]

        df["b"] = df["b"].apply(lambda x: '{0:0>6}'.format(x))

        df1 = df[["i", "b"]]

        df2 = df1.to_csv(header=None, index=False)

        resultado = str(df2).replace("\r", "")

        text.delete("1.0", END)
        text.insert("1.0", resultado)
    except Exception as e:
        messagebox.showerror("Erro", str(e))
