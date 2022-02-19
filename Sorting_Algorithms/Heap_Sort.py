# complexity n.logn 
# heapify yapısında sol ve sağ çocuklara bakıp, root büyük olanla değiştirilir.
# max heap anlayışında en büyük sayı her zaman roota gelir. sonra o sayı dizinin en sağına konur ve hariç bırakılarak döngü yine başlar. 
# böylelikle her seferinde en büyük sayı root a yerleşir ve yukardaki işlemler tekrarlanır. 
# Fakat ağaç yapısında en büyüğü aradan çekip aldığında 
# (ki bu çekip alma önce ağacın en alttaki elemanı (önce sol kırılımın sağ yaprağı, son sol yaprağı sonra sağ kırılımın sağ yaprağı sonra sol yaprağı şeklinde devam ederek)
# ile root un yer değiştirmesi, sonra en aşağıya yerleşen eski root dizinin en sağına konularak ağaçtan çıkartılmasıyla olur) altında yapı bozulduğundan tekrar heapify fonksiyonunu çağırmak gerekiyor..
# bir de min heap yapısı var. onda da root a her zaman en küçük sayı yazılır. bu kod max heap anlayışına göre.

def max_heapify(dizi,boyut,rootIndex): 
        
    solCocuk_Index= (rootIndex * 2) + 1 # Ör: [2,4,5,1] dizisinde rootIndex 0. indeks ise, solçocuk 1 indeksteki, sağçocuk 2. indeksteki olacaktır. 
    sagCocuk_Index = (rootIndex * 2) + 2
    
    enBuyuk=rootIndex # rootIndex tekinin en büyük olduğunu kabul ediyorum.
    
    if  boyut > solCocuk_Index and dizi[solCocuk_Index] > dizi[rootIndex]  :
        enBuyuk = solCocuk_Index
    
    if  boyut > sagCocuk_Index and dizi[sagCocuk_Index] > dizi[enBuyuk]  :
        enBuyuk = sagCocuk_Index
    
    if enBuyuk !=rootIndex: # yukardaki işlemlerden birinin gerçekleşip gerçekleşmediğini kontrol ediyorum.
        dizi[rootIndex], dizi[enBuyuk] = dizi[enBuyuk], dizi[rootIndex] # koşul gerçekleşmişse swap işlemi yapıyorum.
        max_heapify(dizi, boyut, enBuyuk) # yer değiştirme yaptıkça heapify ı yeniden çağırıyorum.


def heap_sort(dizi): # esas sıralama işlemini bu fonksiyon yapacak.
    for i in range(len(dizi),-1,-1):
        max_heapify(dizi, len(dizi), i) # dizinin en büyük elemanı 0. indekse yerleşmiş olacak.     
      
    for i in range(len(dizi)-1,-1,-1):
        dizi[i], dizi[0] = dizi[0], dizi[i] # en başta olan en büyük sayıyı en sona attım.swap.
        max_heapify(dizi,i, 0) # yukardaki bütün işlem recursive olarak tekrarlandığında her tekrardaki en büyük sayı  en sağdan itibaren yerleşir.
    return dizi



dizi= [-1,7,-5,3,0]
result = heap_sort(dizi)
print(result)

# Not: python un default recursion limiti 1000 dir. yani bir fonksiyon kendini en fazla 1000 kere çağırabilir. bunu aşağıdaki kodla override ederek çözebiliriz.
# import sys
# x=1500
# sys.setrecursionlimit(x)
 