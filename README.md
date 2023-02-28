# Tugas kecil 2 Strategi Algoritma

## Closest Pair

Dibuat oleh Bintang Hijriawan Jachja - 13521003 dalam rangka penyelesaian tugas Strategi Algoritma IF2211

## Deskripsi Permasalahan

Closest pair atau pasangan terdekat adalah suatu permasalahan yang mengharuskan kita mencari pasangan terdekat dari sekumpulan objek. Pada tugas kali ini, permasalahan yang harus diselesaikan adalah mencari pasangan titik dengan jarak terdekat di bidang 3 dimensi dan bidang n dimensi sebagai bonus persoalan.

Projek ini adalah membuat suatu algoritma dengan pendekatan *Divide and Conquer* untuk menyelesaikan permasalahan closest pair.

## Algoritma yang digunakan

Pencarian closest dilakukan dengan pendekatan *divide and conquer*. Algoritma yang dijalankan adalah sebagai berikut:

- misalkan ada sekumpulan titik terurut terhadap sumbu x sebanyak N di bidang D dimensi.
- Hitung jarak terdekat dari titik yang ada di bagian kiri dan titik yang ada dibagian kanan. Simpan nilai terkecil sebagai jarak terdekat.
    - jika N > 2, maka kumpulan titik dibagi menjadi 2 bagian sama rata. Jika N ganjil, bagian pertama akan lebih sedikit 1 titik dibanding bagian kedua. Kedua bagian akan dikenakan algoritma divide and conquer hingga menghasilkan jarak terdekat di masing-masing bagian.
    - jika N == 2, maka akan dicari jarak kedua titik tersebut, dan di kembalikan sebagai pasangan terdekat pada bagian tersebut.
    - jika N == 1, maka akan dikembalikan nilai infinity karena tidak ada pasangan titik pada bagian tersebut.
    - tidak ada kasus N < 1, sehingga tidak perlu di handle.
- Jika kumpulan titik dibagi 2, cari titik tengah sumbu x antara titik yang ada di perbatasan, simpan nilainya sebagai titik tengah.
- untuk setiap titik pada bagian pertama dengan posisi terhadap sumbu x > (titik tengah - jarak terdekat) dan setiap titik pada bagian kedua dengan posisi terhadap sumbu x < (titik tengah + jarak terdekat).
- cari jarak antara kedua titik, bandingkan dengan jarak terdekat sebelumnya, ambil yang terkecil.
- kembalikan jarak terdekat yang baru sebagai jarak terdekat pada himpunan titik.


## Menjalankan Program

Untuk menjalankan program, pada *root directory*, jalankan run.bat (pada *windows*):
```
./run.bat
```
Program akan menjalankan *main.py*