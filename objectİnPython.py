#NESNE TABANLI PROGRAMLAMA
class calisan:
    def __init__(self,name,surname,salary):
        self.name=name
        self.surname=surname
        self.salary=salary
        self.email=self.name+self.surname+"@gazi.edu.tr"
    def showInfo(self):
        return print(f"ad: {self.name} soyad: {self.surname} maas: {self.salary} email: {self.email}")
calisan1=calisan("Buse","Tuğlu",100000)
print(calisan1.name,calisan1.surname,calisan1.salary)
print(calisan1.showInfo())

calisan2=calisan("Ayse","Can",30000)
print(calisan2.showInfo())

calisan3=calisan("Cem","Zengin",60000)
print(calisan3.showInfo())

class ogrenci:
    def __init__(self,ad,soyad,vize,odev,final):
        self.ad=ad
        self.soyad=soyad
        self.vize=vize
        self.odev=odev
        self.final=final
    def ortalama(self):
        ortalama=self.vize*0.35+self.odev*0.15+self.final*0.5
        return ortalama
    def durum(self):

        if self.ortalama()>=50:
            print("gecti")
        else:
            print("kaldi")


ogrenci1=ogrenci("Ayse","Yilmaz",50,50,50)
ogrenci2=ogrenci("Ahmet","Can",60,60,60)
print(ogrenci1.ad,ogrenci1.soyad,ogrenci1.ortalama())
print(ogrenci2.ad,ogrenci2.soyad,ogrenci2.ortalama())
print(ogrenci1.durum())

class hasta:
    def __init__(self,ad,yas,sistolikTansiyon,diyastolikTansiyon):
        self.ad=ad
        self.yas=yas
        self.sistolikTansiyon=sistolikTansiyon
        self.diyastolikTansiyon=diyastolikTansiyon
    def risk(self):
        if self.sistolikTansiyon>140 or self.diyastolikTansiyon>90:
            print("yuksek tansiyon")
        else:
            print("dusuk tansiyon")

hasta1=hasta("Rifki",64,150,80)
print(hasta1.risk())
hasta2=hasta("Cemile",54,130,78)
print(hasta2.risk())

class ogr:
    def __init__(self,ad,soyad,numara):
        self.ad=ad
        self.soyad=soyad
        self.numara=numara
        self.puan=[]
        self.devamDurumu=0
    def notEkle(self):
        puan1=int(input("not giriniz: "))
        self.puan.append(puan1)
    def ortalama(self):
        if len(self.puan)==0:
            print("henuz not girilmedi. ")
        else:
            ortalama=sum(self.puan)/len(self.puan)
            return ortalama

    def dvmDurumu(self):
        durum=input("derse girdi mi: ")
        if durum=="girdi":
            self.devamDurumu+=1
            return self.devamDurumu
        elif durum=="girmedi":
            self.devamDurumu+=0
            return self.devamDurumu
        else:
            print("gecersiz deger")
            return self.devamDurumu






ogr1=ogr("Buse","Tuglu",234)
print(ogr1.ortalama())
print(ogr1.notEkle())
print(ogr1.notEkle())
print(ogr1.ortalama())
print(ogr1.dvmDurumu())








