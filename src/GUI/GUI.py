import tkinter
from tkinter import filedialog
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image


def pilih_folder():
    dipilih = filedialog.askdirectory()
    if dipilih:
        showinfo(title = "Folder Telah Dipilih", message = dipilih)
        
frame = tkinter.Tk()
frame.geometry("1067x600")
frame.title("FACE RECOGNITION")
gambar = tkinter.PhotoImage(file = "Frame.png", master = frame)
gambar_label = tkinter.Label(frame, image = gambar)
gambar_label.place(x = 0, y = 0)

def pilih_picture():
    tipe = (('image files', '*.jpg'), ('All files', '*.*'))
    nama = filedialog.askopenfilename(title = 'Open a file', initialdir = '/', filetypes = tipe)
    if nama:
        gambar = Image.open(nama)
        gambar = ImageTk.PhotoImage(gambar)
        gambar = gambar.resize((256,256), Image.ANTIALIAS)
        panel.image = gambar
        panel = tkinter.Label(frame, image = gambar)
        panel.place(x = 338, y = 220)

tekan1 = tkinter.Button(frame, text = "Choose Dataset", font=("Times New Roman", 12), command = pilih_folder )
tekan1.place(x = 46, y = 235, relx = 0.01, rely = 0.01)
tekan2 = tkinter.Button(frame, text = "Choose Image", font=("Times New Roman", 12), command = pilih_picture)
tekan2.place(x = 46, y = 349, relx = 0.01, rely = 0.01)
label1 = tkinter.Label(frame, text = "Result", font = ("Times New Roman", 15))
label1.place(x = 70, y = 469)
label2 = tkinter.Label(frame, text = "Time", font = ("Times New Roman", 15))
label2.place(x = 548, y = 522)

frame.mainloop()