# Input angka pertama
while True:
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        break
    except ValueError:
        print("Error: harus angka!")

# Input angka kedua
while True:
    try:
        angka2 = float(input("Masukkan angka kedua  : "))
        break
    except ValueError:
        print("Error: harus angka!")

# Input operator
while True:
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

        break  # keluar loop jika berhasil

    except ZeroDivisionError:
        print("Error: tidak bisa membagi dengan nol!")
    except Exception as e:
        print("Error:", e)

print("Hasil:", hasil)