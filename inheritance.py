class Orang:
    nama = None
    def _init_(self, nama):
        self.nama = nama

    def info(self):
        #cetak info
        print("Nama:",self.nama)

class Mahasiswa(Orang):
    npm = None
    def _init_(self, nama, npm, semester):
        Orang._init_(self, nama)
        self.semester = semester
       
    def info(self):
        Orang.info(self)
        print("Nama:",self.nama)
        print("NPM:",self.npm)
        print("Semester:",self.semester)

class Pegawai(Orang):
    nidn = None
    def _init_(self, nip, nama):
        self.nip = nip
        
    def info(self):
        Orang.info(self)
        print("NIP:",self.nip)
        print("Nama:",self.nama)

class Dosen(Pegawai):
    def _init_(self, nip, nama, nidn):
        self.nip = nip
        
    def info(self):
        Orang.info(self)
        print("NIP:",self.nip)
        print("Nama:",self.nama)
        print("NIDN:",self.nidn)
        
class Karyawan(Pegawai):
    def _init_(self, nip, nama):
        self.nama = nama
        
    def info(self):
        print("NIP:", self.nip)
        print("Nama:", self.nama)
