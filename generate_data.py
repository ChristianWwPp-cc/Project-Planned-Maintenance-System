import json
import random

# Daftar Peralatan dan Kode Fiktif
peralatan = [
    ("Main Engine Oil Filter", "ME-FO-01"),
    ("Auxiliary Engine 1 Cooling Pump", "AE1-CP-05"),
    ("Bilge Pump Motor", "BP-MOT-11"),
    ("Steering Gear Hydraulic Check", "SG-HYD-03"),
    ("Compressor Air Filter", "COM-AF-07"),
    ("Generator 2 Fuel Injectors", "GEN2-FI-04"),
    ("Fire Pump Sea Suction Valve", "FP-SSV-10"),
    ("Separator Oil Discharge Valve", "SEP-ODV-09"),
    ("Windlass Brake Inspection", "WIND-BI-02")
]

# Daftar Status Awal
status_list = ["Belum Selesai", "Sedang Dikerjakan", "Selesai"]
kategori_list = ["Harian", "Mingguan", "Bulanan"]

pms_tasks = []
task_id_counter = 1

# Generate 40 tugas fiktif
for i in range(40):
    nama_alat, kode_alat = random.choice(peralatan)
    
    # Randomisasi data
    status_awal = random.choices(status_list, weights=[60, 20, 20], k=1)[0]
    kategori_tugas = random.choice(kategori_list)
    
    task = {
        "id": task_id_counter,
        "nama": f"Cek Rutin {nama_alat}",
        "kode": kode_alat,
        "status": status_awal,
        "kategori": kategori_tugas,
        "frekuensi": f"Dilakukan {kategori_tugas}"
    }
    pms_tasks.append(task)
    task_id_counter += 1

# Simpan hasil ke file JSON
with open('pms_data_initial.json', 'w') as f:
    json.dump(pms_tasks, f, indent=4)

print("Data 40 tugas pemeliharaan kapal berhasil dibuat di pms_data_initial.json")
