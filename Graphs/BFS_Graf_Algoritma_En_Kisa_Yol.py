graph = { 
    "A": ["B", "C"],
    "B": ["A", "C", "E", "D"],
    "C": ["B", "A", "E"],
    "D": ["B", "E", "F"],
    "E": ["C", "B", "D", "F"],
    "F": ["D", "E"]  
    }

def BFS_en_kisa(baslangic, son):
    ziyaret = []
    kuyruk = [[baslangic]]
    
    if baslangic == son:
        return
    
    while kuyruk:
        yol = kuyruk.pop(0)
        dugum = yol[-1]
        if dugum not in ziyaret:
            komsular = graph[dugum]
            for komsu in komsular:
                yeni_yol = list(yol)
                yeni_yol.append(komsu)
                kuyruk.append(yeni_yol)
                if komsu == son:
                    return yeni_yol
            ziyaret.append(dugum)
            #print(kuyruk)
    
result = BFS_en_kisa("A", "D")
print(result)   
    