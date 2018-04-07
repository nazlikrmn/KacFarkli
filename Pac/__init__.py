def Ekle( oncekiDizi,basamak,eklenecek):
    oncekiDizi=oncekiDizi+eklenecek
    kacTane(oncekiDizi,basamak)
def kacTane( oncekidizi,bas):
    if len(oncekidizi) is int(bas):
        global toplam
        toplam=toplam+1
    else:
       sonHarf= oncekidizi[len(oncekidizi)-1]
       if sonHarf=='a':
           Ekle( oncekidizi,bas,'e')
       elif sonHarf=='e':
           Ekle(oncekidizi,bas,'a')
           Ekle(oncekidizi,bas,'i')
       elif sonHarf == 'i':
           Ekle(oncekidizi,bas, 'a')
           Ekle(oncekidizi,bas, 'e')
           Ekle(oncekidizi,bas, 'o')
           Ekle(oncekidizi,bas, 'u')
       elif sonHarf=='o':
           Ekle(oncekidizi,bas,'i')
           Ekle(oncekidizi,bas,'u')
       elif sonHarf=='u':
           Ekle(oncekidizi,bas,'a')

if __name__ == '__main__':
    sayi = input("Kac haneli için sonuc isteniyor?")
    dizi = ['a','e','i','o','u']
    toplam=0
    for a in dizi:
        kacTane(a,sayi)
    print(toplam)


