from geometri.persegipanjang import PersegiPanjang
from geometri.segitiga import Segitiga

p1 = PersegiPanjang(10, 8)
print(p1.info())
print(p1.hitung_luas())

print('=' * 30)
s1 = Segitiga(4, 7)
print(s1.info())
print(s1.hitung_luas())