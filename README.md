# Pertemuan 11 — Dictionary

## Identitas

- **Nama:** Shofwatunnida
- **NIM:** 2225250074
- **Kelas:** 3A

## Tujuan

1. Memahami konsep dictionary dalam Python.
2. Mengakses data menggunakan key dan method `get()`.
3. Menambahkan, mengubah, dan menghapus data dictionary.
4. Melakukan iterasi menggunakan `keys()`, `values()`, dan `items()`.
5. Menggunakan nested dictionary dan fungsi untuk mengelola data.

## Struktur Data

Program utama menggunakan dictionary bersarang (*nested dictionary*). NIM digunakan sebagai key, sedangkan value berupa dictionary yang menyimpan nama, kelas, dan nilai mahasiswa.

## Struktur Folder

```text
pertemuan-11-dictionary-2225250074/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_dasar_dictionary.py
│   ├── 02_akses_get.py
│   ├── 03_manipulasi_dictionary.py
│   ├── 04_iterasi_dictionary.py
│   ├── 05_dictionary_bersarang.py
│   └── 06_fungsi_dictionary.py
└── praktik/
	└── data_mahasiswa.py
```

## Cara Menjalankan

Jalankan program utama melalui terminal dari folder utama proyek:

```bash
python praktik/data_mahasiswa.py
```

## Pengujian Program

| No. | Pengujian | Hasil yang Diharapkan |
|---:|---|---|
| 1 | Mencari NIM A003 | Data Citra ditemukan. |
| 2 | Mencari NIM A999 | Pesan bahwa mahasiswa tidak ditemukan ditampilkan. |
| 3 | Memperbarui nilai A002 | Nilai berubah menjadi 82. |
| 4 | Menambahkan mahasiswa A006 | Data mahasiswa baru ditambahkan. |
| 5 | Menampilkan seluruh data | Semua data ditampilkan menggunakan `items()`. |
| 6 | Menghitung rata-rata | Rata-rata nilai ditampilkan dengan dua angka desimal. |

## Refleksi

Melalui praktikum ini, saya memahami bahwa dictionary menyimpan data dalam pasangan key dan value. Dictionary memudahkan proses pencarian, penambahan, perubahan, dan penghapusan data. Saya juga belajar menggunakan nested dictionary, melakukan iterasi dengan `items()`, serta membuat fungsi untuk mencari mahasiswa dan menghitung rata-rata nilai.
