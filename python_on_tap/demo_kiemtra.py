import os, json, pickle
from abc import ABC, abstractmethod

# ---- Exception
class AmAmError(Exception):
    pass
def chia(a, d):
    try:
        return a / d
    except ZeroDivisionError as e:
        print("Loi:", e); return None
    else:
        pass
    finally:
        pass
print(chia(10, 0))
try:
    raise AmAmError("gia tri am")
except AmAmError as e:
    print("Custom:", e)

# ---- File
with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("Thuc\nhanh\nvoi\nfile\nIO\n")
with open("demo.txt", encoding="utf-8") as f:
    print([l.strip() for l in f])
text = "Dem so luong tu xuat hien abc abc abc 12 12 it it itplus"
d = {}
for w in text.split():
    d[w] = d.get(w, 0) + 1
print(d)
with open("d.json", "w") as f: json.dump(d, f)
print(json.load(open("d.json")) == d)
with open("d.pkl", "wb") as f: pickle.dump(d, f)
print(pickle.load(open("d.pkl", "rb")) == d)
os.remove("demo.txt"); os.remove("d.json"); os.remove("d.pkl")

# ---- OOP
class Nguoi:
    def __init__(self, hoten=None, ngaysinh=None):
        self.hoten, self.ngaysinh = hoten, ngaysinh
    def viewInfo(self): print(self.hoten, self.ngaysinh)
class ThiSinh(Nguoi):
    def __init__(self, hoten, ngaysinh, sobd, toan, ly, hoa):
        super().__init__(hoten, ngaysinh)
        self.sobd, self.toan, self.ly, self.hoa = sobd, toan, ly, hoa
    def tong(self): return self.toan + self.ly + self.hoa
    def viewInfo(self):
        super().viewInfo(); print(self.sobd, self.tong())
ds = [ThiSinh("A","1/1/2005","01",7,8,9), ThiSinh("B","2/2/2005","02",5,6,7)]
ds.sort(key=lambda t: t.tong(), reverse=True)
for t in ds: t.viewInfo()
print(sum(1 for t in ds if t.tong() >= 20))

class DaGiac(ABC):
    @abstractmethod
    def dienTich(self): ...
class HCN(DaGiac):
    def __init__(self, a, b): self.a, self.b = a, b
    def dienTich(self): return self.a * self.b
try: DaGiac()
except TypeError as e: print("TypeError:", e)
print(HCN(3,4).dienTich())

class A: 
    def hi(self): return "A"
class B: 
    def hi(self): return "B"
class C(A, B): pass
print(C().hi(), [k.__name__ for k in C.mro()])

class SV:
    _n = 0
    def __init__(self, ten, dtb):
        SV._n += 1; self._masv = f"SV{SV._n:03d}"; self.ten = ten; self.dtb = dtb
    @property
    def masv(self): return self._masv
    @property
    def dtb(self): return self._dtb
    @dtb.setter
    def dtb(self, v):
        if not 0 <= v <= 10: raise ValueError("DTB 0-10")
        self._dtb = v
s = SV("An", 8.5); print(s.masv, s.dtb)
try: s.dtb = 11
except ValueError as e: print(e)
try: s.masv = "x"
except AttributeError as e: print("AttributeError")

# ---- dict / sort
print(sorted([("Tom","19","80"),("John","20","90"),("Jony","17","93"),("Jony","17","91")], key=lambda x:(x[0],int(x[1]),int(x[2]))))
print({i:i**2 for i in range(1,21)}[20])
def ticket(s, ds):
    n = 0
    for v in ds:
        if v <= s:
            s -= v; n += 1
            if s <= 3: break
    return n, s
print(ticket(8,[2,1,6,3]))
