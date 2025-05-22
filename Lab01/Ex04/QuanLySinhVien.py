#QLSV
from SinhVien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []

    def generateID(self):
        maxId = 1
        if self.soLuongSinhVien() > 0:
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if maxId < sv._id:
                    maxId = sv._id
            maxId += 1
        return maxId

    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        svId = self.generateID()
        ten = input("Nhap ten sinh vien: ")
        gt = input("Nhap gioi tinh sinh vien: ")
        chuyennganh = input("Nhap chuyen nganh cua sinh vien: ")
        diemTB = float(input("Nhap diem cua sinh vien: "))
        sv = SinhVien(svId, ten, gt, chuyennganh, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if sv is not None:
            ten = input("Nhap ten sinh vien: ")
            gt = input("Nhap gioi tinh sinh vien: ")
            chuyennganh = input("Nhap chuyen nganh cua sinh vien: ")
            diemTB = float(input("Nhap diem cua sinh vien: "))
            sv.setten(ten)
            sv.setgt(gt)
            sv.setchuyennganh(chuyennganh)
            sv.setDiemTB(diemTB)
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh vien co ID = {} khong ton tai.".format(ID))

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id)

    def sortByten(self):
        self.listSinhVien.sort(key=lambda x: x._ten)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB)

    def findByID(self, ID):
        for sv in self.listSinhVien:
            if sv._id == ID:
                return sv
        return None

    def findByten(self, keyword):
        listSV = []
        for sv in self.listSinhVien:
            if keyword.lower() in sv._ten.lower():
                listSV.append(sv)
        return listSV

    def deleteByID(self, ID):
        sv = self.findByID(ID)
        if sv:
            self.listSinhVien.remove(sv)
            return True
        return False

    def xepLoaiHocLuc(self, sv):
        if sv._diemTB >= 8:
            sv._hocLuc = "Gioi"
        elif sv._diemTB >= 6.5:
            sv._hocLuc = "Kha"
        elif sv._diemTB > 5:
            sv._hocLuc = "Trung binh"
        else:
            sv._hocLuc = "Yeu"

    def showSinhVien(self, listSV):
        print('{:<8} {:<18} {:<8} {:<12} {:<10} {:<10}'
              .format("ID", "ten", "gt", "chuyennganh", "Diem TB", "Hoc Luc"))
        for sv in listSV:
            print('{:<8} {:<18} {:<8} {:<12} {:<10} {:<10}'
                  .format(sv._id, sv._ten, sv._gt, sv._chuyennganh, sv._diemTB, sv._hocLuc))
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien