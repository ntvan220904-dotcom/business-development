# Python Programming – Tóm tắt Bài 9→13 và bộ bài luyện tập

Phạm vi: Dictionary + bài tập tình huống (bài 9–10), Kế thừa & Đa hình (bài 11), Luyện tập OOP (bài 12), Ngoại lệ & File I/O (bài 13).
Mọi đoạn code trong tài liệu này đã được chạy thử (xem `demo_kiemtra.py`).

---

## PHẦN A. TÓM TẮT KIẾN THỨC

### 1. Dictionary (từ điển) – bài 9–10

**Ý chính**
- Tập các cặp `key: value`, khai báo bằng `{}`.
- **Key** phải *bất biến* (str, số, tuple) và *không trùng*. **Value** là kiểu bất kỳ, được phép trùng.
- Từ Python 3.7, dict giữ thứ tự chèn.

| Thao tác | Câu lệnh | Giải thích |
|---|---|---|
| Tạo | `d = {"ten": "An", "tuoi": 20}` hoặc `d = dict()` | |
| Truy cập | `d["ten"]` | Key không có → **KeyError** |
| Truy cập an toàn | `d.get("lop", "N/A")` | Không có key → trả giá trị mặc định, không lỗi |
| Thêm/sửa | `d["lop"] = "K25"` | Key chưa có thì thêm, có rồi thì ghi đè |
| Gộp | `d.update({"tuoi": 21, "sdt": "09"})` | |
| Xóa | `del d["tuoi"]`, `d.pop("tuoi")`, `d.clear()` | |
| Kiểm tra key | `"ten" in d` | Slide ghi `has_key()` nhưng hàm này **đã bỏ ở Python 3**, dùng `in` |
| Duyệt | `for k, v in d.items():` | Cũng có `d.keys()`, `d.values()` |
| Mặc định | `d.setdefault("diem", 0)` | Giống `get` nhưng gán luôn nếu chưa có |
| Tạo hàng loạt | `dict.fromkeys(["a","b"], 0)` | → `{'a':0,'b':0}` |
| Số phần tử | `len(d)` | |

**Mẫu hay dùng trong bài tập lớn**
```python
# Đếm tần suất (bài 6 bài 13, thống kê doanh số...)
dem = {}
for tu in "abc abc 12 it".split():
    dem[tu] = dem.get(tu, 0) + 1          # {'abc': 2, '12': 1, 'it': 1}

# Dictionary comprehension (bài 1: bình phương 1..20)
binh_phuong = {i: i**2 for i in range(1, 21)}

# Tổng tiền kho = Σ giá × tồn
gia  = {"banana": 4, "apple": 2}
kho  = {"banana": 6, "apple": 0}
tong = sum(gia[k] * kho[k] for k in gia)

# Dictionary lồng nhau: dữ liệu người dùng / học viên
hv = {"name": "Lloyd", "homework": [90, 97], "quizzes": [88, 40], "test": [75, 90]}
tb = sum(hv["homework"]) / len(hv["homework"])
```

**Lưu ý hay sai:** dùng `d[k]` khi key có thể chưa tồn tại (nên dùng `get` hoặc `in`); key kiểu `list` sẽ gây `TypeError: unhashable`; sửa dict trong lúc đang `for` qua nó sẽ gây lỗi (hãy duyệt trên `list(d)`).

### 2. Ôn nhanh String/List/Tuple (bài tập tình huống)

| Việc cần làm | Cách làm |
|---|---|
| Xóa khoảng trắng thừa | `" ".join(s.split())` |
| Đếm từ | `len(s.split())` |
| Chuẩn hóa tên | `s.title()` hoặc `s.capitalize()` |
| Tách/gộp | `s.split(",")`, `",".join(ds)` |
| List tách chẵn lẻ | `chan = [x for x in l if x % 2 == 0]` |
| Bỏ trùng, giữ thứ tự | `list(dict.fromkeys(l))` |
| Phần tử xuất hiện đúng 1 lần (bài 7) | `[x for x in l if l.count(x) == 1]` |
| Hiệu hai list (bài 12) | `list(set(a) - set(b))` |
| Tuple bất biến → sửa | `l = list(t); l.insert(2,'c'); t = tuple(l)` |

**Sắp xếp với `sorted` / `lambda` (bài 3 tuple)**
```python
ds = [("Tom","19","80"), ("John","20","90"), ("Jony","17","93"), ("Jony","17","91")]
sorted(ds, key=lambda x: (x[0], int(x[1]), int(x[2])))   # ưu tiên tên > tuổi > điểm
sorted(ds, key=lambda x: x[2], reverse=True)             # giảm dần theo điểm
```
- `key=` nhận một hàm trả về "giá trị để so sánh"; trả về tuple thì so sánh lần lượt từng phần tử.
- `list.sort()` sắp xếp tại chỗ và trả `None`; `sorted()` trả list mới.
- Nhớ ép kiểu `int(...)` nếu dữ liệu đang là chuỗi, vì `"100" < "20"` theo chuỗi.

**Bài kiểm tra mật khẩu (mẫu dùng cho đăng nhập trong bài tập lớn)**
```python
def hop_le(p):
    return (6 <= len(p) <= 12 and any(c.islower() for c in p)
            and any(c.isupper() for c in p) and any(c.isdigit() for c in p))
print(",".join(p for p in input().split(",") if hop_le(p)))
```

### 3. Kế thừa – bài 11

```python
class Nguoi:                                  # lớp cha
    def __init__(self, hoten=None, ngaysinh=None):
        self.hoten, self.ngaysinh = hoten, ngaysinh
    def viewInfo(self):
        print("Ho ten:", self.hoten, "| Ngay sinh:", self.ngaysinh)

class ThiSinh(Nguoi):                         # lớp con
    def __init__(self, hoten, ngaysinh, sobd, toan, ly, hoa):
        super().__init__(hoten, ngaysinh)     # gọi __init__ của cha
        self.sobd, self.toan, self.ly, self.hoa = sobd, toan, ly, hoa
    def tong(self):
        return self.toan + self.ly + self.hoa
    def viewInfo(self):                       # ghi đè (override)
        super().viewInfo()                    # tái sử dụng code của cha
        print("SBD:", self.sobd, "| Tong:", self.tong())
```
- Lớp con **không có `__init__`** thì dùng `__init__` của cha.
- `super()` gọi thành phần của cha. **Ghi đè**: lớp con định nghĩa lại phương thức cùng tên.
- `issubclass(ThiSinh, Nguoi)` → True; `isinstance(ts, Nguoi)` → True (đối tượng con cũng là đối tượng cha).
- Mọi lớp đều kế thừa `object`.
- Python chỉ có một kiểu kế thừa (public). Quy ước `_x` = protected, `__x` = private (bị đổi tên, không phải bảo mật thật).

**Đa kế thừa & MRO**
```python
class A:  def hi(self): return "A"
class B:  def hi(self): return "B"
class C(A, B): pass
C().hi()                       # 'A' (ưu tiên lớp đứng trước, trái → phải)
C.mro()                        # [C, A, B, object]  (thuật toán C3)
```
Khi nhiều lớp cha đều có `__init__`, chỉ `__init__` của lớp **đầu tiên** được gọi tự động; muốn gọi cả hai phải gọi tường minh `A.__init__(self)`, `B.__init__(self)` (hoặc dùng `super()` đồng bộ ở mọi lớp).

**Lớp trừu tượng (ABC)**
```python
from abc import ABC, abstractmethod
class DaGiac(ABC):
    @abstractmethod
    def dienTich(self): ...
    @abstractmethod
    def chuVi(self): ...
class HCN(DaGiac):
    def __init__(self, a, b): self.a, self.b = a, b
    def dienTich(self): return self.a * self.b
    def chuVi(self): return 2 * (self.a + self.b)
# DaGiac()  → TypeError: Can't instantiate abstract class ...
```
- Không tạo được đối tượng của lớp trừu tượng; lớp con **bắt buộc** cài đặt hết phương thức `@abstractmethod`, nếu không cũng không khởi tạo được.
- Python không có từ khóa `interface`: dùng ABC chỉ có phương thức trừu tượng để làm "giao diện".

### 4. Đa hình – bài 11
- **Đa hình khi chạy (override):** cùng tên phương thức, mỗi lớp con làm khác nhau.
- **Nạp chồng (overload):** Python **không có** overload thật (định nghĩa cùng tên thì cái sau ghi đè cái trước). Thay bằng tham số mặc định, `*args`, hoặc kiểm tra kiểu.
- Python còn có **duck typing**: miễn đối tượng có phương thức cần gọi là dùng được, không cần cùng cha.

```python
class DongVat:
    def __init__(self, ten): self.ten = ten
    def tiengKeu(self): raise NotImplementedError
class Cho(DongVat):
    def tiengKeu(self): return "Gau gau"
class Meo(DongVat):
    def tiengKeu(self): return "Meo meo"
for v in [Cho("Lu"), Meo("Mun")]:        # cùng lời gọi, hành vi khác nhau
    print(v.ten, v.tiengKeu())

# Giả lập overload
def tinh_tong(*so): return sum(so)
tinh_tong(1, 2); tinh_tong(1, 2, 3)
```

### 5. Property & Encapsulation (bài tập cuối bài 11)
```python
class SinhVien:
    _dem = 0
    def __init__(self, ten, dtb):
        SinhVien._dem += 1
        self._masv = f"SV{SinhVien._dem:03d}"   # chỉ đọc
        self.ten = ten
        self.dtb = dtb                           # đi qua setter → có kiểm tra
    @property
    def masv(self): return self._masv            # không có setter → chỉ lấy
    @property
    def dtb(self): return self._dtb
    @dtb.setter
    def dtb(self, v):
        if not 0 <= v <= 10:
            raise ValueError("DTB phai trong [0, 10]")
        self._dtb = v
```
- `@property` biến phương thức thành thuộc tính; `@x.setter` thêm kiểm tra khi gán.
- Gán vào property không có setter → `AttributeError`. Đây là cách làm "thuộc tính chỉ cho phép lấy".
- Biến lớp (`SinhVien._dem`) dùng chung cho mọi đối tượng, hợp để tự sinh mã.

### 6. Ngoại lệ – bài 13

**Cấu trúc đầy đủ**
```python
try:
    x = int(input("So: "))
    kq = 10 / x
except ValueError:                 # gõ chữ thay vì số
    print("Phai nhap so nguyen")
except ZeroDivisionError as e:     # as e → lấy thông điệp lỗi
    print("Loi:", e)
except Exception as e:             # bắt mọi lỗi còn lại (đặt CUỐI CÙNG)
    print("Loi khac:", e)
else:                              # chạy khi KHÔNG có lỗi
    print("Ket qua:", kq)
finally:                           # LUÔN chạy (đóng file, giải phóng tài nguyên)
    print("Xong")
```
> Slide dùng cú pháp cũ `except Kiểu, Tham_số` (Python 2). Ở Python 3 phải viết **`except Kiểu as tham_số`**.

**Các ngoại lệ hay gặp**: `ZeroDivisionError` (chia 0), `ValueError` (sai giá trị, vd `int("abc")`), `TypeError` (sai kiểu), `IndexError` (chỉ số ngoài list), `KeyError` (key không có trong dict), `NameError`, `AttributeError`, `FileNotFoundError` (con của `OSError`/`IOError`), `ImportError`, `AssertionError`, `KeyboardInterrupt`.
Lưu ý: slide ghi `ZeroDivisonError` (thiếu "i") và `StandardError`/`has_key`/`file.next()` đều của Python 2; Python 3 không còn.

**Ngoại lệ tự định nghĩa và `raise`**
```python
class DiemKhongHopLe(Exception):
    def __init__(self, diem):
        super().__init__(f"Diem {diem} nam ngoai [0, 10]")
        self.diem = diem

def nhap_diem(d):
    if not 0 <= d <= 10:
        raise DiemKhongHopLe(d)       # chủ động ném lỗi
    return d

try:
    nhap_diem(11)
except DiemKhongHopLe as e:
    print(e)
```
**Mẫu nhập liệu chắc chắn (dùng rất nhiều trong menu của bài tập lớn):**
```python
def nhap_so_nguyen(msg, lo=None, hi=None):
    while True:
        try:
            n = int(input(msg))
            if (lo is not None and n < lo) or (hi is not None and n > hi):
                print("Ngoai khoang cho phep"); continue
            return n
        except ValueError:
            print("Vui long nhap so nguyen")
```

### 7. File I/O – bài 13

**Mở file**: `open(ten_file, che_do, encoding="utf-8")`

| Chế độ | Ý nghĩa |
|---|---|
| `r` | Đọc (mặc định), lỗi nếu file chưa có |
| `w` | Ghi, **xóa sạch** nội dung cũ, tạo mới nếu chưa có |
| `a` | Ghi **nối thêm** vào cuối |
| `x` | Tạo mới, lỗi nếu đã tồn tại |
| `r+` / `w+` / `a+` | Đọc và ghi |
| thêm `b` (`rb`, `wb`) | Chế độ nhị phân |

**Đọc/ghi text**
```python
with open("data.txt", "w", encoding="utf-8") as f:   # `with` tự đóng file kể cả khi lỗi
    f.write("Thuc\n")
    f.writelines(["hanh\n", "voi\n"])                # writelines không tự thêm \n

with open("data.txt", encoding="utf-8") as f:
    s    = f.read()          # toàn bộ file thành 1 chuỗi (read(n): n ký tự)
    # f.readline()           # 1 dòng, giữ ký tự \n ở cuối
    # f.readlines()          # list các dòng
    # for dong in f: ...     # cách duyệt từng dòng tiết kiệm bộ nhớ nhất
```
- Thuộc tính: `f.closed`, `f.mode`, `f.name`.
- `f.tell()` cho vị trí con trỏ; `f.seek(offset, from)` dời con trỏ (`0` đầu file, `1` vị trí hiện tại, `2` cuối file; ở chế độ text chỉ nên dùng `seek(0)` hoặc `seek(0, 2)`).
- `f.flush()` đẩy bộ đệm xuống đĩa, `f.truncate(size)` cắt file.
- Module `os`: `os.rename(cu, moi)`, `os.remove(ten)`, `os.path.exists(ten)`.

**File nhị phân & lưu cấu trúc dữ liệu**
```python
with open("b.bin", "wb") as f:  f.write(bytes([3, 6, 9, 12, 18]))
with open("b.bin", "rb") as f:  print(list(f.read()))     # [3, 6, 9, 12, 18]

import json, pickle
d = {"ten": "An", "diem": [8, 9]}
json.dump(d, open("d.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
d2 = json.load(open("d.json", encoding="utf-8"))
pickle.dump(d, open("d.pkl", "wb"));  d3 = pickle.load(open("d.pkl", "rb"))
```
- **json**: dạng text, đọc được bằng mắt, dùng chung với ngôn ngữ khác; chỉ lưu kiểu cơ bản (dict, list, str, số, bool, None).
- **pickle**: nhị phân, lưu được cả **đối tượng của lớp tự định nghĩa**, nhưng **không tải file pickle không đáng tin** (có thể chạy mã độc).
- Cũng có thể ghi CSV bằng module `csv`.

**Gói file + ngoại lệ (mẫu chuẩn)**
```python
def doc_file(ten):
    try:
        with open(ten, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("Khong tim thay file", ten)
        return ""
```

### 8. Ứng dụng vào Bài tập lớn

Khung chương trình quản lý (sản phẩm / khách hàng / hóa đơn, slide bài 12) gồm 4 lớp nền:

```
Lớp thực thể      → SanPham, KhachHang, HoaDon (+ ChiTietHoaDon)       [OOP, property, kiểm tra dữ liệu]
Lớp danh sách     → DSSanPham, DSKhachHang, DSHoaDon                    [list/dict, thêm-sửa-xóa-tìm-sắp xếp-thống kê]
Lớp lưu trữ       → đọc/ghi json hoặc pickle                            [File I/O]
Lớp giao diện     → menu vòng lặp while True                            [try/except, nhập liệu an toàn]
```

**Sườn code dùng lại được** (đã chạy thử):
```python
import json

class SanPham:
    def __init__(self, ma, ten, ton, gia):
        self.ma, self.ten, self.ton, self.gia = ma, ten, ton, gia
    def to_dict(self):   return self.__dict__.copy()
    @staticmethod
    def from_dict(d):    return SanPham(**d)

class DSSanPham:
    def __init__(self): self.ds = {}                     # dict: ma -> SanPham (tìm O(1))
    def them(self, sp):
        if sp.ma in self.ds: raise ValueError("Ma san pham da ton tai")
        self.ds[sp.ma] = sp
    def xoa(self, ma):
        if self.ds.pop(ma, None) is None: raise KeyError("Khong co ma " + ma)
    def tim_theo_ten(self, kw):
        return [s for s in self.ds.values() if kw.lower() in s.ten.lower()]
    def sap_xep_gia(self, giam=False):
        return sorted(self.ds.values(), key=lambda s: s.gia, reverse=giam)
    def thong_ke_ton(self):
        return sum(s.ton * s.gia for s in self.ds.values())
    def luu(self, f):
        with open(f, "w", encoding="utf-8") as fh:
            json.dump([s.to_dict() for s in self.ds.values()], fh, ensure_ascii=False, indent=2)
    def tai(self, f):
        try:
            with open(f, encoding="utf-8") as fh:
                self.ds = {d["ma"]: SanPham.from_dict(d) for d in json.load(fh)}
        except FileNotFoundError:
            self.ds = {}                                 # lần chạy đầu chưa có file
```

Menu:
```python
def menu():
    ql = DSSanPham(); ql.tai("sp.json")
    while True:
        print("\n1. Them  2. Xoa  3. Tim  4. Sap xep  5. Thong ke  0. Thoat")
        try:
            c = int(input("Chon: "))
            if c == 1: ql.them(SanPham(input("Ma: "), input("Ten: "), int(input("Ton: ")), float(input("Gia: "))))
            elif c == 2: ql.xoa(input("Ma: "))
            elif c == 3: [print(s.ma, s.ten) for s in ql.tim_theo_ten(input("Tu khoa: "))]
            elif c == 4: [print(s.ten, s.gia) for s in ql.sap_xep_gia()]
            elif c == 5: print("Gia tri ton kho:", ql.thong_ke_ton())
            elif c == 0: ql.luu("sp.json"); break
        except (ValueError, KeyError) as e:
            print("Loi:", e)
```

**Checklist trước khi nộp bài tập lớn**
1. Mỗi thực thể một lớp; dữ liệu nhạy cảm dùng `property` + kiểm tra hợp lệ (điểm 0–10, giá > 0, email có `@`).
2. Có ít nhất một chỗ **kế thừa + ghi đè** (ví dụ `NhanVienBienChe` / `NhanVienHopDong` cùng có `tinhLuong()`), và/hoặc lớp trừu tượng `NhanVien(ABC)`.
3. Mọi `input` ép kiểu đều bọc `try/except ValueError`; mọi thao tác file bọc `FileNotFoundError`.
4. Dữ liệu lưu `json`/`pickle` và tải lại khi mở chương trình.
5. Có tìm kiếm, sắp xếp (`sorted` + `lambda`), thống kê (`sum`, dict đếm).
6. Có mã nguồn chạy được từ đầu đến cuối, có dữ liệu mẫu, có hướng dẫn sử dụng.

---

## PHẦN B. ĐỀ LUYỆN TẬP

Gợi ý cách làm: tự làm trước, chạy thử, rồi so với phần gợi ý ở Phần C.

### Mức 1 – Khởi động (Dictionary, File, Ngoại lệ)
1. Cho `gia = {"banana":4, "apple":2, "orange":1.5, "pear":3}` và `kho = {"banana":6, "apple":0, "orange":32, "pear":15}`. In giá và tồn kho từng loại, tổng tiền nếu bán hết kho, rồi liệt kê mặt hàng **hết hàng** (tồn = 0).
2. Nhập một câu, đếm tần suất từng từ (không phân biệt hoa thường), in 3 từ xuất hiện nhiều nhất.
3. Viết hàm `chia_an_toan(a, b)` trả về thương, in thông báo và trả `None` khi chia 0 hoặc khi tham số không phải số.
4. Viết chương trình nhập `n`, đọc `n` dòng đầu của file `data.txt`. Nếu file không tồn tại hoặc `n` không hợp lệ thì thông báo lỗi tương ứng, không để chương trình sập.
5. Ghi 5 dòng vào `ds.txt`, sau đó mở chế độ `a` thêm 2 dòng nữa, đọc lại và đánh số thứ tự từng dòng.
6. Cho file `demo_file2.txt` chứa `Dem so luong tu xuat hien abc abc abc 12 12 it it itplus`. Đếm từ và lưu kết quả vào `ketqua.json`, rồi đọc ngược lại để kiểm tra.

### Mức 2 – Lớp, kế thừa, property
7. **Sinh viên có kiểm tra:** lớp `SinhVien` có `masv` (8 ký tự, chỉ đọc), `ten`, `tuoi` (16–60), `dtb` (0–10), `email` (phải chứa `@`, không có khoảng trắng). Dùng `property` + ném `ValueError` khi sai. Nhập `n` sinh viên (nhập sai thì hỏi lại), in danh sách theo ĐTB giảm dần, rồi in những sinh viên đủ điều kiện học bổng (ĐTB ≥ 8.0).
8. **Hình học:** lớp trừu tượng `Hinh` có `dienTich()` và `chuVi()`; các lớp `HinhChuNhat`, `HinhTron`, `TamGiac` kế thừa. Tạo danh sách hỗn hợp, in thông tin từng hình, tìm hình có diện tích lớn nhất và tổng chu vi.
9. **Lương nhân viên:** lớp cha `NhanVien(hoten, cmnd, phongban)`; `BienChe` (bậc lương × 560000), `HopDong` (số giờ × tiền công/giờ), thêm `QuanLy` (lương = lương biên chế + phụ cấp). Dùng **một list chung**, in lương từng người và tổng lương theo từng loại và toàn cơ quan (dùng `isinstance`).
10. **Sở thú:** `Animal` (tên, tuổi, mô tả; `xemThongTin()`, `tiengKeu()`), các lớp con `Tiger`, `Dog`, `Cat` ghi đè `tiengKeu()`; lớp `Chuong` (mã, danh sách con vật; `themConVat`, `xoaConVat(ten)`), lớp `Zoo` (danh sách chuồng; `themChuong`, `xoaChuong`). Viết menu cho phép thêm chuồng, thêm con vật (chọn loại), xóa, và hiển thị toàn bộ thông tin cùng tiếng kêu.
11. **Đa kế thừa:** tạo `Bay` (có `di_chuyen()` in "Bay"), `Boi` (có `di_chuyen()` in "Boi"), lớp `Vit(Bay, Boi)`. Dự đoán rồi kiểm chứng `Vit().di_chuyen()` in ra gì, in `Vit.mro()`. Sau đó sửa để `Vit.di_chuyen()` gọi **cả hai** hành vi.

### Mức 3 – Tích hợp (gần với bài tập lớn)
12. **Đăng nhập an toàn:** dict `tai_khoan = {ten: mat_khau}` gồm 5 tài khoản. Cho phép tối đa 3 lần nhập sai; thành công thì cho đổi mật khẩu (mật khẩu mới phải hợp lệ: 6–12 ký tự, có chữ hoa, chữ thường, số); ghi lại `tai_khoan` vào `tk.json`. Tạo ngoại lệ riêng `SaiMatKhau`, `TaiKhoanKhongTonTai`.
13. **Quản lý bán sách (mini-project):**
    - Lớp `Sach(ma, ten, tacgia, gia, ton)` với `property` kiểm tra (giá > 0, tồn ≥ 0).
    - Lớp `KhachHang(ma, ten, email)`.
    - Lớp `HoaDon(mahd, ngay, khachhang, chitiet)` với `chitiet` là dict `{ma_sach: so_luong}`; không cho bán quá tồn kho (ném ngoại lệ `KhongDuHang`).
    - Menu: quản lý sách (thêm/sửa/xóa/tìm/sắp xếp), quản lý khách, lập hóa đơn, thống kê doanh thu theo ngày và top 3 sách bán chạy.
    - Lưu/đọc toàn bộ dữ liệu bằng `json` (chuyển đối tượng ↔ dict), khởi động chương trình sẽ tải lại dữ liệu.
14. **Phân tích điểm từ file:** file `diem.csv` dạng `ten,toan,ly,hoa` (tạo tay 10 dòng). Đọc file (bỏ qua dòng lỗi, đếm số dòng lỗi), tạo lớp `ThiSinh` kế thừa `Nguoi`, in danh sách giảm dần theo ĐTB, đếm số thí sinh đạt (tổng ≥ 20), ghi bảng xếp hạng ra `xephang.txt`.
15. **Câu hỏi lý thuyết ngắn:**
    a. Khác nhau giữa `w` và `a`? Giữa `read()`, `readline()`, `readlines()`?
    b. Khi nào khối `else` và khối `finally` của `try` được chạy?
    c. Vì sao `with open(...)` tốt hơn `open()` + `close()`?
    d. Lớp trừu tượng khác lớp thường ở điểm nào? Khi nào dùng?
    e. `json` khác `pickle` ra sao? Chọn cái nào để lưu danh sách đối tượng tùy ý?
    f. Python có overload không? Cách thay thế là gì?
    g. Kết quả của `class C(A, B)` khi A và B cùng có phương thức `hi()`?

---

## PHẦN C. GỢI Ý ĐÁP ÁN (chỉ xem sau khi đã tự làm)

**Bài 1**
```python
for k in gia: print(k, gia[k], kho[k])
print(sum(gia[k]*kho[k] for k in gia))
print([k for k in kho if kho[k] == 0])
```
**Bài 2**
```python
dem = {}
for w in input().lower().split(): dem[w] = dem.get(w, 0) + 1
print(sorted(dem.items(), key=lambda kv: kv[1], reverse=True)[:3])
```
**Bài 3**
```python
def chia_an_toan(a, b):
    try: return a / b
    except ZeroDivisionError: print("Khong chia cho 0")
    except TypeError: print("Tham so phai la so")
```
**Bài 4**
```python
try:
    n = int(input("n = "))
    with open("data.txt", encoding="utf-8") as f:
        for i, dong in enumerate(f):
            if i >= n: break
            print(dong.rstrip())
except ValueError: print("n phai la so nguyen")
except FileNotFoundError: print("Khong co file data.txt")
```
**Bài 8** – khung lớp: `class Hinh(ABC)` với hai `@abstractmethod`; `max(ds, key=lambda h: h.dienTich())`; `sum(h.chuVi() for h in ds)`; dùng `math.pi` cho hình tròn, công thức Heron cho tam giác.

**Bài 9**
```python
class NhanVien(ABC):
    def __init__(self, hoten, cmnd, pb): self.hoten, self.cmnd, self.pb = hoten, cmnd, pb
    @abstractmethod
    def tinhLuong(self): ...
class BienChe(NhanVien):
    def __init__(self, hoten, cmnd, pb, bac): super().__init__(hoten, cmnd, pb); self.bac = bac
    def tinhLuong(self): return self.bac * 560000
class HopDong(NhanVien):
    def __init__(self, hoten, cmnd, pb, gio, cong): super().__init__(hoten, cmnd, pb); self.gio, self.cong = gio, cong
    def tinhLuong(self): return self.gio * self.cong
ds = [BienChe("A","1","KT",3), HopDong("B","2","KD",100,50000)]
tong_bc = sum(n.tinhLuong() for n in ds if isinstance(n, BienChe))
tong_hd = sum(n.tinhLuong() for n in ds if isinstance(n, HopDong))
```
**Bài 11** – kết quả `"Bay"` vì A đứng trước trong MRO `[Vit, Bay, Boi, object]`. Muốn gọi cả hai: trong `Vit` viết `Bay.di_chuyen(self); Boi.di_chuyen(self)`.

**Bài 12** – vòng `for lan in range(3)` + `try/except`; ngoại lệ riêng: `class SaiMatKhau(Exception): pass`. Kiểm tra mật khẩu mới bằng hàm `hop_le` ở Phần A.2. Lưu `json.dump(tai_khoan, f)`.

**Bài 13 – ý chính cần nhớ**
- Lưu: `json.dump([s.to_dict() for s in ...])`, tải: `Sach(**d)`. Đối tượng lồng nhau (hóa đơn → khách) chỉ lưu **mã khách**, khi tải tra lại từ dict khách hàng.
- Kiểm tra tồn kho trong `HoaDon.them_chi_tiet`: nếu `sl > sach.ton` thì `raise KhongDuHang(...)`, trừ kho chỉ khi cả hóa đơn hợp lệ.
- Top 3 bán chạy: dict `ban[ma] += sl` rồi `sorted(ban.items(), key=lambda kv: kv[1], reverse=True)[:3]`.

**Bài 15 (đáp án ngắn)**
a. `w` xóa nội dung cũ, `a` ghi nối cuối. `read()` đọc cả file thành chuỗi, `readline()` một dòng, `readlines()` list các dòng.
b. `else` chạy khi `try` không lỗi; `finally` luôn chạy dù có lỗi hay không.
c. `with` tự đóng file kể cả khi xảy ra ngoại lệ, tránh rò rỉ tài nguyên.
d. Lớp trừu tượng không khởi tạo trực tiếp được, ép lớp con cài đặt phương thức bắt buộc; dùng để định khuôn chung cho nhóm lớp.
e. `json` là text, dễ đọc, chỉ kiểu cơ bản; `pickle` là nhị phân, lưu được đối tượng tùy ý nhưng chỉ tải từ nguồn tin cậy. Với đối tượng tùy ý có thể dùng `pickle`, hoặc tốt hơn là chuyển sang dict rồi `json`.
f. Không; dùng tham số mặc định, `*args/**kwargs` hoặc kiểm tra kiểu.
g. Gọi phương thức của A (lớp đứng đầu trong MRO).
