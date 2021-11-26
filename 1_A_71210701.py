def calculator():
    X = ("======== Calculator sederhana ========\n")
    Y = ("1. Pertambahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Perpangkatan")
    return(X+Y)

def tambah():
    A1 = int(input("Masukkan bilangan 1: "))
    A2 = int(input("Masukkan bilangan 2: "))
    return A1 + A2 
def kurang():
    A1 = int(input("Masukkan bilangan 1: "))
    A2 = int(input("Masukkan bilangan 2: "))
    return A1 - A2 
def kali():
    A1 = int(input("Masukkan bilangan 1: "))
    A2 = int(input("Masukkan bilangan 2: "))
    return A1 * A2 
def bagi():
    A1 = int(input("Masukkan bilangan 1: "))
    A2 = int(input("Masukkan bilangan 2: "))
    return A1 / A2 
def pangkat():
    A1 = int(input("Masukkan bilangan 1: "))
    A2 = int(input("Masukkan bilangan 2: "))
    return A1 ** A2 
print(calculator())
Data = int(input("Masukkan pilihan: "))
if Data == 5:
    Hasil = pangkat()
    print("Hasilnya:",Hasil)
elif Data == 4:
    Hasil = bagi()
    print("Hasilnya:",Hasil)
elif Data == 3:
    Hasil = kali()
    print("Hasilnya:",Hasil)
elif Data == 2:
    Hasil = kurang()
    print("Hasilnya:",Hasil)
elif Data == 1:
    Hasil = tambah()
    print("Hasilnya:",Hasil)
else:
    print("Maaf input operasi antara 1-5")