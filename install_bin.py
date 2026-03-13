# import module
from zipfile import ZipFile
from tkinter import messagebox
from urllib.request import urlretrieve
import os 


# ask choose 
choose = messagebox.askyesno(title="TEME binary Installer",message="Would you install bin ( openssl ) in local ?")

if choose == 1:

    # extract it
    with ZipFile(f"openssl_bin.zip","r") as zip_file:
        zip_file.extractall("bin") 


    # finish
    messagebox.showinfo(title="TEME binary Installer",message="OpenSSL bin installed correctly")

else:
    # quit
    messagebox.showinfo(title="TEME binary Installer",message="Ok, good bye!")
