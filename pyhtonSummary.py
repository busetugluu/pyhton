#STRİNGLER
a="kahve"
print(a[0]) # k

#[başlama indexi : bitiş indexi : adım degeri]

b="pyhton programlama dili"
print(b[4:10]) #4. indexten 10. indexe kadar (10 dahil değil) yazdırır
#on pro
print(b[:10]) #baslangıc degeri belirtilmemişse bastan baslar
#pyhton pro
print(b[4:])#bitis degeri belirtilmemişse sona kadar alır
#on programlama dili
print(b[:]) # iki deger de belirtilmemişse bastan sona hepsini alır
#pyhton programlama dili
print(b[:-1]) #son karaktere kadar alır son karakteri almaz
#pyhton programlama dil
print(b[::1]) #bastan sona her adımda 1 karakteri alır bu da hepsi demek
#pyhton programlama dili
print(b[::2]) #bastan sona her adımda 2 deger atlaya atlaya karakteri alır
#pho rgalm ii
print((b[4:12:3])) #4. indexten 12. indexe üçer üçer atlayarak alır
#opg
print(b[::-1]) #baştan sona alır ama ters yazdırır
#ilid amalmargorp nothyp
print(b[::-2]) #baştan sona alır 2 adımda bir karakteri tersten yazdırır
#ii mlagr ohp
print(len(b)) #len fonk stringin uzunlugunu verir
#23

#LİSTELER

boy=[["ali",170],["veli",167],["selin",154]]

#string ifadeyi list() ile listeye cevirebiliriz
c="merhaba"
d=list(c)
print(d,type(c),type(d))
#['m', 'e', 'r', 'h', 'a', 'b', 'a'] <class 'str'> <class 'list'>

#Listeleri parçalama
fam2=['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]
print(fam2[3:5]) #3. indexten 5. indexe kadar alır (5 dahil dğeil)
#[1.68, 'mom']
print(fam2[:4]) #baştan başlar 4. indexe kadar (4 dahil değil)
#['liz', 1.73, 'emma', 1.68]
print(fam2[5:]) #5'ten baslar sonuna kadar gider
#[1.71, 'dad', 1.89]
print(fam2[:]) #baştan sona kadar alır
#['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]


#Listelerin listsini parçalama
print(boy)
#[['ali', 170], ['veli', 167], ['selin', 154]]
print(boy[0])
#['ali', 170]
print(boy[2][0]) #boy listesinin 3. elemanının ilk elemanı
#selin
print(boy[2][:]) #boy listesinin 3. elemanının tüm elemanları
# ['selin', 154]

#Liste ögelerini değiştirmek

print(fam2)
#['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.89]
fam2[7]=1.72
print(fam2)
#['liz', 1.73, 'emma', 1.68, 'mom', 1.71, 'dad', 1.72]
fam2[0:2]=["lisa",1.74]
print(fam2)
#['lisa', 1.74, 'emma', 1.68, 'mom', 1.71, 'dad', 1.72]

#öge ekleme
fam2=fam2+["me",1.70]
print(fam2)
#['lisa', 1.74, 'emma', 1.68, 'mom', 1.71, 'dad', 1.72, 'me', 1.7]

#listeden ögeler silmek
del(fam2[3]) #fam2'nin 3. indexini siler
print(fam2)
#['lisa', 1.74, 'emma', 'mom', 1.71, 'dad', 1.72, 'me', 1.7]

#FONKSİYONLAR
print(type(fam2)) #türünü verir
#<class 'list'>

print(boy)
#[['ali', 170], ['veli', 167], ['selin', 154]]
print(max(boy)) #listedeki max değeri verir

sayi=[1,2,3,4]
print(max(sayi))
#4
print(len(sayi))
#4

print(round(1.68,1)) #birincisi, yuvarlamak istediğiniz bir sayı ve 
# ikincisi, yani noktadan sonra kaç basamak tutmak istediğiniz.
#1.7
print(round(1.68)) #eger ikinci girdiyi yazmazsak fonk en yakın integer sayıya yuvarlar
#2

sayi2=[43,6,3,7654,32,65,32,54]
print(sorted(sayi2)) #listeyi kucukten buyuge dogru sıralar
#[3, 6, 32, 32, 43, 54, 65, 7654]

print(sorted(sayi2,reverse=True)) #reverse normalde false olarak kabul edilir.
# True olarak değiştirililrse buyukten kucuge dogru sıralama yapar
#str ifadelerde de alfabetik bir sıralama olusturur.
#[7654, 65, 54, 43, 32, 32, 6, 3]


#Metodlar

sister="liz"
height=1.70

help(sister.capitalize())
print(sister.capitalize()) #dizenin ilk harfini büyük harfe cevirir
#Liz

print(sister.replace("z","sa")) #değişim için kullanılır. eski, yeni
#lisa

youtube="bu video cok kotu"
y=youtube.replace(" ","_")
print(y)
#bu_video_cok_kotu

print(youtube.split()) #string ifadeyi parcalar. boşluğa göre parcalanır
#['bu', 'video', 'cok', 'kotu']
print(youtube.split("u")) #u herfine göre böler
#['b', ' video cok kot', '']

place="kutuphane"
print(place.upper()) #string ifadenin tum harflerini büyütür
#KUTUPHANE
print(place.count("u")) #place değiskenindeki ifadenin içinde kaç kez u geçtiğini sayar
#2

print(place.isupper()) #place değişkenindeki ifade büyük harf mi diye sorgulamak için
#False
print(place.islower()) #place değişkenindeki ifade küçük harf mi diye sorgulamak için
#True
print(place.isnumeric()) #place değişkenindeki ifade numerik mi diye sorgulamak için
#False


kelime=input("bir kelime giriniz: ")
harf=input("sayisini bulmamizi istediginiz bir harf giriniz: ")
sonuc=kelime.count(harf)
print(sonuc)


print(fam2)
#['lisa', 1.74, 'emma', 'mom', 1.71, 'dad', 1.72, 'me', 1.7]

print(fam2.index("mom")) #mom değişkeninin kaçıncı sırada oldugunu gosterdi
#3
print(fam2.count("dad")) #dad değişkeni var mı diye kontrol etti
#1

#listelerde replace metodu kullanılmaz

fam2.append("you")#listenin sonuna you değişkenini ekler
print(fam2)
#['lisa', 1.74, 'emma', 'mom', 1.71, 'dad', 1.72, 'me', 1.7, 'you']

fam2.pop() #içine bir şey yazmazsak son elemanı siler
print(fam2)
#['lisa', 1.74, 'emma', 'mom', 1.71, 'dad', 1.72, 'me', 1.7]

fam2.remove("mom") #içine yazdıgım değişkeni siler
print(fam2)
#['lisa', 1.74, 'emma', 1.71, 'dad', 1.72, 'me', 1.7]

fam2.reverse() #listedeki ögelerin sırasını tersine cevirir
print(fam2)
#[1.7, 'me', 1.72, 'dad', 1.71, 'emma', 1.74, 'lisa']

areas=[11.25, 18, 20, 10.175, 9.50]
areas.insert(0,30) # 0. indisine 30 değerinii ekler
print(areas)
#[30, 11.25, 18, 20, 10.175, 9.5]

x=[1,2,3,4]
y=x.copy() #listeyi kopyalar
print(y)
#[1, 2, 3, 4]

#x'ten bir eleman sildiğimizde y'den silinmez
x.remove(1)
print(x)
#[2, 3, 4]
print(y)
#[1, 2, 3, 4]

print(areas)
#[30, 11.25, 18, 20, 10.175, 9.5]
print(min(areas)) #areas listesindeki min degeri verir
#9.5
print(areas.index(min(areas))) #min degerin index numarasını verir
#5
#min metodunu kullanabilmemiz için listedeki tüm elemanlar sayısal veri olmalı

areas.sort() #kucukten buyuge sıralar
print(areas)
#[9.5, 10.175, 11.25, 18, 20, 30]

areas.clear() #listenin içini temizler. boş hsle getirir
print(areas)
#[]

data=[]
s1=int(input('veriyi giriniz:'))
data.append(s1)
s2=int(input('veriyi giriniz:'))
data.append(s2)
s3=int(input('veriyi giriniz:'))
data.append(s3)
print(data)
#[5342, 542, 1434]
data[1]=5
print(data)
#[5342, 5, 1434]

#KARSILASTIRMA OPERATORLERİ
# < , <= , > , >= , == , !=
#MANTIKSAL BAGLACLAR
#and, or, not

x=12
print(x>10 and x<15) #True
print(x>10 and x<9) #False
print("********")
print(x>10 or x<8) #True
print(x>10 or x<15) #True
print("*********")
print(2==2) #True
print(not (2==2)) #False
print("************")

#KOSULLU DURUMLAR
#if kosul:
#   yapilacak islem
#else: (if saglanmazsa)
#   yapilacak islem

#DONGULER
#for
print(boy)
#[['ali', 170], ['veli', 167], ['selin', 154]]
for i in boy:
    print(i)
#['ali', 170]
#['veli', 167]
#['selin', 154]
print("******************")
boy2=[1.73,1.68,1.71,1.89]
toplam=0
for i in boy2:
    toplam+=i
    print(f"toplam: {toplam}")
    print(f"ortalama : {toplam/len(boy2)}")
#toplam: 1.73
#ortalama : 0.4325
#toplam: 3.41
#ortalama : 0.8525
#toplam: 5.12
#ortalama : 1.28
#toplam: 7.01
#ortalama : 1.7525

print("**********************")
#varyans hesabı
top1=0
top2=0
n=len(boy2)
for i in boy2:
    top1+=i
    top2+=i**2
ort=top1/n
varyans=top2/n-ort**2
print(f"ortalama: {ort:.2f}, standart sapma: {varyans**0.5:.2f}")
#ortalama: 1.75, standart sapma: 0.08

#boy2 listesindeki elemanları standartlaştırın:
boy2_s=[]
for i in boy2:
    z=(i-ort)/(varyans**0.5)
    print(z)
    #-0.2765632877383527
    #-0.8911483716013602
    #-0.5223973212835556
    #1.6901089806232685
    boy2_s.append(round(z,2))
print(boy2_s)
#[-0.28, -0.89, -0.52, 1.69]

liste=list(range(21))
print(liste)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
cift=[]
tek=[]
ciftTop=0
tekTop=0
for i in liste:
    if i%2==0:
        cift.append(i)
        ciftTop+=i
    else:
        tek.append(i)
        tekTop+=i
print(f"cift listesi: {cift} \nciftlerin toplami: {ciftTop}")
print(f"tek listesi: {tek} \nteklerin toplami: {tekTop}")
#cift listesi: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#ciftlerin toplami: 110
#tek listesi: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
#teklerin toplami: 100

for i in "family":
    print(i)
'''
f
a
m
i
l
y
'''
for sayi in range(1,20):
    print("* "*sayi)
'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * * * 
* * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * * 
* * * * * * * * * * * * 
* * * * * * * * * * * * * 
* * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * 
'''
#while döngüsü kosul dogru oldugu surece calısmaya devam eder
'''while kosul:
        yapilacak islem
'''
x=1
while x<4:
    x+=1
    print(x)
#2
#3
#4
print("*********")

'''
say=int(input("bir sayi giriniz: "))
top=0
while say!=0:
    top+=say
    say=int(input("bir sayi giriniz: "))
print(top)
'''
#break : çalışmayı durdurur.
i=0
while i<20:
    if i==10:
        break
    print(i)
    #1 2 3 4 5 6 7 8 9
    i+=1

#while True: sonsuz döngüdür

#continue Döngü herhangi bir yerde ve herhangi bir zamanda continue ifadesiyle
#karşılaştığı zaman geri kalan işlemlerini yapmadan direkt bloğunun başına döner

liste2 = [1,2,3,4,5,6,7,8,9]

for i in liste2:
    if(i==3 or i==5):
        continue
    print("i: ",i)
'''
i:  1
i:  2
i:  4
i:  6
i:  7
i:  8
i:  9
'''


bakiye=1000
while True:
    islem=int(input("1- bakiye sorgulama\n"
                "2- para yatırma\n"
                "3- para cekme\n"
                "4- 'q' tusu ile programdan cıkma:"))
    if str(islem)=="q":
        print("programdan cıkılıyor..")
        break
    else:
        if islem==1:
            print(f"bakiyeniz: {bakiye}")
            continue
        elif islem==2:
            miktar=int(input("yatırılıcak miktari giriniz: "))
            bakiye+=miktar
            print(f"guncel bakiyeniz: {bakiye}")
            continue
        elif islem==3:
            cekMiktar=int(input("cekmek istediginiz tutarı giriniz: "))
            bakiye-=cekMiktar
            print(f"guncel bakiyeniz: {bakiye}")
            continue
        else:
            print("gecersiz islem")
            break

#iç içe döngüler

for i in range(0,11):
    for j in range(0,11):
        print(f"{i}*{j}={i*j}")

    print("-------"*10)

veri=[
    [12, '-', 18],
    [10,14,'-'],
    ['-',13,15]
]

for i in range(0,len(veri)):
    s=0
    for j in range(0,len(veri[i])):
        if veri[i][j]=='-':
            s+=1
    print(f"{i+1}. satırdaki kayıp gözlem sayisi: {s}")
#1. satırdaki kayıp gözlem sayisi: 1
#2. satırdaki kayıp gözlem sayisi: 1
#3. satırdaki kayıp gözlem sayisi: 1
print("**********")
veri2 = [
    [3, 5, 7],
    [2, 4, 6],
    [1, 3, 5]
 ]
for i in range(0,len(veri2)):
    t=0
    for j in range(0,len(veri2[i])):
        t+=veri2[i][j]
    print(f"{i+1}. satırın toplami: {t}")
#1. satırın toplami: 15
#2. satırın toplami: 12
#3. satırın toplami: 9

print("*********")

p=0
for k in range(0,len(veri2)):
    for l in range(0,len(veri2[k])):
        p+=veri2[k][l]
print(f"tüm satırlların toplami: {p}")
#tüm satırlların toplami: 36

#zip fonksiyonu
asd=[1,2,3]
asd2=['a','b','c']

for i,j in zip(asd,asd2):
    print(i,j)
'''
1 a
2 b
3 c
'''
print("*********")
boy=[1.70,1.82, 1.60, 1.75, 1.68]
kilo = [65, 85, 55, 70, 60]
id_no = [1, 2, 3, 4, 5]
for i,j,k in zip(id_no,boy,kilo):
    vki=k/j**2 #kilo / boyun karesi
    print(f"{i}. kişinin vki: {vki:.2f}")
'''
1. kişinin vki: 22.49
2. kişinin vki: 25.66
3. kişinin vki: 21.48
4. kişinin vki: 22.86
5. kişinin vki: 21.26
'''

#KARAR YAPILARI
# if koşul_1:
#   yapılacak işlem
# elif koşul_2:
#   yapılacak işlem
#elif koşul_3:
#    yapılacak işlem
#else:
#    yapılacak işlem
print("***********")

no=int(input("bir sayi giriniz: "))
if no==0:
    print("sayi sifirdir.")
elif no>0 :
    print("sayi pozitiftir")
else:
    print("sayi  negatiftir")

print("************")

sayi3=int(input("bir sayi giriniz: "))
sayi4=int(input("bir sayi giriniz: "))
islemler=int(input("1- toplama\n"
                   "2-cıkarma\n"
                   "3-carpma\n"
                   "4-bölme\n"))

if islemler==1:
    print(f"sayıların toplamı : {sayi3+sayi4}")
elif islemler==2:
    print(f"sayıların farkı: {sayi3-sayi4}")
elif islemler==3:
    print(f"sayıların carpımı: {sayi3*sayi4}")
elif islemler==4:
    print(f"sayıların oranı: {sayi3/sayi4}")
else:
    print("gecersiz islem")

print("**********")

b1=float(input("boyunuzu metre cinsinden giriniz: "))
k1=float(input("kilonuzu giriniz: "))
vki=k1/b1**2

if vki<18.5 :
    print("zayif")
elif vki>18.5 and vki<25:
    print("normal")
elif vki>25 and vki<30:
    print("fazla kilolu")
elif vki>30:
    print("obez")


s1=15
s2=18
s3=20
enb=s1
if s2>enb:
    enb=s2
if s3>enb:
    enb=s3
print(f"en buyuk sayi : {enb}")
#en buyuk sayi : 20

print("**********")
#Tek satırda if-else yapısı
#degisken=sonuc1 if kosul else sonuc2
# Eğer koşul doğruysa değer değişkenine sonuc1, koşul doğru değilse değer
#değişkenine sonuc2 atanır.


puan=int(input("notunuz: "))
sonuc= "gectiniz" if puan>=50 else "kaldiniz"
print(sonuc)

s1=int(input("bir sayi giriniz: "))
durum=s1**2 if s1%2==0 else s1**3
print(durum)

s2=int(input("bir sayi giriniz: "))
s3=int(input("bir sayi giriniz: "))
enb1=s2 if s2>s3 else s3
print(enb1)


#değişken=sonuc1 if koşul1 else sonuc2 if koşul2 else sonuc3

num=int(input("bir sayi giriniz: "))
tm="sayi 0'dir" if num==0 else "sayi cifttir" if num%2==0 else "sayi tektir"
print(tm)

#in operatörü: öge in koleksiyon
meyveler=["armut","mandalina","kivi"]
print("elma" in meyveler) #false
print("kivi" in meyveler) #true
print("*******")
isim="Buse"
isim=isim.lower()
print("b" in isim) #true
print("U" in isim) #false

bolge=input("bir bölge giriniz: ")
if bolge in ["marmara","akdeniz","karadeniz"]:
    print("bu bolgenin denize kıyısı vardır")
else:
    print("bu bolgenin denize kıyısı yoktur")

#LİST COMPREHENSİON
num1=[1,2,3,4]
num2=[]
for i in num1:
    num2.append(i+1)
print(num2) #[2, 3, 4, 5]

# tek satırda for dongusu  [expression for iteratör in iterable]
num3=[i+1 for i in num1]
print(num3)
#[2, 3, 4, 5]

nlist=[]
for i in range(0,11):
    nlist.append(i)
print(nlist)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nlist2=[i for i in range(0,11)]
print(nlist2)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

kare=[i**2 for i in range(0,11)]
print(kare)
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

kare1=[i**2 for i in range(0,11) if i%2==0]
print(kare1)
#[0, 4, 16, 36, 64, 100]

kare2=[i**2 if i%2==0 else 0 for i in range(0,11)]
print(kare2)
#[0, 0, 4, 0, 16, 0, 36, 0, 64, 0, 100]

fellowship=["frodo", "samwise", "merry", "aragorn",
            "legolas", "boromir", "gimli" ]
fellowship2=[i for i in fellowship if len(i)>=7]
print(fellowship2)
#['samwise', 'aragorn', 'legolas', 'boromir']

isimler = ["Ali", "Zeynep", "Ece", "Murat", "aslı"]
isimler2=[isimler[i] for i in range(len(isimler)) if isimler[i][0].lower()=='a']
print(isimler2)
#['Ali', 'aslı']

a=input("bir kelime giriniz: ")
print(a[0:1])
print(a[-1:-2:-1])
print(a[-1:-2])