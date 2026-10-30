 # Latihan 2: Akses Dictionary dengan get()

# Membuat dictionary data mahasiswa
mahasiswa = {
	"nim": "2225250074",
	"nama": "Shofwatunnida",
	"kelas": "2A",
	"nilai": 90
}

# Mengakses data menggunakan get()
print("Nama:", mahasiswa.get("nama"))
print("Nilai:", mahasiswa.get("nilai"))

# Mengakses key yang tidak tersedia
print("Jurusan:", mahasiswa.get("jurusan"))

# Mengakses key yang tidak tersedia dengan nilai default
print("Jurusan:", mahasiswa.get("jurusan", "Belum tersedia"))
