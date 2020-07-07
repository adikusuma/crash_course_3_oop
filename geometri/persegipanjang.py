from geometri.bangun_ruang import BangunRuang


class PersegiPanjang(BangunRuang):


    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def info(self):
        return 'modul ini untuk menghitung luas persegi panjang'

    def hitung_luas(self):
        return self.panjang * self.lebar
