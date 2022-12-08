import webbrowser
from tkinter import messagebox
import urllib.request
from urllib.parse import urlencode
import gerarQRCodes


def abrir():
    try:
        webbrowser.open("https://pastebin.com/")
    except Exception as e:
        messagebox.showerror("Erro", str(e))


def paste():
    site = 'https://pastebin.com/api/api_post.php'
    dev_key = 'chave aqui'
    code = "banana"
    our_data = urllib.parse.urlencode({"api_dev_key": dev_key,
                                       "api_option": "paste",
                                       "api_paste_code": code,
                                       "api_paste_expire_dat": "10M"})
    our_data = our_data.encode()
    request = urllib.request.Request(site, method='POST')
    resp = urllib.request.urlopen(request, our_data)
    _url = str(resp.read()).split("/")
    new_url = "https://pastebin.com/raw/" + _url[3]

    print(_url)

    gerarQRCodes.gerar(new_url)
