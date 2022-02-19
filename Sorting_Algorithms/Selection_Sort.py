# selection sort algoritmasında 0. indeksten başlanarak sağa doğru dizideki en küçük sayı bulunur ve en başa atılır. 
# Sonra bir sonraki indise geçer ve yine dizinin geri kalanındaki en küçük sayıyı bulur ve bu sefer en baştan bir sonraki indise atar.
# buble sort'taki gibi anı sayı için sürekli bir yer değiştirme yapılmaz. dizi taranır ve küçük olduğuna emin olunduktan sonra
# yer değiştirme işlemi(swap) işlemi yapılır.
# (n.(n-1))/2 kadar döner.
# time complexity O(N**2)
# space complexity O(1) 


def SelectionSort(liste):
        
    for i in range(0,len(liste)):
        indexof_min_value = i
        for j in range(i+1,len(liste)):
            if liste[j] < liste[indexof_min_value]:
                indexof_min_value = j
        
        liste[i], liste[indexof_min_value] = liste[indexof_min_value], liste[i]
    return liste
             

liste= [2,3,4,1,-1,2]

result = SelectionSort(liste)
print(result)


            
    