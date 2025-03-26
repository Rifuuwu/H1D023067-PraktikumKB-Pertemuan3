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

## Note Tugas ##
- Sistem kontrol  
Salah satu penerapan sistem kontrol yang digunakan di aplikasi ini adalah if else dan looping pada pemilihan mode
```python
While True:
    if choice == "1":
        ...
    elif choice == "2":
        ...
    elif choice == "3":
        ...
    elif choice == "4":
        ...
        break
    else:
        ...
```
- Struktur data  
Salah satu struktur data Python yang digunakan di aplikasi ini adalah dictionary, yang pada kasus aplikasi ini digunakan untuk menyimpan password pada file JSON
```python
password_terenkripsi = enkripsi_password(password)
data = {}
...
data[account] = password_terenkripsi
```
- Library  
Aplikasi ini menggunakan total 5 library yaitu json, os, random, string dan base64.  
1. Library json pada aplikasi ini digunakan untuk melakukan pengolahan file json seperti membaca isi file json dan menuliskan data baru ke file json.  
```python
# Membaca file JSON (r)
with open(PASSWORD_FILE, "r") as file:
    try:
        data = json.load(file)
    except json.JSONDecodeError:
        return "File password rusak atau kosong!"

# Menulis data baru ke file JSON (w)
with open(PASSWORD_FILE, "w") as file:
    json.dump(data, file, indent=4)
```
2. Library os pada aplikasi ini digunakan untuk mengecek apakah file penyimpanan password sudah ada atau belum.
```python
if not os.path.exists(PASSWORD_FILE):
    return "Tidak ada file password yang tersimpan!"
```
3. Library random pada aplikasi ini digunakan untuk mengacak string disaat proses pembuatan password.  
```python
characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(characters) for _ in range(length))
```
4. Library string pada aplikasi ini digunakan untuk menentukan karakter apa saja yang akan diacak saat pembuatan password.  
```python
characters = string.ascii_letters + string.digits + string.punctuation
password =  "".join(random.choice(characters) for _ in range(length))
```
5. Library base64 pada aplikasi ini digunakan untuk melakukan enkripsi dan dekripsi terhadap password.
```python
# Enkripsi (b64encode)
def enkripsi_password(password):
    return base64.b64encode(password.encode()).decode()
    
# Dekripsi (b64decode)
def dekripsi_password(encoded_password):
    return base64.b64decode(encoded_password.encode()).decode()
```
