"""
    by:Srv
"""

from tkinter import *
import tkinter
from tkinter.filedialog import *
import os


window = Tk()
window.title("Encrypter...")
window.geometry("500x300")

#open file
def openfile():
    global filename
    filename = askopenfilename()
    #print(filename)
    label = Label(window, text="file selected: "+filename)
    label.place(relx=0.5, rely=0.2, anchor=CENTER)


#encyption of file using X-OR
def encrypt_decrypt():
    asc=0
    with open(filename,'rb') as f:
        data = f.read()
        f.close()
    fkey = key_box.get()
    if fkey.isnumeric() != True:
        for i in fkey:
            asc = asc + ord(i)
        if int(asc)>255:
            asc=asc//4
        fkey = int(asc)
    #encrypt
    data = bytearray(data)
    for index,values in enumerate(data):
        data[index] = values ^ int(fkey)
    if filename[-4:]!=".enc":
        with open(filename+".enc",'wb') as f1:
            f1.write(data)
            f1.close()
        os.remove(filename)
    else:
        with open(filename[:-4],'wb') as f1:
            f1.write(data)
            f1.close()
        os.remove(filename)
    label = Label(window, text="Encrypted/Decrypted succesfully!")
    label.place(relx=0.5, rely=0.3, anchor=CENTER)


#get the input from key_box
key_box = Entry(window)


#labels
label = Label(window, text="Select a file")
button = Button(window, text="Browse", command=openfile)
button_enctypt = Button(window, text="Encrypt / Decrypt", command=encrypt_decrypt)
label_password = Label(window, text="Password:")



#placing button and labels
key_box.place(relx=0.5, rely=0.5, anchor=CENTER)
button.place(relx=0.5, rely=0.4, anchor=CENTER)
label.place(relx=0.5, rely=0.2, anchor=CENTER)
button_enctypt.place(relx=0.5, rely=0.6, anchor=CENTER)
label_password.place(relx=0.3, rely=0.5, anchor=CENTER)

window.mainloop()