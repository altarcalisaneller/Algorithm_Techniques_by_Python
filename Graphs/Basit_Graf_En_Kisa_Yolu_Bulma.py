graph = { 
    "A": ["B", "C"],
    "B": ["A", "C", "E", "D"],
    "C": ["B", "A", "E"],
    "D": ["B", "E", "F"],
    "E": ["C", "B", "D", "F"],
    "F": ["D", "E"]  
    }

def enKisaYoluBul(baslangic, hedef, yol=[]):
    
    yol = yol + [baslangic]
    
    if baslangic == hedef:
        return yol 
    
    enKisaYol = []
    
    for i in graph[baslangic]:
        if i not in yol: # aynı noktayı tekrar kullanmasın diye.yol burda geçtiğim düğümleri gösteriyor.
            yeniyollar = enKisaYoluBul(i, hedef, yol) # recursive bir şekilde devam ettiriyorum.
            if yeniyollar != None:
                if not enKisaYol or (len(yeniyollar) < len(enKisaYol)): # enkısayol dizisi boşsa veya yeniyollar enkisayol dan küçükse.
                    enKisaYol = yeniyollar
    return enKisaYol

result = enKisaYoluBul("A", "E")
print(result)