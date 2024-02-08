import tkinter as tk
import centralizarJanelas
import pyperclip
import setIcon


def mostrarDuplicados():
    toplevel = tk.Toplevel()
    toplevel.title("Números Duplicados")
    toplevel.geometry("500x500")
    toplevel.resizable(False, False)
    setIcon.icon(toplevel, "duplicado.ico")
    centralizarJanelas.center_window(toplevel, 500, 500)

    def achar():
        numeros = text_box.get("1.0", tk.END)
        text_box.delete("1.0", tk.END)
        result = find_duplicates(numeros)
        text_box.insert(tk.END, result)

    text_box = tk.Text(toplevel, height=5, width=30)
    text_box.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    frame = tk.Frame(toplevel)
    frame.pack(fill=tk.X)

    find_button = tk.Button(frame, text="Mostrar", command=achar)
    find_button.pack(side=tk.LEFT, padx=5, pady=5)


def find_duplicates(numbers_text):
    numbers = [int(x) for x in numbers_text.split() if x.strip()]
    duplicates = {}
    result_string = ""
    numeros = ""

    for number in numbers:
        if number in duplicates:
            duplicates[number] += 1
        else:
            duplicates[number] = 1

    for number, count in duplicates.items():
        if count > 1:
            result_string += f'"{number}" foi repetido {count} vezes nesta lista.\n'
            numeros += f"{number}\n"

    pyperclip.copy(numeros)
    return result_string.strip()
