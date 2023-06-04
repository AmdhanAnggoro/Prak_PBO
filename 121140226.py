import tkinter as tk

def submit_form():
    # Fungsi ini akan dieksekusi saat tombol 'Submit' ditekan
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    
    # Proses pengiriman data atau tindakan lainnya bisa ditambahkan di sini
    
    # Contoh menampilkan data yang diisi ke dalam label
    result_label.config(text=f"Nama: {name}\nEmail: {email}\nUsia: {age}")

# Membuat instance objek Tkinter
window = tk.Tk()
window.title("Form")

# Membuat label untuk Nama
name_label = tk.Label(window, text="Nama:")
name_label.pack()

# Membuat entry (input) untuk Nama
name_entry = tk.Entry(window)
name_entry.pack()

# Membuat label untuk Email
email_label = tk.Label(window, text="Email:")
email_label.pack()

# Membuat entry (input) untuk Email
email_entry = tk.Entry(window)
email_entry.pack()

# Membuat label untuk Usia
age_label = tk.Label(window, text="Usia:")
age_label.pack()

# Membuat entry (input) untuk Usia
age_entry = tk.Entry(window)
age_entry.pack()

# Membuat tombol Submit
submit_button = tk.Button(window, text="Submit", command=submit_form)
submit_button.pack()

# Membuat label untuk menampilkan hasil
result_label = tk.Label(window, text="")
result_label.pack()

# Memulai event loop
window.mainloop()