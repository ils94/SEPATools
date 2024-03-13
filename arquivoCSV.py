from tkinter import filedialog, messagebox


def salvar(texto):
    try:
        saida = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Arquivo CSV", "*.csv")])

        if saida != "":
            arquivo = open(saida, "wb")
            arquivo.write(bytes(texto, "utf-8"))
            arquivo.close()

    except Exception as e:
        messagebox.showerror("Erro", str(e))
