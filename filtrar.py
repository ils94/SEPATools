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
