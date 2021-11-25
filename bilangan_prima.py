jumlah = 0
angka = int(input("masukkan angka: "))
for i in range(1, angka + 1, 1):
    if angka % i == 0:
        jumlah = jumlah + 1
if jumlah == 2:
    print(str(angka) +  ":adalah bilangan prima")
else:
    print(str(angka) +  ":adalah bukan bilangan prima")
