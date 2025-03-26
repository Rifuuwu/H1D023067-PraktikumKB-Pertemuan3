import json
import os
import random
import string
import base64

PASSWORD_FILE = "passwords.json"

# Fungsi untuk generate password
def buat_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))

# Fungsi untuk mengenkripsi password dengan Base64
def enkripsi_password(password):
    return base64.b64encode(password.encode()).decode()

# Fungsi untuk mendekripsi password dari Base64
def dekripsi_password(encoded_password):
    return base64.b64decode(encoded_password.encode()).decode()

# Fungsi untuk menyimpan password ke JSON
def simpan_password(account, password):
    password_terenkripsi = enkripsi_password(password)
    data = {}

    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {}

    data[account] = password_terenkripsi

    with open(PASSWORD_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Password untuk '{account}' berhasil disimpan!")

# Fungsi untuk mengambil password
def ambil_password(account):
    if not os.path.exists(PASSWORD_FILE):
        return "Tidak ada file password yang tersimpan!"

    with open(PASSWORD_FILE, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            return "File password rusak atau kosong!"

    if account in data:
        return dekripsi_password(data[account])
    else:
        return "Akun tidak ditemukan!"

# Menu utama
def main():
    while True:
        print("\nSimple Password Manager")
        print("1. Buat Password")
        print("2. Simpan Password")
        print("3. Ambil Password")
        print("4. Keluar")

        choice = input("Pilih opsi (1-4): ")

        if choice == "1":
            length = int(input("Masukkan panjang password: "))
            password = buat_password(length)
            print(f"Password yang dihasilkan: {password}")

        elif choice == "2":
            account = input("Masukkan nama akun/website: ")
            password = input("Masukkan password: ")
            simpan_password(account, password)

        elif choice == "3":
            account = input("Masukkan nama akun/website: ")
            print(f"Password: {ambil_password(account)}")

        elif choice == "4":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()

