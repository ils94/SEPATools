from tkinter import Menu, Frame, Text, LEFT, RIGHT, Scrollbar, Button, Y, END, Tk

import misc
import comparador
import filtrar
import gerarQRCodes
import pastebin
import depreciacao
import arquivoCSV

import pyperclip

root = Tk()

janela_width = 500
janela_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (janela_width / 2)
y = (screen_height / 2) - (janela_height / 2)

root.resizable(False, False)
root.geometry("500x500+" + str(int(x)) + "+" + str(int(y)))
root.iconbitmap('icones/tools.ico')
root.title("SEPATools")

menubar = Menu(root)

menu_1 = Menu(menubar, tearoff=0)

menu_1.add_command(label="Mostrar QR code apenas",
                   command=lambda: misc.multithreading(lambda: gerarQRCodes.gerar(text)))
menu_1.add_command(label="Gerar QR code sem brasão",
                   command=lambda: misc.multithreading(lambda: gerarQRCodes.gerar(text, salvar="sim")))
menu_1.add_command(label="Gerar QR code com brasão",
                   command=lambda: misc.multithreading(lambda: gerarQRCodes.gerar(text, salvar="sim", brasao="sim")))

menubar.add_cascade(label="QR Code", menu=menu_1)

menu_2 = Menu(menubar, tearoff=0)

menu_2.add_command(label="Apenas patrimônio",
                   command=lambda: misc.multithreading(lambda: filtrar.apenasPatrimonio(text)))
menu_2.add_command(label="Material + Patrimônio",
                   command=lambda: misc.multithreading(lambda: filtrar.materialPatrimonio(text)))
menu_2.add_command(label="Marca + Patrimônio",
                   command=lambda: misc.multithreading(lambda: filtrar.marcaPatrimonio(text)))

menubar.add_cascade(label="Padronizar", menu=menu_2)

menu_3 = Menu(menubar, tearoff=0)

menu_3.add_command(label="Abrir pastebin.com", command=lambda: misc.multithreading(pastebin.abrir))
menu_3.add_command(label="Salvar para um arquivo CSV",
                   command=lambda: misc.multithreading(arquivoCSV.salvar(text.get("1.0", END))))
menu_3.add_command(label="Abrir Comparador", command=lambda: comparador.comparar(root, x, y))
menu_3.add_command(label="Calculo de Depreciação",
                   command=lambda: misc.multithreading(lambda: depreciacao.calcular(text)))

menubar.add_cascade(label="Outros", menu=menu_3)

root.config(menu=menubar)

frame_text_widget = Frame(root)
frame_text_widget.pack()

text = Text(frame_text_widget, height=26, width=58)
text.pack(side=LEFT, pady=5, padx=5)

text_scrollbar = Scrollbar(frame_text_widget, command=text.yview, orient="vertical")
text_scrollbar.pack(fill=Y, side=RIGHT, pady=5)

text.configure(yscrollcommand=text_scrollbar.set)

button_copiar = Button(root, text="Copiar", width=10, height=2, command=lambda: pyperclip.copy(text.get("1.0", END)))
button_copiar.pack(side=LEFT, padx=5, pady=5)

button_copiar = Button(root, text="Apagar", width=10, height=2, command=lambda: text.delete("1.0", END))
button_copiar.pack(side=RIGHT, padx=5, pady=5)

root.mainloop()
