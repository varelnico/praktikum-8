try:
     angka1 = float(input("Masukkan angka pertama: "))
except ValueError:
        print("Error: harus angka!")
try:
    angka2 = float(input("Masukkan angka kedua  : "))
except ValueError:
    print("Error: harus angka!")
operator = input("Masukkan operator (+, -, *, /): ")
try:
    if operator == "+":
        hasil = angka1 + angka2
    elif operator == "-":
        hasil = angka1 - angka2
    elif operator == "*":
        hasil = angka1 * angka2
    elif operator == "/":
        hasil = angka1 / angka2
    else:
        raise Exception("Operator tidak valid")    
except ZeroDivisionError:
    print("Error: tidak bisa membagi dengan nol!")
except Exception as e:
    print("Error:", e)

print("Hasil:", hasil) 