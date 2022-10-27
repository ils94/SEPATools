import threading
import tabula
from tkinter import messagebox, filedialog


def multithreading(funcao):
    x = threading.Thread(target=funcao)
    x.setDaemon(True)
    x.start()


def extrair_tabela():
    try:
        entrada = filedialog.askopenfilename(defaultextension=".csv", filetypes=[("Arquivo PDF", "*.pdf")])

        if entrada != "":
            tabula.convert_into(entrada, entrada + "_resultado.csv", output_format="csv", pages='all')

    except Exception as e:
        messagebox.showerror("Erro", str(e))
