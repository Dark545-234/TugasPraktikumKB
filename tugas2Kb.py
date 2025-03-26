import random
import datetime

# membuat data kelas yang tesedia
kelas = {
    "1": "Praktikum Kecerdasan Buatan",
    "2": "Praktikum Jaringan Komputer",
    "3": "Rebahan"
}

def tampilkan_kelas():
    """Menampilkan daftar kelas yang tersedia."""
    print("\nDaftar Kelas:")
    for key, name in kelas.items():
        print(f"{key}. {name}")

def pendaftaran_mahasiswa():
    """Memproses pendaftaran mahasiswa ke dalam kelas yang dipilih."""
    # Menampilkan daftar kelas
    tampilkan_kelas()  
    
    # Meminta input dari pengguna
    pilihan = input("Pilih nomor kelas: ")  
    
    # Validasi pilihan kelas
    if pilihan not in kelas:
        print("Pilihan tidak valid!")
        return
    
    # Meminta input nama mahasiswa
    nama_mahasiswa = input("Masukkan nama mahasiswa: ")  
    # Membuat ID mahasiswa secara acak
    NIM = random.randint(1000, 9999)  
    # Mendapatkan waktu saat ini
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
    
    # Menampilkan hasil pendaftaran
    print("\nPendaftaran Berhasil!")
    print(f"Nomor Induk Mahasiswa: {NIM}")
    print(f"Nama: {nama_mahasiswa}")
    print(f"Kelas: {kelas[pilihan]}")
    print(f"Waktu Pendaftaran: {waktu}")

def main():
    """Fungsi utama yang menjalankan program dalam loop sampai pengguna keluar."""
    while True:
        print("\nSistem Pendaftaran Mahasiswa")
        print("1. Lihat daftar kelas")
        print("2. Daftar mahasiswa ke kelas")
        print("3. Keluar")
        # Meminta input menu dari pengguna
        pilihan = input("Pilih menu: ") 
        
        if pilihan == "1":
            # Menampilkan daftar kelas
            tampilkan_kelas()  
        elif pilihan == "2":
            # Memproses pendaftaran mahasiswa
            pendaftaran_mahasiswa()  
        elif pilihan == "3":
            print("Terima kasih!")
            # Keluar dari loop
            break  
        else:
            # Menampilkan pesan jika input tidak sesuai
            print("Pilihan tidak valid!")  

# Menjalankan program jika file dijalankan secara langsung
if __name__ == "__main__":
    main()
