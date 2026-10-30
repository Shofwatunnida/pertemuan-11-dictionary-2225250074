
# Praktik: Pengelolaan Data Mahasiswa dengan Dictionary

# Dictionary untuk menyimpan data mahasiswa
mahasiswa = {
    "A001": {
        "nama": "Andi",
        "kelas": "2A",
        "nilai": 85
    },
    "A002": {
        "nama": "Budi",
        "kelas": "2A",
        "nilai": 78
    },
    "A003": {
        "nama": "Citra",
        "kelas": "2B",
        "nilai": 90
    },
    "A004": {
        "nama": "Dina",
        "kelas": "2B",
        "nilai": 88
    },
    "A005": {
        "nama": "Eka",
        "kelas": "2A",
        "nilai": 80
    }
}


# Fungsi untuk mencari mahasiswa berdasarkan NIM
def cari_mahasiswa(data, nim):
    return data.get(nim)


# Fungsi untuk menghitung rata-rata nilai
def rata_rata_nilai(data):
    if not data:
        return 0

    total = 0

    for nim, mahasiswa in data.items():
        total += mahasiswa["nilai"]

    return total / len(data)


# Fungsi untuk menampilkan seluruh data mahasiswa
def tampilkan_mahasiswa(data):
    print("\nDaftar Data Mahasiswa:")

    for nim, mahasiswa in data.items():
        print("NIM:", nim)
        print("Nama:", mahasiswa["nama"])
        print("Kelas:", mahasiswa["kelas"])
        print("Nilai:", mahasiswa["nilai"])
        print("-" * 30)


# 1. Mencari mahasiswa berdasarkan NIM
print("=== PENCARIAN MAHASISWA ===")
nim_dicari = input("Masukkan NIM yang dicari: ")

hasil = cari_mahasiswa(mahasiswa, nim_dicari)

if hasil:
    print("Nama:", hasil["nama"])
    print("Kelas:", hasil["kelas"])
    print("Nilai:", hasil["nilai"])
else:
    print("Mahasiswa dengan NIM tersebut tidak ditemukan.")


# 2. Menambahkan mahasiswa baru
print("\n=== TAMBAH MAHASISWA ===")
nim_baru = input("Masukkan NIM mahasiswa baru: ")

if nim_baru in mahasiswa:
    print("NIM sudah terdaftar. Data tidak ditambahkan.")
else:
    nama_baru = input("Masukkan nama: ")
    kelas_baru = input("Masukkan kelas: ")
    nilai_baru = float(input("Masukkan nilai: "))

    mahasiswa[nim_baru] = {
        "nama": nama_baru,
        "kelas": kelas_baru,
        "nilai": nilai_baru
    }

    print("Data mahasiswa berhasil ditambahkan.")


# 3. Memperbarui nilai mahasiswa
print("\n=== PERBARUI NILAI ===")
nim_update = input("Masukkan NIM mahasiswa yang nilainya ingin diubah: ")

if nim_update in mahasiswa:
    nilai_baru = float(input("Masukkan nilai baru: "))
    mahasiswa[nim_update]["nilai"] = nilai_baru
    print("Nilai mahasiswa berhasil diperbarui.")
else:
    print("Mahasiswa tidak ditemukan. Nilai tidak diperbarui.")


# 4. Menampilkan seluruh data mahasiswa
print("\n=== SELURUH DATA MAHASISWA ===")
tampilkan_mahasiswa(mahasiswa)


# 5. Menghitung rata-rata nilai mahasiswa
print("\n=== RATA-RATA NILAI ===")
rata_rata = rata_rata_nilai(mahasiswa)
print(f"Rata-rata nilai mahasiswa: {rata_rata:.2f}")
