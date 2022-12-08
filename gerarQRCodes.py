from tkinter import END, messagebox, filedialog
import cv2
import qrcode
import os
from PIL import Image


def apenasGerarQRCode(text):
    try:
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4, )
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

        img.save("QRcode.jpeg")

        image = cv2.imread("QRcode.jpeg")
        cv2.imshow("QR code", image)
        cv2.waitKey(0)
    except Exception as e:
        messagebox.showerror("Erro", str(e))


def gerarQrCodeSemBrasao(text):
    try:
        salvar = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes=[("JPG files", "*.jpg")])

        if salvar:
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4, )
            qr.add_data(text)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
            img.save(salvar)

            pergunta = messagebox.askyesno("QR code criado", "Abrir o arquivo?")

            if pergunta:
                os.startfile(salvar)
    except Exception as e:
        messagebox.showerror("Erro", str(e))


def gerarQRCodeComBrasao(text):
    try:
        salvar = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes=[("JPG files", "*.jpg")])

        if salvar:
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4, )
            qr.add_data(text)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

            brasao = Image.open('icones/brasao.ico')
            brasao.thumbnail((60, 60))
            brasaopos = ((img.size[0] - brasao.size[0]) // 2, (img.size[1] - brasao.size[1]) // 2)

            img.paste(brasao, brasaopos)
            img.save(salvar)

            pergunta = messagebox.askyesno("QR code criado", "Abrir o arquivo?")

            if pergunta:
                os.startfile(salvar)
    except Exception as e:
        messagebox.showerror("Erro", str(e))


def gerar(text, **kwargs):
    salvar = kwargs.get("salvar")
    brasao = kwargs.get("brasao")

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4, )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    if salvar:

        path = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes=[("JPG files", "*.jpg")])

        if path:
            if brasao:
                brasao = Image.open('icones/brasao.ico')
                brasao.thumbnail((60, 60))
                brasaopos = ((img.size[0] - brasao.size[0]) // 2, (img.size[1] - brasao.size[1]) // 2)
                img.paste(brasao, brasaopos)

            img.save(path)

            pergunta = messagebox.askyesno("QR code criado", "Abrir o arquivo?")

            if pergunta:
                os.startfile(path)
    else:

        img.save("QRcode.jpeg")

        image = cv2.imread("QRcode.jpeg")
        cv2.imshow("QR code", image)
        cv2.waitKey(0)
