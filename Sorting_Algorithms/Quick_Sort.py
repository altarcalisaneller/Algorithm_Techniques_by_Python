# O(log n) speed is a best-case/average time, in worst case scenarios it can be O(n**2) depending on the implementation.
# divide and conquer algoritmalarından biridir. dezavantajı yanlış pivot seçildiğinde recursion fazla olur.
# diziden bir eleman istenilen bir elemanı pivot seçilir.
# i ve j counter ı kullanılır. i -1 den j 0 dan başlatılır.
# pivotun solunda daha küçük sayılar, sağında daha büyük sayılar sıralanır.
# j nin gösterdiği sayılı ile pivot karşılaştırılır.
# eğer j daha büyük ise sadece j nin değeri artırılır. daha küçük ise, i nin değeri 1 artırılır ve yeni i ile j nin değerleri yer değiştirilir ve j nin değeri 1 artırılır.
# j counterı pivota geldiğinde işlem biter ve ek bir işlem yapılır. pivot, i nin gösterdiği yerin bir sağına (yani i+1 e) getirilir.
# pivotun solunda pivottan daha küçük değerler, sağında daha büyük değerler oluşmuş oldu.
# solundaki ve sağındaki parçalar üzerinde ayrı ayrı yukarıdaki işlemler yapılır.

def parcalaraAyir(dizi, solIndis,sagIndis):
    i = solIndis-1 
    pivot=dizi[sagIndis]
    
    for j in range(solIndis,sagIndis):
        if dizi[j] <= pivot:
            i +=1 
            dizi[i], dizi[j] = dizi[j], dizi[i] 
    dizi[i+1], dizi[sagIndis] = dizi[sagIndis], dizi[i+1]
    return i+1 # pivotun yeni yerinin indisi

def quicksort(dizi, solIndis, sagIndis):
    if solIndis < sagIndis: # base case
        pivot = parcalaraAyir(dizi, solIndis, sagIndis)
        quicksort(dizi, solIndis, pivot-1) # pivotun solundaki parçayı sıralamak için recursive işlem yapılır.
        quicksort(dizi, pivot+1, sagIndis) # pivotun sağındaki parçayı sıralamak için recursive işlem yapılır.
    return dizi

dizi = [-2,0,-1,6,2]
result = quicksort(dizi, 0, len(dizi)-1)
print(result)