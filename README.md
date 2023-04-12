# Tugas Kecil 3 -- IF2211 - Strategi Algoritma
<h2 align="center">
  Shortest Path Finder With UCS and A* Algorithm <br/>
</h2>
<hr>

## Table of Contents
1. [General Info](#general-information)
2. [Creator Info](#creator-information)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
5. [Setup](#setup)
6. [Usage](#usage)
7. [Screenshots](#screenshots)
7. [Structure](#structure)
8. [Project Status](#project-status)
9. [Room for Improvement](#room-for-improvement)
10. [Acknowledgements](#acknowledgements)

<a name="general-information"></a>

## General Information
**Shortest Path Finder** merupakan program yang berguna menentukan lintasan terpendek berdasarkan matriks ketetanggaan yang merepresentasikan graf berbobot. Matriks ketetanggan dapat diperoleh dengan dua cara, yaitu memasukkan input berupa sebuah file yang berisi matriks ketetanggaan antar simpul beserta namanya atau memasukkan koordinat peta yang akan diubah menjadi graf dan matriks ketetanggaan. Jika memilih menggunakan input file, pengguna akan diminta memilih start node dan end node. Jika memilih menggunakan koordinat peta, pengguna akan diminta memasukkan koordinat start point dan destination point. Program akan memanggil algoritma UCS dan A* untuk mencari shortest path, menampilkan informasi terkait hasil algoritma, dan membuat visualisasi graf atau peta beserta shortest path yang dihasilkan.

<a name="creator-information"></a>

## Creator Information

| Nama                        | NIM      | E-Mail                      |
| --------------------------- | -------- | --------------------------- |
| Ahmad Ghulam Ilham          | 13521118 | 13521118@std.stei.itb.ac.id |
| Muhammad Naufal Nalendra    | 13521152 | 13521152@std.stei.itb.ac.id |

<a name="features"></a>

## Features
- Pengguna dapat memilih metode input (`file` atau `koordinat peta`) program
- Pengguna dapat memilih `start node` dan `end node`  (metode `input file`)
- Pengguna dapat memasukkan koordinat `start point` dan `destination point` (metode `input koordinat peta`)
- Pengguna dapat melihat informasi mengenai `jarak`, `iterasi`, dan `waktu` yang dihasilkan
- Pengguna dapat melihat `graph` atau `peta` beserta `shortest path` yang dihasilkan

<a name="technologies-used"></a>

## Technologies Used
- Python 3.11
- Python Standard Library
- OpenStreetMap API
- Matplotlib
- NetworkX
- Folium
> Note: The version of the libraries above is the version that we used in this project. You can use the latest version of the libraries.

<a name="setup"></a>

## Setup
1. Install [Python](https://www.python.org/downloads/)
2. Install [osmnx](https://pypi.org/project/osmnx/) melalui command prompt:
```bash
pip install osmnx
```
3. Install [matplotlib](https://pypi.org/project/matplotlib/) melalui command prompt:
```bash
pip install matplotlib
```
4. Install [networkx](https://pypi.org/project/networkx/) melalui command prompt:
```bash
pip install networkx
```
5. Install [folium](https://pypi.org/project/folium/) melalui command prompt:
```bash
pip install folium
```

<a name="usage"></a>

## Usage

#### WINDOWS (VS Code)
> Note: Untuk menjalankan program ini, pastikan anda telah memiliki semua requirements yang dibutuhkan
1. Clone repository [ini](https://github.com/Agilham/Tucil3_13521118_13521152.git) ke dalam direktori lokal Anda, dengan cara:
```bash
git clone https://github.com/Agilham/Tucil3_13521118_13521152.git
```
2. Masuk ke dalam direktori `Tucil3_13521118_13521152` yang telah Anda clone, dengan cara:
```bash
cd Tucil3_13521118_13521152
```
3. Buat terminal baru pada VSCode
4. Masukkan perintah berikut:
```bash
python src/program.py
```
5. Ikuti petunjuk input yang diberikan program. Pastikan semua input yang dimasukkan valid
6. Informasi hasil algoritma (`jarak, iterasi, waktu`) akan ditampilkan pada terminal
7. Visualisasi graf (metode `input file`) beserta `shortest path` akan muncul sebagai pop up. Selama pop up graf belum ditutup, program akan berhenti berjalan. Pastikan untuk menutup pop up graf agar program kembali berjalan
8. Visualisasi peta (metode `input koordinat peta`) akan disimpan sebagai file ekstensi `.html` pada folder `test`. Buka file tersebut pada browser untuk melihat peta dan `shortest path` yang dihasilkan 

<a name="screenshots"></a>

## Screenshots
  Contoh Menggunakan File Matriks Ketetanggaan
  ![Image description](/img/SS1.png)
  Contoh Hasil Berdasarkan Input File
  ![Image description](/img/SS2.png)
  Contoh Menggunakan Koordinat Peta
  ![Image description](/img/SS3.png)
  Contoh Hasil Berdasarkan Input Koordinat
  ![Image description](/img/SS4.png)

<a name="structure"></a>

## Structure
```bash
.
├── README.md
├── doc
├── img
│   ├── SS1.png
│   ├── SS2.png
│   ├── SS3.png
│   └── SS4.png
├── src
│   ├── lib
│   │   ├── astar.py
│   │   ├── input.py
│   │   ├── output.py
│   │   ├── prioitem.py
│   │   └── ucs.py
│   └── program.py
└── test
    ├── graph1.txt
    ├── graph2.txt
    └── graph3.txt
```

<a name="project-status">

## Project Status
Project is: _Completed_

<a name="room-for-improvement">

## Room for Improvement
- Menambahkan GUI.

<a name="acknowledgements">

## Acknowledgements
- Thanks To Allah SWT and His guidance, we were able to design this project without any meaningful hurdle

<hr>
