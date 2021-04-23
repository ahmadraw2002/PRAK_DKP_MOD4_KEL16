huruf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def enkripsi(huruf):
    str = input("Masukkan kata : ") 
    key = int(input("Key : ")) 

    str = str.lower() 
    result = '' 

    for char in str: 
        if char in huruf: 
            n = huruf.index(char) 
            encrypt = (n + key) % 26 
            convert = huruf[encrypt] 
            result = result + convert 
        else:
            result = result + ' ' 

    print(f"Result : {result}") 

def dekripsi(huruf):
    str = input("Masukkan kata : ") 
    key = int(input("Key : ")) 

    str = str.lower() 
    result = '' 

    for char in str: 
        if char in huruf: 
            n = huruf.index(char) 
            encrypt = (n - key) % 26 
            convert = huruf[encrypt] 
            result = result + convert 
        else:
            result = result + ' '

    print(f"Result : {result}")


pilihan = 'y'

while (pilihan == 'y'):
    print("Menu yang tersedia : ")
    print("1. Enkripsi Data")
    print("2. Dekripsi Data")
    print("3. Keluar")

    menu = input("Menu yang dipilih [1/2/3] : ")
    print("-------------------------------------")

    if menu == '1':
        print("Menu Enkripsi Data")
        enkripsi(huruf)
    elif menu == '2':
        print("Menu Dekripsi Data")
        dekripsi(huruf)
    elif menu == '3':
        print("Program Selesai, terima kasih.")
        break
    else:
        print("Menu tidak ditemukan")

    print("------------------------------------")
    pilihan = input("Apakah ingin melanjutkan ? (y/n) : ")

pilihan = 'n'
while(pilihan == 'n'):
    print("Program selesai")
    break
    print("------------------------------------")