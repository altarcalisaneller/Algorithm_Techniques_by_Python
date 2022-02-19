# sıralı dizilerde kullanılabilir.
# dizinin orta elemanını bul.
# aranan sayı ortancadan büyük mü küçük mü bakılır.
# aranan hangi taraftaysa o parça alınır ve onun ortası bulunarak aynı işlemler tekrarlanır.

def binary_search(list,number): # bir dizi içinde string veya sayı aramak için kullanılır.
    low=0
    high=len(list)
    while low <= high:
        mid = (low+high)// 2 # metodun mantığı dizinin boyutunu her seferinde 2 ye bölerek aranan ifadeyi o bölüm içinde aramaktır.
        guess=list[mid]
        if guess==number:
            return mid  # bulunan ifadenin indeks numarasını vericektir.
        elif guess < number:
            low = mid +1
        else:
            high = mid -1
    return None
        
            
result = binary_search([1,5,8,9,90], 5)
print(f"Aranan değerin indeksi {result}'dir.")

