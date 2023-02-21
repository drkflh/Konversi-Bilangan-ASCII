string = input("Masukkan string yang ingin dikonversi ke ASCII: ")

# Konversi string ke ASCII
ascii_result = ""
for char in string:
    ascii_result += str(ord(char)) + " "
print("ASCII: ", ascii_result)

# Konversi string ke Desimal
decimal_result = ""
for char in string:
    decimal_result += str(ord(char)) + " "
print("Desimal: ", decimal_result)

# Konversi string ke Biner
binary_result = ""
for char in string:
    binary_result += bin(ord(char))[2:] + " "
print("Biner: ", binary_result)

# Konversi string ke Oktal
octal_result = ""
for char in string:
    octal_result += oct(ord(char))[2:] + " "
print("Oktal: ", octal_result)

# Konversi string ke Hexadesimal
hex_result = ""
for char in string:
    hex_result += hex(ord(char))[2:] + " "
print("Hexadesimal: ", hex_result)
