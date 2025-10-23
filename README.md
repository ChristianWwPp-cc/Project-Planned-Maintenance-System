# ⚓ Dashboard PMS Kapal Sederhana

##  Deskripsi Proyek
Dashboard web statis yang mensimulasikan **Sistem Manajemen Pemeliharaan Terencana (PMS)** untuk peralatan kapal. Proyek ini bertujuan memberikan solusi digital untuk **efisiensi kerja** dengan memvisualisasikan, memfilter, dan memperbarui status tugas pemeliharaan harian, mingguan, dan bulanan.

---

##  Teknologi yang Digunakan

* **Front-End:** HTML5, CSS3, JavaScript.
* **Penyimpanan Data:** **JavaScript Local Storage** (untuk menyimpan status tugas secara persisten).
* **Koding Efisien:** **Python 3** (untuk *data generation*).
* **Desain:** Custom CSS (menggunakan Flexbox/Grid untuk *layout* responsif dan desain maritim).

---

##  Bukti Koding Efisien & Solusi Digital

Proyek ini memenuhi kriteria pelatihan melalui praktik koding yang optimal:

### 1. Koding Efisien (Python)
* **File:** `generate_data.py`
* **Tujuan:** Script Python digunakan untuk menghasilkan **40 *item* tugas pemeliharaan fiktif** ke dalam format JSON. Penggunaan **List** dan **Looping** dalam Python menggantikan input data manual yang memakan waktu (Koding yang Tidak Efisien).

### 2. Solusi Digital (Manajemen Data Persisten)
* **Teknik:** Implementasi fungsi `loadTasks()` dan `saveTasks()` yang terintegrasi dengan **Local Storage**.
* **Hasil:** Status tugas yang diubah pengguna (**Belum Selesai** -> **Selesai**) akan tetap tersimpan dan termuat kembali dengan status terakhir meskipun *browser* di-*refresh* atau ditutup.

---

##  Cara Menjalankan Aplikasi

1.  **Kloning Repositori:** Unduh atau *clone* seluruh repositori ini.
2.  **Buka Website:** Buka file **`index.html`** menggunakan Live Server (disarankan) atau langsung di *browser* Anda.
3.  **Uji Coba:** Ubah status tugas menggunakan tombol **Selesaikan** atau **Mulai** dan perhatikan bahwa status tetap tersimpan.

### Tautan Proyek (GitHub Pages)

[**
https://christianwwpp-cc.github.io/Project-Planned-Maintenance-System
**]

---

## Kontribusi Tim

| Nama Siswa | Peran Utama |
| :--- | :--- |
| **[Nama Christian Wahyu Prakoso]** | Web Design (CSS Estetika & Responsif), Finalisasi HTML. |
| **[Nama Bilqi Alviansyah]** | Logika Data (Python `generate_data.py`), Logika Fungsional JavaScript (Local Storage & Filter). |

---

