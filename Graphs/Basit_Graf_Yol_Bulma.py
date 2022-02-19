graph = { 
    "A": ["B", "C"],
    "B": ["A", "C", "E", "D"],
    "C": ["B", "A", "E"],
    "D": ["B", "E", "F"],
    "E": ["C", "B", "D", "F"],
    "F": ["D", "E"]  
    }

def yolBul(baslangic, hedef, yol=[]):
    
    yol = yol + [baslangic]
    
    if baslangic == hedef: # aşağıdaki i değeri her seferinde baslangıcın yerini alıyor. Hedefle aynı olduğundan iş bitiyor.base case.
        return yol
    
    for i in graph[baslangic]:
        if i not in yol: # aynı noktayı tekrar kullanmasın diye. yol burda geçtiğim düğümleri gösteriyor.
            return yolBul(i, hedef, yol) # recursive bir şekilde devam ettiriyorum.
            
    return None

yol = yolBul("B", "F")
print(yol)





