import tkinter as tk
import sqlite3
from tkinter import messagebox

def simpan_data_ke_sqlite(Nama, Biologi, Fisika, Inggris):
# Membuka atau membuat database SQLite
    Prediksi = predik(nama=Nama, bio=Biologi, fisik=Fisika, ing=Inggris)
    conn = sqlite3.connect("namasiswa.db")
    cursor = conn.cursor()

    # Membuat tabel jika belum ada
    cursor.execute('''CREATE TABLE IF NOT EXISTS Nilai_Siswa (Nama TEXT,Biologi INTEGER, Fisika INTEGER,Inggris INTEGER,Hasil_Prediksi TEXT)''')
    # Memasukkan data mata pelajaran ke dalam tabel
    cursor.execute("INSERT INTO Nilai_Siswa (Nama, Biologi, Fisika, Inggris, Hasil_Prediksi) VALUES (?, ?, ?, ?, ?)",
    (Nama, Biologi, Fisika, Inggris, Prediksi))
    # Melakukan commit dan menutup koneksi
    conn.commit()
    conn.close()

def predik(nama, bio, fisik, ing):
    nilai_bagus = max(bio,fisik,ing)

    if nilai_bagus == bio:
        return "Kedokteran"
    elif nilai_bagus == fisik:
        return "Teknik"
    elif nilai_bagus == ing:
        return "Bahasa"

top = tk.Tk()
top.title("Pemrograman Kelas B")
top.geometry("400x400")
top.resizable(False, False)

inputframe=tk.LabelFrame(top)
inputframe.pack(padx=10, pady=10, fill="x", expand=True)

#Bikin Label Untuk Judul
var = tk.Label(inputframe, text="Aplikasi Prediksi Prodi Pilihan")
var.pack()
#Bikin Input 1
Input=tk.Label(inputframe, text="Masukan Nama: " )
Input.pack(padx=10, pady=5,fill="x", expand=True)
e1=tk.Entry(inputframe)
e1.pack(padx=10, pady=5,fill="x", expand=True)

#Bikin Input 2
Input2=tk.Label(inputframe, text="Masukan Nilai Biologi: " )
Input2.pack(padx=10, pady=5,fill="x", expand=True)
e2=tk.Entry(inputframe)
e2.pack(padx=10, pady=5,fill="x", expand=True)

#Bikin Input 3
Input3=tk.Label(inputframe, text="Masukan Nilai Fisika: " )
Input3.pack(padx=10, pady=5,fill="x", expand=True)
e3=tk.Entry(inputframe)
e3.pack(padx=10, pady=5,fill="x", expand=True)

#Bikin Input 4
Input4=tk.Label(inputframe, text="Masukan Nilai Bahasa Inggris: " )
Input4.pack(padx=10, pady=5,fill="x", expand=True)
e4=tk.Entry(inputframe)
e4.pack(padx=10, pady=5,fill="x", expand=True)

#Bikin Button
def onClickBut():
    Nama=e1.get()
    Biologi=e2.get()
    Fisika=e3.get()
    Inggris=e4.get()
    simpan_data_ke_sqlite(Nama, Biologi, Fisika, Inggris)
    messagebox.showinfo("Keterangan","Kamu Cocok Masuk Fakultas " + 
    predik(nama=Nama, bio=Biologi, fisik=Fisika, ing=Inggris) )
    

tombol=tk.Button(inputframe, text="Submit", command=onClickBut)
tombol.pack(padx=10, pady=5,fill="x", expand=True)



top.mainloop()
