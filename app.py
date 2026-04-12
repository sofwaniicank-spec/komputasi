import sys

print(sys.argv)

class penduduk: 
    def __init__(self *args): # paggil(nama,nik,umur)
        self.nama = args[0]
        self.nik = args[1]
        self.umur = args[2]

    def cek_umur(self):
        return self.umur    

    def cek_nik(self):
        return "NIK : {self.__nik}"


andre  = penduduk("Andre", 20032031, 21)

print(andre.nama)
print(andre.cek_umur())
print(andre.cek_nik())