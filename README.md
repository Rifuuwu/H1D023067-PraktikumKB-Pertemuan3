# Password Manager With Base64 Encoding

## 📌 Deskripsi
Password Manager sederhana dengan enkripsi Base64 dan password generator
**For educational purposes only!!!**
**Catatan**
Base64 bukan metode enkripsi yang aman, hanya untuk menyembunyikan teks. 

---

## 🚀 Fitur
- **Generate Password** → Membuat password acak dengan panjang yang ditentukan pengguna.
- **Simpan Password** → Mengenkripsi password dengan Base64 dan menyimpannya ke file JSON.
- **Ambil Password** → Menampilkan password yang telah tersimpan.

---

## 🛠 Instalasi dan Penggunaan
1. **Clone repository:**
   ```bash
   git clone https://github.com/username/password-manager.git
   cd password-manager
   ```

2. **Jalankan program:**
   ```bash
   python password_manager.py
   ```

---

## 📖 Cara Penggunaan
1. **Pilih opsi di menu utama:**
   - `1` → Generate password acak.
   - `2` → Simpan password untuk akun tertentu.
   - `3` → Ambil password berdasarkan nama akun.
   - `4` → Keluar dari program.

2. **Format JSON yang digunakan untuk menyimpan password:**
   ```json
   {
       "gmail.com": "dXNyX3Bhc3N3b3JkMTIz",
       "facebook.com": "ZkFiM2NyX1Bhc3N3MHJkIQ=="
   }
   ```

3. **Password dapat diambil dan didekode menggunakan Base64.**

---

## 📌 Contoh Output
```
Simple Password Manager
1. Buat Password
2. Simpan Password
3. Ambil Password
4. Keluar
Pilih opsi (1-4):
```

---

## 🔐 Catatan Keamanan
- Base64 **bukan metode enkripsi**, hanya encoding.
- Untuk keamanan lebih baik, pertimbangkan enkripsi AES atau hashing.
- Jangan membagikan file JSON secara publik jika berisi data penting.

---


