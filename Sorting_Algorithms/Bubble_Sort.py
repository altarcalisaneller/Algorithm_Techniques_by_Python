# time complexity O(N**2)
# space complexity O(1)
# ilk elemanı sağındakiyle karşılaştırarak 

def BubleSort(dizi): # BubleSort algoritması küçükten büyüğe sıralama yapmak için kulanılır. (n.(n-1))/2 kadar döner. 
    for i in range(len(dizi)):
        #flag = False # to optimaze Buble_Sort
        for j in range(len(dizi)-1-i): # ilk döndüğünde en büyük elamanı en sona kadar götürür. Sonraki dönüşte kalanlardan en büyüğünü sona götürür. böyle devam eder.
            if dizi[j] > dizi[j+1]:
                dizi[j], dizi[j + 1] = dizi[j + 1], dizi[j] # swap işlemi yapılır.
        #        flag = True # to optimaze Buble_Sort
        #if flag == False: # to optimaze Buble_Sort
        #    break
    return dizi

result = BubleSort([1,0,12])
print(result)