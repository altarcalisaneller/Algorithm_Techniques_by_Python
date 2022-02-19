# time complexity O(N**2)
# space complexity O(1)


def insertion_sort(dizi): # araya sokma algoritması
    for i in range(1,len(dizi)): # algoritma gereği dizinin 1. indeksindeki değerden başlanıyor. 0. indekse sahip olan zaten sıralı kabul ediliyor.
        key = dizi[i] # bunun değerini sonradan swap ile değiştireceğim için burada geçici olarak değerini bir yerde saklamak istiyorum.
        j = i -1 # algortma gereği i değeri bir önceki indeks değeriyle karşılaştırılacağından j yi i-1 olarak belirliyorum.
        while key < dizi[j] and j >= 0 : # j'nin - değer almasına izin verirsem dizi sıralandıktan sonra sonsuz döngüye girer. O nedenle istemiyorum.
            dizi[j+1]  = dizi[j] # while daki koşul gerçekleştiğinden j nin değerini bir sağa kaydırıyorum.
            j = j-1 # j nin değerini bir azaltıyorum ki bir sonraki satırdaki atama işlemi doğru gerçekleşsin, üzerine yazmasın.
        dizi[j+1] = key # key değerini sola kaydırmış oldum.

    return dizi

dizi = [8,1,7,6,2,0]
result = insertion_sort(dizi)
print(result)

            