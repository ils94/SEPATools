from tkinter import Menu, Frame, Text, LEFT, RIGHT, Scrollbar, Button, Y, END, Tk

import misc
import comparador
import filtrar
import gerarQRCodes
import myPastebin
import depreciacao
import arquivoCSV
import arquivoJSON
import setIcon

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
setIcon.icon(root, "tools.ico")
root.title("SEPATools")

menubar = Menu(root)

menu_1 = Menu(menubar, tearoff=0)

menu_1.add_command(label="Mostrar QR code apenas",
                   command=lambda: misc.multithreading(lambda: gerarQRCodes.gerar(text.get("1.0", "end"))))
menu_1.add_command(label="Gerar QR code sem brasão",
                   command=lambda: misc.multithreading(
                       lambda: gerarQRCodes.gerar(text.get("1.0", "end"), salvar="sim")))
menu_1.add_command(label="Gerar QR code com brasão",
                   command=lambda: misc.multithreading(
                       lambda: gerarQRCodes.gerar(text.get("1.0", "end"), salvar="sim", brasao="sim")))

menubar.add_cascade(label="QR Code", menu=menu_1)

menu_2 = Menu(menubar, tearoff=0)

sub_menu = Menu(menu_2, tearoff=False)
sub_menu.add_command(label="Apenas patrimônio",
                     command=lambda: misc.multithreading(lambda: filtrar.apenas_patrimonio(text)))
sub_menu.add_command(label="Material + Patrimônio",
                     command=lambda: misc.multithreading(lambda: filtrar.material_patrimonio(text)))
sub_menu.add_command(label="Marca + Patrimônio",
                     command=lambda: misc.multithreading(lambda: filtrar.marca_patrimonio(text)))

menu_2.add_cascade(label="Relação de bens", menu=sub_menu)

sub_menu = Menu(menu_2, tearoff=False)
sub_menu.add_command(label="Material + Patrimônio",
                     command=lambda: misc.multithreading(lambda: filtrar.termo_descricao_patrimonio(text)))
sub_menu.add_command(label="Somente patrimônios",
                     command=lambda: misc.multithreading(lambda: filtrar.termo_patrimonio(text)))

menu_2.add_cascade(label="Termo de Saída", menu=sub_menu)

menubar.add_cascade(label="Padronizar", menu=menu_2)

menu_3 = Menu(menubar, tearoff=0)

menu_3.add_command(label="Abrir pastebin.com", command=lambda: misc.multithreading(myPastebin.abrir))
menu_3.add_command(label="Criar Pastebin", command=lambda: arquivoJSON.criar_json(root, x, y, text.get("1.0", "end")))
menu_3.add_command(label="Salvar Credenciais", command=lambda: myPastebin.salvar_credenciais(root, x, y))

menubar.add_cascade(label="Pastebin", menu=menu_3)

menu_4 = Menu(menubar, tearoff=0)

menu_4.add_command(label="Salvar para um arquivo CSV",
                   command=lambda: misc.multithreading(arquivoCSV.salvar(text.get("1.0", END))))
menu_4.add_command(label="Abrir Comparador", command=lambda: comparador.comparar(root, x, y))
menu_4.add_command(label="Calculo de Depreciação", command=lambda: depreciacao.calcular(root, x, y))

menubar.add_cascade(label="Outros", menu=menu_4)

root.config(menu=menubar)

frame_text_widget = Frame(root)
frame_text_widget.pack()

text = Text(frame_text_widget, height=27, width=58)
text.pack(side=LEFT, pady=5, padx=5)

text_scrollbar = Scrollbar(frame_text_widget, command=text.yview, orient="vertical")
text_scrollbar.pack(fill=Y, side=RIGHT, pady=5)

text.configure(yscrollcommand=text_scrollbar.set)

button_copiar = Button(root, text="Copiar", width=10, height=1, command=lambda: pyperclip.copy(text.get("1.0", END)))
button_copiar.pack(side=LEFT, padx=5, pady=5)

button_copiar = Button(root, text="Apagar", width=10, height=1, command=lambda: text.delete("1.0", END))
button_copiar.pack(side=RIGHT, padx=5, pady=5)

root.mainloop()
