usn = 'informatika'
pwd = '12345678'
cek = False

while(cek == False):
    
    username = input("masukan username :")
    password = input("masukan password :") 

    if username == usn and password == pwd:
        print ("berhasil login!")
        break
    else:
        print("username atau password salah coba lagi")
        