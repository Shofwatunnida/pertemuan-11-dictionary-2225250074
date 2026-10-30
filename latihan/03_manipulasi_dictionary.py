
# Latihan 3: Manipulasi Dictionary

# Membuat dictionary data mahasiswa
mahasiswa = {
    "nim": "2225250074",
    "nama": "Shofwatunnida",
    "kelas": "2A",
    "nilai": 90
}

# Menambahkan data baru
mahasiswa["jurusan"] = "Pendidikan Matematika"
print("Setelah menambahkan data:")
print(mahasiswa)

# Mengubah nilai mahasiswa
mahasiswa["nilai"] = 95
print("\nSetelah mengubah nilai:")
print(mahasiswa)

# Menggunakan update() untuk mengubah data
mahasiswa.update({"kelas": "2B"})
print("\nSetelah mengubah kelas:")
print(mahasiswa)

# Menghapus data menggunakan pop()
mahasiswa.pop("jurusan")
print("\nSetelah menghapus jurusan:")
print(mahasiswa)
