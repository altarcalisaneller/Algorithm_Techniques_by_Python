# tek tek dizideki her elemana bakar.
# O(N)'dir.
# Sırasız dizilerde kullanılması mecburidir.

dizi = [3,1,78,3,59,23]

def linear_search(aranan, dizi):
    for i in range(0,len(dizi)):
        if dizi[i] == aranan:
            return i
    return -1

result = linear_search(78, dizi)

if result == -1:
    print("Aranan eleman " + "dizide bulunamadı.")
else:
    print("Aranan eleman " + str(result) + ".indekste" + " bulundu.")