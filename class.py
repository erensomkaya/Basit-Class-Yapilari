class araba():
    def __init__(self,renk,marka,model):
        print("ARABA ÖZELLİKLERİ")
        self.renk = renk
        self.marka = marka
        self.model = model
    def bilgi(self):
        print("Renk : {}\nMarka : {}\nModel : {}".format(self.renk,self.marka,self.model))
class kişi():
    def __init__(self,isim,soyisim,yaş):
        print("Kişi Bilgileri")
        self.isim = isim
        self.soyisim = soyisim
        self.yaş = yaş
    def bilgiler(self):
        print("İsim : {}\nSoyisim : {}\nYaş : {}".format(self.isim,self.soyisim,self.yaş))

-bu işlemi kaydedin daha sonra 


-bu kısma geçiniz.

Kişi = kişi("EREN","SOMKAYA",22)
Araba = araba("KIRMIZI","BMW",2020)

-bu kısmıda kaydedin

-bu kısma geçin

Kişi.bilgiler()
Araba.bilgi()
