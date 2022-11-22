import tkinter
from tkinter import filedialog
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image
from eigen import *
from pict import *
import timeit

frame = tkinter.Tk()
frame.geometry("1067x600")
frame.title("Pengenalan Wajah")
gambar = tkinter.PhotoImage(file = "Frame.png", master = frame)
gambar_label = tkinter.Label(frame, image = gambar)
gambar_label.place(x = 0, y = 0)
start = timeit.default_timer()

def execute_TIME(): 
    global jam
    global menit
    global detik
    global label
    
    stop = timeit.default_timer()
    waktu = stop - start
    menit, detik = divmod(waktu, 60) 
    jam, menit = divmod(menit, 60)
    label = "{:02d}:{:02d}:{:02d}".format(int(jam), int(menit), int(detik))
    execute_time = tkinter.Label(frame, text = label) 
    execute_time.place(x = 548, y = 525) 

def pilih_picture():
    global mins
    global tes_weight
    global tes
    type = (('image files', '*.jpg'), ('All files', '*.*'))
    name = filedialog.askopenfilename( title ='Open a file', initialdir = '/', type = type)

    if name:
        foto = Image.open(name)
        foto = foto.resize((256,256), Image.ANTIALIAS)
        foto = ImageTk.PhotoImage(foto)
        panel = tkinter.Label(frame, image=foto)
        panel.image = foto
        panel.place(x = 320, y=200)

        tes = np.array(open_image(name))                                # Open image               
        selisihface = np.array(abs(tes - mean))                         # Calculate difference between image and mean
        selisihfaces = selisihface.reshape(65536, 1)                    # Reshape difference
        tes_weight = np.array(np.dot(eigen_face, selisihfaces))         # Calculate weight of image
        x = np.array(np.square(weight - tes_weight))                    # Calculate difference between weight of image and weight of dataset        
        y = np.sum(x, axis=0)                                           # Sum of difference
        euclidean_distance = np.sqrt(y)                                 # euclidean distance
        mins = min(euclidean_distance)                                  # minimum euclidean distance
        percent_result = (mins/Normalize(tes_weight))*100               # Calculate percentage of result
        res = tkinter.Label(frame, text=percent_result)                 # Show percentage of result
        res.place(x=70, y=469)                                          # Show percentage of result
        if (mins < 0.5):                                                # If minimum euclidean distance < 0.5 
            for i in range (len(euclidean_distance)): 
                if euclidean_distance[i] == mins:
                    hasil = i+1
            for i in range(len(matrix)):
                if i == hasil-1:
                    foto = matrix[i].reshape(256,256)
                    foto = Image.fromarray(foto)
                    foto = foto.resize((256,256), Image.ANTIALIAS)
                    foto = ImageTk.PhotoImage(foto)
                    panel = tkinter.Label(frame, image=foto)
                    panel.image = foto
                    panel.place(x=727, y=200) 
                    execute_TIME()  
        else:
            showinfo("Hasil", "Coba Lagi")                             # If minimum euclidean distance > 0.5

def pilih_folder():
    global mean
    global eigen_face
    global weight
    global matrix
    dipilih = filedialog.askdirectory()
    
    if dipilih:
        matrix = np.array(open_folder(".\dataset"))
        H = np.transpose(matrix)
        mean = np.mean(matrix, axis=0)                                  # Calculate mean of dataset
        selisih = np.array(abs(matrix - mean))                          # Calculate difference between dataset and mean
        trans = np.transpose(selisih)
        covarian = np.array(np.dot(selisih, trans))                     # Calculate covariance of dataset
        covarian = covarian / len(covarian)
        vektor_eigen = np.array(eigen_Vec(covarian))                    # Calculate eigen vector of covariance

        for i in range(len(vektor_eigen)):
            norm = Normalize(vektor_eigen[i])
            vektor_eigen[i] = vektor_eigen[i]/norm

        eigen_face = np.array(np.dot(vektor_eigen.T, selisih))      
        weight = np.array(np.dot(eigen_face, selisih.T))
        showinfo("Berhasil", dipilih)                            # Show folder selected

tekan1 = tkinter.Button(frame, text = "Choose Dataset", font=("Times New Roman", 12), command = pilih_folder )
tekan1.place(x = 46, y = 235, relx = 0.01, rely = 0.01)
tekan2 = tkinter.Button(frame, text = "Choose Image", font=("Times New Roman", 12), command = pilih_picture)
tekan2.place(x = 46, y = 349, relx = 0.01, rely = 0.01)

frame.mainloop()