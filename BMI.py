from tkinter import *
from tkinter import font

#Instance Window
root = Tk()
root.title("BMI Apps")
root.resizable(False, False)

def open_w_alert(message):
    """
    Membuka child window
    """
    w_alert = Toplevel(root)
    w_alert.title("Error")

    nilai_msg = StringVar()
    lbl_msg = Label(w_alert, textvariable=nilai_msg)
    lbl_msg.grid(row=0, column=2)
    nilai_msg.set(message)

    btn_ok = Button(w_alert, text="Ok", command=w_alert.destroy)
    btn_ok.grid(row=1, column=3)

def validate_input():
    """
    memvalidasi seluruh inputan 
    """
    status=False
    if nilai_nama.get()=="":
        open_w_alert("Nama tidak boleh kosong!")
    elif nilai_usia.get()=="":
        open_w_alert("Usia tidak boleh kosong!")
    elif nilai_tinggi.get()=="":
        open_w_alert("Tinggi tidak boleh kosong!")
    elif int(nilai_tinggi.get())<=0:
        open_w_alert("Tinggi harus bernilai lebih dari 0")
    elif nilai_berat.get()=="":
        open_w_alert("Berat tidak boleh kosong!")
    elif int(nilai_berat.get())<=0:
        open_w_alert("Berat harus bernilai lebih dari 0")
    else:
        status=True
    
    return status

def calc_BMI():
    """
    Hitung BMI jika input valid
    """
    if validate_input():
        tinggi_cm = int(nilai_tinggi.get())
        tinggi_m = tinggi_cm/100
        berat = int(nilai_berat.get())
        nilai_BMI = berat/(tinggi_m**2)
        lbl_nilai_hasil["text"] = round(nilai_BMI, 2)

def reset():
    """
    Hapus Semua inputan
    """
    ent_nama.delete(0, 'end')
    ent_usia.delete(0, 'end')
    ent_tinggi.setvar(value=0)
    ent_berat.setvar(value=0)
    lbl_nilai_hasil["text"] = 0



#declare frame
frm_header = Frame(root)
frm_input = Frame(root)
frm_action = Frame(root)
frm_hasil = Frame(root)
frm_footer = Frame(root)

#declare label
lbl_judul = Label(master=frm_header, text="Aplikasi Hitung BMI", font=("Arial", 24, UNDERLINE))

lbl_nama = Label(master=frm_input, text="Nama")
lbl_jk = Label(master=frm_input, text="Jenis Kelamin")
lbl_usia = Label(master=frm_input, text="Usia")
lbl_tahun = Label(master=frm_input, text="Tahun")
lbl_tinggi = Label(master=frm_input, text="Tinggi")
lbl_cm = Label(master=frm_input, text="Cm")
lbl_berat = Label(master=frm_input, text="Berat")
lbl_kg = Label(master=frm_input, text="Kg")

lbl_judul_hasil = Label(master=frm_hasil, text="Hasil Perhitungan", font=("Arial", 12, UNDERLINE))
lbl_nilai_hasil = Label(master=frm_hasil, text="0", font=("Arial",44))
lbl_deskripsi_hasil = Label(master=frm_hasil, text="Normal BMI range\n18.5 - 24.9")

lbl_copyright = Label(master=frm_footer, text="copyright @ 2021 - Ciprun Official")

#declare Radio button
v = StringVar(master=root, value="1")
rd_jk_l = Radiobutton(master=frm_input, text="Laki-laki", variable=v, value="1")
rd_jk_p = Radiobutton(master=frm_input, text="Perempuan", variable=v, value="2")


#declare entry
nilai_nama = StringVar()
nilai_usia = StringVar()
nilai_tinggi = StringVar(value=0)
nilai_berat = StringVar(value=0)

ent_nama = Entry(master=frm_input, textvariable=nilai_nama)
ent_usia = Entry(master=frm_input, textvariable=nilai_usia)
ent_tinggi = Entry(master=frm_input,textvariable=nilai_tinggi, )
ent_berat = Entry(master=frm_input,textvariable=nilai_berat)

#declare button
btn_reset = Button(master=frm_action, text="Reset", command=reset)
btn_submit = Button(master=frm_action, text="Submit", command=calc_BMI)

#set placed frame
frm_header.grid(row=0, columnspan=2, pady=10)
frm_input.grid(row=1, column=0, pady=10)
frm_action.grid(row=2, column=0, pady=10)
frm_hasil.grid(row=1, column=1, rowspan=2, pady=10)
frm_footer.grid(row=3, column=1, pady=10)

#set placed items
lbl_judul.grid(row=0)

lbl_nama.grid(row=0, column=0, sticky=W)
ent_nama.grid(row=0, column=1, columnspan=2, sticky=W+E)

lbl_jk.grid(row=1, column=0, sticky=W)
rd_jk_l.grid(row=1, column=1)
rd_jk_p.grid(row=1, column=2)

lbl_usia.grid(row=2, column=0, sticky=W)
ent_usia.grid(row=2, column=1)
lbl_tahun.grid(row=2, column=2, sticky=W)

lbl_tinggi.grid(row=3, column=0, sticky=W)
ent_tinggi.grid(row=3, column=1)
lbl_cm.grid(row=3, column=2, sticky=W)

lbl_berat.grid(row=4, column=0, sticky=W)
ent_berat.grid(row=4, column=1)
lbl_kg.grid(row=4, column=2, sticky=W)

btn_reset.grid(row=0, column=0)
btn_submit.grid(row=0, column=1)

lbl_judul_hasil.grid(row=0, column=0, sticky=W)
lbl_nilai_hasil.grid(row=1)
lbl_deskripsi_hasil.grid(row=2)

lbl_copyright.grid(row=0, column=1)


#run window
root.mainloop()