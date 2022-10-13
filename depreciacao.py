from tkinter import filedialog


def calcular(text):

    text.delete("1.0", "end")

    file_1 = filedialog.askopenfilename()

    file_2 = filedialog.askopenfilename()

    patrimonios_1 = []

    patrimonios_2 = []

    depreciacao_total = 0

    with open(file_1, "r") as f1:
        relacao_1 = f1.read()

    with open(file_2, "r") as f2:
        relacao_2 = f2.read()

    relacao_1_array = relacao_1.split("\n")

    relacao_2_array = relacao_2.split("\n")

    for i in relacao_1_array:
        filtro_1 = i.split(",")

        if filtro_1[1] != "0":
            patrimonios_1.append(filtro_1[0])

    for j in relacao_2_array:
        filtro_2 = j.split(",")

        if filtro_2[1] == "0":
            patrimonios_2.append(filtro_2[0])

    temp = [x for x in patrimonios_1 if x in patrimonios_2]

    counter = 0

    for valor in relacao_1_array:
        filtro_3 = valor.split(",")

        if filtro_3[0] in temp:
            counter = counter + 1

            depreciacao_total = depreciacao_total + float(filtro_3[1])

            text.insert("end", filtro_3[0] + " - R$ " + str(filtro_3[1]) + "\n")

    text.insert("1.0", "Total Achados: " + str(counter) + "\n\n")

    text.insert("end", "\nDepreciação Total: R$ " + str(round(depreciacao_total, 2)))
