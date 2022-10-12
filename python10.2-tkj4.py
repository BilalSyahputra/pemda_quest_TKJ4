# Membuat Tipe data koleksi

koleksi_data_str = ["pisang" , "Mangga" , "Jambu" , "Semangka"]

koleksi_data_int = [200, 300, 400, 500]

koleksi_data_mix = ["Rizky Billar", 100, True, "Reza Arap"]

print("Koleksi data Stirng:", koleksi_data_str)
print("Koleksi data Integer:", koleksi_data_int)
print("Koleksi data Campuran:", koleksi_data_mix)

# Buatlah 3 kumpulan data: Nama Hewan, NIlai UTS, Nama Teman sebangku kalian

nama_hewan = ["Burung" , "Ikan" , "Beruang", "Kucing",]

nilai_uts = [100, 90, 80]

nama_teman = ["Dimas", "isal", "Rivai", "Untung",]

print("nama hewan", nama_hewan)
print("nilai uts", nilai_uts)
print("nama teman",  nama_teman)

# Tampilkan data koleksi dengan indeks

print("nama teman data ke-3:", nama_teman[2])

# Data ke 2 hewan 

print("nama hewan data ke-2:", nama_hewan[1])

# Data pertama Nilai UTS

print("nilai uts data ke-1:", nilai_uts[0])

# Data ke terakhir teman sebangku

print("nama teman data terakhir", nama_teman[3])

print(nama_teman)

print(nama_teman[1:2])

nama_teman[3] ="Lesti kejora"

print(nama_teman)


nama_teman.append("Kureiji Ollie")

print(nama_teman)

# Tambahkan 1 data disetiap data koleksi

nama_teman.append("Fadli")
nama_hewan.append("harimau")
nilai_uts.append ("200")

print(nama_teman)
print(nama_hewan)
print(nilai_uts)

# Ubahlah data Terakhir Nilai UTS

nilai_uts[2] =100

print(nilai_uts)

# ubahlah data ke-3 nama hewan

nama_hewan[3] =("kodok")

print(nama_hewan)