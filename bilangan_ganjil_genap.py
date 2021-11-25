angka_awal = int (input("masukkan angka awal: "))
angka_akhir =int (input("masukkan angka akhir : "))
genap=[]
ganjil=[]
for i in range (angka_awal, angka_akhir+1):
    if i%2 == 0:
        genap.append(i)
    if i%2 == 1:
        ganjil.append(i)
print("angka genap : ", genap)
print("angka ganjil: ", ganjil)