# Fungsi untuk konversi ke biner
def to_binary(ascii_string):
    return ''.join(format(ord(char), '08b') for char in ascii_string)

# Fungsi untuk konversi ke heksadesimal


def to_hex(ascii_string):
    return ''.join(hex(ord(char))[2:] for char in ascii_string)

# Fungsi untuk konversi ke oktal


def to_octal(ascii_string):
    return ''.join(format(ord(char), '03o') for char in ascii_string)

# Fungsi untuk konversi ke bilangan desimal


def to_decimal(ascii_string):
    return ''.join(str(ord(char)) for char in ascii_string)


# Menu utama
while True:
    print("===== Konversi ASCII String =====")
    print("1. Konversi ke Biner")
    print("2. Konversi ke Heksadesimal")
    print("3. Konversi ke Oktal")
    print("4. Konversi ke Bilangan Desimal")
    print("0. Keluar")

    # Meminta pilihan dari user
    choice = input("Masukkan pilihan Anda: ")

    if choice == '1':
        ascii_string = input("Masukkan ASCII string: ")
        print("Biner: ", to_binary(ascii_string))
    elif choice == '2':
        ascii_string = input("Masukkan ASCII string: ")
        print("Heksadesimal: ", to_hex(ascii_string))
    elif choice == '3':
        ascii_string = input("Masukkan ASCII string: ")
        print("Oktal: ", to_octal(ascii_string))
    elif choice == '4':
        ascii_string = input("Masukkan ASCII string: ")
        print("Bilangan Desimal: ", to_decimal(ascii_string))
    elif choice == '0':
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
