from io import StringIO
from tkinter import END, messagebox
import pandas as pd


def apenas_patrimonio(text):
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


def material_patrimonio(text):
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


def marca_patrimonio(text):
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


def termo_filtro(text):
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

        return Stringio

    except Exception as e:
        messagebox.showerror("Erro", str(e))


def termo_descricao_patrimonio(text):
    try:
        df = pd.read_csv(termo_filtro(text), sep=",")

        df["i"] = df["i"].str.replace("\d+", "").str.replace(" - ", "").str.replace(".", "").replace("-", "").str[:20]

        df["b"] = df["b"].apply(lambda x: '{0:0>6}'.format(x))

        df1 = df[["i", "b"]]

        df2 = df1.to_csv(header=None, index=False)

        resultado = str(df2).replace("\r", "")

        text.delete("1.0", END)
        text.insert("1.0", resultado)
    except Exception as e:
        messagebox.showerror("Erro", str(e))


def termo_patrimonio(text):
    try:
        df = pd.read_csv(termo_filtro(text), sep=",")

        df["b"] = df["b"].apply(lambda x: '{0:0>6}'.format(x))

        df1 = df[["b"]]

        df2 = df1.to_csv(header=None, index=False)

        resultado = str(df2).replace("\r", "")

        text.delete("1.0", END)
        text.insert("1.0", resultado)
    except Exception as e:
        messagebox.showerror("Erro", str(e))


def selecao_bens_patrimonios(text):
    try:
        # Read the CSV data from the text widget into a DataFrame
        df = pd.read_csv(StringIO(text.get("1.0", END)), sep=",")

        # Assuming "b" is the fourth column ("D")
        df.iloc[:, 3] = df.iloc[:, 3].apply(lambda x: '{0:0>6}'.format(x) if isinstance(x, int) else x)

        # Get the modified column "D" values, removing empty lines and "Patrimônio" string
        df_column_d = df.iloc[:, 3].dropna().loc[lambda x: x != 'Patrimônio']

        # Remove duplicates from the column
        df_column_d = df_column_d.drop_duplicates()

        # Convert the modified column to a CSV-formatted string without header
        resultado = df_column_d.to_csv(header=None, index=False)

        # Clean up string formatting
        resultado = resultado.replace("\r", "")

        # Clear the text widget and insert the result
        text.delete("1.0", END)
        text.insert("1.0", resultado)
    except Exception as e:
        messagebox.showerror("Erro", str(e))


def selecao_bens_descricao_patrimonios(text):
    try:
        # Read the CSV data from the text widget into a DataFrame
        df = pd.read_csv(StringIO(text.get("1.0", END)), sep=",")

        # Assuming "b" is the fourth column ("D")
        df.iloc[:, 3] = df.iloc[:, 3].apply(lambda x: '{0:0>6}'.format(x) if isinstance(x, int) else x)

        # Get the modified column "D" values, removing empty lines and "Patrimônio" string
        df_column_d = df.iloc[:, 3].dropna().loc[lambda x: x != 'Patrimônio']

        # Remove duplicates from the column
        df_column_d = df_column_d.drop_duplicates()

        # Get column number 9, removing "Descrição" and empty lines
        df_column_9 = df.iloc[:, 8].dropna().loc[lambda x: x != 'Descrição'].str.replace("\d+", "").str.replace(" - ",
                                                                                                                "").str.replace(
            ".", "").replace("-", "").str[:20]

        # Convert both columns to a DataFrame for display
        df_result = pd.concat([df_column_9, df_column_d], axis=1)

        # Convert the modified columns to a CSV-formatted string without header
        resultado = df_result.to_csv(header=None, index=False)

        # Clean up string formatting
        resultado = resultado.replace("\r", "")

        # Clear the text widget and insert the result
        text.delete("1.0", END)
        text.insert("1.0", resultado)
    except Exception as e:
        messagebox.showerror("Erro", str(e))
