from geometri.bangun_ruang import BangunRuang


class Segitiga(BangunRuang):


    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def info(self):
        return 'modul untuk menghitung luar segitiga'

    def hitung_luas(self):
        return self.alas * self.tinggi / 2

