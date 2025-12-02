#FONKSİYON OLUŞTURMA
def kare_al(sayi):
    return(sayi**2)
a=kare_al(5)
print(a)
print("*************")
def ciftMi(sayi):
    if sayi%2==0:
        return("sayi cift")
    else:
        return("sayi tek")
b=ciftMi(3)
print(b)
print("**********")
def us(sayi1,sayi2):
    sonuc1=sayi1**sayi2
    sonuc2=sayi2**sayi1
    return sonuc1,sonuc2
c=us(3,2)
print(c)
print("**********")
def vki2(boy,kilo):
    if boy<3:
        vki=kilo/boy**2
        return vki
    else:
        boy=boy/100
        vki=kilo/boy**2
        return vki

e=vki2(170,60)
print(e)
print("*********")
kilo=[50,45,70,90]

def ortalama(dizi):
    toplam=0
    for i in dizi:
        toplam=toplam+i
    ortalama=toplam/len(dizi)
    return ortalama

f=ortalama(kilo)
print(f)
print("********")
def varyans(s):
    kare=0
    for i in s:
        kare=kare+i**2
    kareOrt=kare/len(s)
    ortKare=ortalama(s)**2
    varyans=kareOrt-ortKare
    return varyans
g=varyans(kilo)
print(g)

h=[2,2,2,2]
print(varyans(h))

def varyans2(s):
    hesap=[(i-ortalama(s))**2 for i in s]/len(s)
    return hesap

def korelasyon(s,p):
    toplam=0
    n=len(s)
    for i,j in zip(s,p):
        toplam=toplam+(i-ortalama(s))*(j-ortalama(p))
    r=toplam/((n**2)*varyans2(s)*varyans2(p))**0.5
    return r
s=[10,20,30]
p=[10,20,30]
print(korelasyon(s,p))


#MODÜL
import math
print(dir(math))
print("*****")
math.factorial(5)
math.ceil(4.3)

import hesaplama as hs
print(dir(hs))
print(hs.toplama(3,4))
print(hs.cıkarma(3,4))
print(hs.carpma(3,4))
print(hs.bolme(3,4))

import istatistik as ist
print(dir(ist))
