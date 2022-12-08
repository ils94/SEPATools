import os


def icon(root, icon_file):
    if os.path.isfile("icones/" + icon_file):
        root.iconbitmap("icones/" + icon_file)
