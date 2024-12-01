import tkinter as tk

def hitung():
    try:
        panjang = float(entry_panjang.get())
        lebar = float(entry_lebar.get())
        
        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)
        
        text_output.delete(1.0, tk.END) # Menghapus isi Text Widget
        text_output.insert(tk.END, f"Luas Persegi Panjang: {luas}\n")
        text_output.insert(tk.END, f"Keliling Persegi Panjang: {keliling}\n")
    except ValueError:
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, "Input tidak valid. Harap masukkan angka.")

# Membuat jendela utama
root = tk.Tk()
root.title("Hitung Luas atau Keliling Persegi Panjang")

# Label dan Entry untuk panjang
label_panjang = tk.Label(root, text="Masukan Panjang:")
label_panjang.pack()
entry_panjang = tk.Entry(root)
entry_panjang.pack()

# Label dan Entry untuk lebar
label_lebar = tk.Label(root, text="Masukan Lebar:")
label_lebar.pack()
entry_lebar = tk.Entry(root)
entry_lebar.pack()

# Tombol untuk menghitung
button_hitung = tk.Button(root, text="Hitung", command=hitung)
button_hitung.pack()

# Widget Text untuk output
text_output = tk.Text(root, height=5, width=30)
text_output.pack()

# Menjalankan aplikasi
root.mainloop()
