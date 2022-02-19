# sıralı dizilirde çalışır.
# eleman sayısının karekökü kadar atlama yapmak en optimalidir.
# atlanıldığında ulaşılan sayı aranandan küçük olduğu sürece atlamaya devam edilir. iyice yaklaşıldığında linear search yapılır.
# complexity O (kök n)

import math

def jump_search(dizi,arananEleman):

    adim = int(math.sqrt(len(dizi))) # atlama periyodu
    onceki = 0 # 0. indeksten itibaren atlamaya başlanılacak.
    
    while dizi[min(adim,len(dizi))-1] < arananEleman: # onceki, dizinin boyutunu aştığında patlamasın diye sınır koydum.
        onceki = adim # onceki indis değerini saklıyorum.
        adim = adim + adim # atlanılan indis

    while dizi[onceki] < arananEleman: # aranan elemandan en fazla bir adim değeri kadar öncesine geliyorsun.
        onceki = onceki + 1 # sonra arananelemanın bir öncesine kadar liner artırarak geliyorsun.
    
    if dizi[onceki] == arananEleman:
        return onceki
    
    return -1

dizi = [3, 7, 10, 11, 12, 13, 19]

result = jump_search(dizi,3)

print(f"Aranan değerin indeksi {result}'dir.")