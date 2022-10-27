import threading


def multithreading(funcao):
    x = threading.Thread(target=funcao)
    x.setDaemon(True)
    x.start()
