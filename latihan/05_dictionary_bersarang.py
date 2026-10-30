
# Latihan 5: Dictionary Bersarang

# Membuat dictionary dengan dictionary di dalamnya
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

# Menampilkan seluruh data mahasiswa
print("Data Seluruh Mahasiswa:")
for nim, data in mahasiswa.items():
    print("NIM:", nim)
    print("Nama:", data["nama"])
    print("Kelas:", data["kelas"])
    print("Nilai:", data["nilai"])
    print()

# Mengakses data mahasiswa tertentu
print("Data Mahasiswa dengan NIM 2225250075:")
print("Nama:", mahasiswa["2225250075"]["nama"])
print("Kelas:", mahasiswa["2225250075"]["kelas"])
print("Nilai:", mahasiswa["2225250075"]["nilai"])

# Menambahkan data mahasiswa baru
mahasiswa["2225250077"] = {
    "nama": "Dina",
    "kelas": "2B",
    "nilai": 88
}

print("\nSetelah menambahkan mahasiswa baru:")
for nim, data in mahasiswa.items():
    print(nim, "-", data["nama"], "-", data["kelas"], "-", data["nilai"])
