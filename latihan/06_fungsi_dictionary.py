
# Latihan 6: Fungsi Dictionary

# Membuat dictionary data mahasiswa
mahasiswa = {
    "2225250074": {
        "nama": "Shofwatunnida",
        "kelas": "2A",
        "nilai": 90
    },
    "2225250075": {
        "nama": "Alya",
        "kelas": "2A",
        "nilai": 85
    },
    "2225250076": {
        "nama": "Citra",
        "kelas": "2B",
        "nilai": 95
    },
    "2225250077": {
        "nama": "Dina",
        "kelas": "2B",
        "nilai": 88
    }
}

# Fungsi untuk mencari mahasiswa berdasarkan NIM
def cari_mahasiswa(data, nim):
    return data.get(nim)

# Fungsi untuk menghitung rata-rata nilai mahasiswa
def rata_rata_nilai(data):
    if not data:
        return 0

    total = 0

    for mahasiswa in data.values():
        total += mahasiswa["nilai"]

    return total / len(data)

# Mencari mahasiswa
nim_dicari = "2225250075"
hasil = cari_mahasiswa(mahasiswa, nim_dicari)

print("Pencarian Mahasiswa:")
if hasil:
    print("NIM:", nim_dicari)
    print("Nama:", hasil["nama"])
    print("Kelas:", hasil["kelas"])
    print("Nilai:", hasil["nilai"])
else:
    print("Mahasiswa tidak ditemukan.")

# Menghitung rata-rata nilai
rata_rata = rata_rata_nilai(mahasiswa)
print("\nRata-rata nilai mahasiswa:", rata_rata)
