# dive and conquer şeklinde işleyen bir sıralama algoritması. Dizi 2 ye ayrılır. oluşan dizilerde, tek eleman kalana kadar 2'ye bölünmeye devam eder.
# dezavantajı space complexity.
# bir nevi ağacın dalları gibi bir şekil ortaya çıkar.  
# bölünme işlemi tamamlandıktan sonra bir araya getirme işlemine geçilir. Ağacın dalları yukarıya doğru bir araya getirilmeye başlanır.
# Fakat bir araya getirilirken her zaman soldizinin elemanı esas alınarak sağdaki dizinin elemanlarıyla karşılaştırılır, küçük olan birleşirilen diziye atanır. 
# Nihayetinde sıralı tek bir dizi oluşmuş olur.  
# time complexity O(n.logn)
# space complexity O(N)

def dive_merge(dizi):
    #print("Bölünün diziler: " + str(dizi))
    if len(dizi) > 1:
        mid = len(dizi) // 2
        solDizi = dizi[:mid]
        sagDizi = dizi[mid:]
        dive_merge(solDizi) # recursive metod
        dive_merge(sagDizi)
        mergeSort(dizi,solDizi,sagDizi)
        return dizi

def mergeSort(dizi,solDizi,sagDizi):
    i = 0 # bu değişken soldizi nin indisini tutsun
    j = 0 # bu değişken sagdizi nin indisini tutsun
    k = 0 # bu değişken birleştirdğimizi dizinin indisini tutsun
    
    while i < len(solDizi) and j < len(sagDizi):
        if solDizi[i] < sagDizi[j]:
            dizi[k] = solDizi[i] # küçük olanı birleştirdiğimiz dizinin ilk elemanı haline geliyor.
            i +=1 # bu elemanı kullandığım için sol dizinin bir sonraki elemanına geçiyorum.
        else:
            dizi[k] = sagDizi[j]
            j += 1 # bu elemanı kullandığım için sağ dizinin bir sonraki elemanına geçiyorum.
        k += 1 # k nın değerini artıyorum çünkü yukardaki döngüden her durumda 1 eleman birleşilen diziye gelecektir.
                # bu nedenle birlişen dizinin indisinide artırmam lazım.
    
    while i < len(solDizi): # sol ve sağ dizinin eleman karşılaştırmalarında her zaman ikisinden birinde sona bir veya daha fazla eleman kalacaktır. 
                            # bu kod bloğuyla sağ veya sol dizide kalan o elemanı/elemanları birleştirilmiş diziye aktarıyorum.
        dizi[k] = solDizi[i]
        i += 1
        k += 1
        
    while j < len(sagDizi):
        dizi[k] = sagDizi[j]
        j += 1
        k += 1
    
    #print("Birleştirilmiş diziler:" + str(dizi))
    

dizi = [0,7,-4,3,1,]
result = dive_merge(dizi)
print(result)

# Output:

# Bölünün diziler: [0, 7, -4, 3, 1, 9]
# Bölünün diziler: [0, 7, -4]
# Bölünün diziler: [0]
# Bölünün diziler: [7, -4]
# Bölünün diziler: [7]
# Bölünün diziler: [-4]
# Birleştirilmiş diziler:[-4, 7]
# Birleştirilmiş diziler:[-4, 0, 7]
# Bölünün diziler: [3, 1, 9]
# Bölünün diziler: [3]
# Bölünün diziler: [1, 9]
# Bölünün diziler: [1]
# Bölünün diziler: [9]
# Birleştirilmiş diziler:[1, 9]
# Birleştirilmiş diziler:[1, 3, 9]
# Birleştirilmiş diziler:[-4, 0, 1, 3, 7, 9]