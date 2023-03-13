class Bio:
  def _init_(self, nama, nim, kelas_siakad, jumlah_SKS):
    self.nama = nama
    self.nim = nim
    self.kelas_siakad = kelas_siakad
    self.jumlah_sks = jumlah_SKS

  def data(self):
    print("Nama: ", self.nama)
    print("NIM: ", self.nim)
    print("Kelas_siakad: ", self.kelas_siakad)
    print("Jumlah_sks: ",self.jumlah_sks)
    
summon = Bio("Amdhan", "121140226", "RB", "20")
summon.data()