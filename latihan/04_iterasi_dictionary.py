
# Latihan 4: Iterasi Dictionary

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
    }
}

# Menampilkan seluruh NIM
print("Daftar NIM:")
for nim in mahasiswa:
    print(nim)

# Menampilkan seluruh nama mahasiswa
print("\nDaftar Nama Mahasiswa:")
for data in mahasiswa.values():
    print(data["nama"])

# Menampilkan NIM dan data mahasiswa menggunakan items()
print("\nData Lengkap Mahasiswa:")
for nim, data in mahasiswa.items():
    print("NIM:", nim)
    print("Nama:", data["nama"])
    print("Kelas:", data["kelas"])
    print("Nilai:", data["nilai"])
    print()
