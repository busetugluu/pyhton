print("hi guys")

print("Benim adim {}" .format('Buse'))
print("Benim adim {}, yasim {}" .format('Buse',19) )
print ("Benim adim {1},yasim {0}" .format('Buse',19))
print("Benim adim {ad} , yasim {yas}".format(ad='Buse',yas=19))

sayi=10
print(sayi)

sayi=sayi+5
print(sayi)

_=20
print(_)

#list -> [1,2,true,'a',2] aynı elamn birden fazla kez var olabilir
#set -> {1,2,true,'a'} aynı eleman birden fazla kez varsa sadece bir kez varmış gibi yapıcak
#dict -> {'isim:'buse , 'yas':19} class'a benziyor
#tup -> (1,2,True) değerler değiştirilemiyor

type(3)
print(3*4)


buse="PYTHON "
print(buse)
print(buse[0])
print(buse[2:])
print(buse[2:4])
print(buse[:3])
print(buse[::2]) #ikişerli atlıyor
print(buse[0:5:3]) #0'dan 5'e üçerli atlıyor
print(len(buse)) #uzunluğu buluyor
print(buse+"ogren ")
buse=buse+ "ogren "
print(buse*5)
a='Python Programlama Dili'
print(a[7:17:2])
print(a[::-1]) #tersten yazar
print(a[::1]) # belki  bu tarz sorarmış
x='Merhaba'
print(x[::-2])
print(x+a)

'''
LİST
listeleme,listelerde indexleme,ekleme,silme,çıkarma
'''

boy1=1.66
boy2=1.76
boy3=1.80

boy=[1.66,1.76,1.80]

boys=["ayse",1.66,"fatma",1.76,"ahmet",1.80]


fiyatListesi=['muz',90,'elma' ,45,'armut',50]
print(fiyatListesi)

boys2=[["ayse",1.66],["fatma",1.76],["ali",1.80]]
print(boys2)

#boş liste oluşturma
x=[]
print(x)
#ikinci yol
xx=list()
print(xx)

##listelerde indexleme işlemleri
print(boy)
print(boy[0])
print(boy[1])
print(boy[2])

print(boys2[1])
print(boys[2:4])
print(len(boys))
print(boys[len(boys)-1])
print(boys[1::2])

meyve=fiyatListesi[::2]
print(meyve)
fiyat=fiyatListesi[1::2]
print(fiyat)

w=fiyat[0]
y=fiyat[1]
r=fiyat[2]
fiyatToplam=w+y+r
print(fiyatToplam)

print(len(boys2))

print(boys2[0][0])
print(boys2[2][1])

height=boys
print(boys)

#listelerde ekleme işlemi
height=height+["esma",1.70]
print(height)

print(boys)

#listelerde silme işlemi

del(height[5:])
print(height)

a="merhaba"
print(a[-1:-2:-1])

Kelime="matematik"
gizli=Kelime[0]+Kelime[3]+Kelime[2]+Kelime[5]
print(gizli)

kelime="susam"
sifre=kelime[::-1][2:]
print(sifre)
