class Handphone:
    def __init__(self, Warna, RAM, Merk):
        self.Warna = Warna
        self.RAM = RAM
        self.Merk = Merk

    def printname(self):
        print(self.Warna)
        print(self.RAM)
        print(self.Merk)

class IOS(Handphone):
     def __init__(self, Warna, RAM, Merk):
         Handphone.__init__(self, Warna, RAM, Merk)
         self.KapasistasBaterai = "10000mAH"

     def IOS(Self):
        print("Warna             : ", Self.Warna)
        print("RAM               : ", Self.RAM)
        print("Merk              : ", Self.Merk)
        print("Kapasitas Baterai : ", Self.KapasistasBaterai)
        print("******************************")


class Android(Handphone):
    def __init__(self, Warna, RAM, Merk):
          Handphone.__init__(self, Warna, RAM, Merk)
          self.KapasistasBaterai = "8000mAH"

    def Android(Self):
        print("Warna             : ", Self.Warna)
        print("RAM               : ", Self.RAM)
        print("Merk              : ", Self.Merk)
        print("Kapasitas Baterai : ", Self.KapasistasBaterai)
        print("******************************")

x = IOS("Rainbow", "8 GB", "Iphone")
y = Android("silver", "4 Gb", "Xiaomi")

x.IOS()
y.Android()
