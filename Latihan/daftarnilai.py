nilai = [80, 90, 'A', 70, 100, 'B']

total = 0
jumlah = 0

for n in nilai:
    try:
        total += n      # akan error jika n bukan angka
        jumlah += 1
    except TypeError:
        # Jika n adalah string ('A', 'B'), lewati saja
        continue

rata2 = total / jumlah
print("Rata-rata nilai valid:", rata2)
print("Total nilai valid:", total) 