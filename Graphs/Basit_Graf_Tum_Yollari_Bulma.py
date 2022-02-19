graph = { 
    "A": ["B", "C"],
    "B": ["A", "C", "E", "D"],
    "C": ["B", "A", "E"],
    "D": ["B", "E", "F"],
    "E": ["C", "B", "D", "F"],
    "F": ["D", "E"]  
    }

def tumYollariBul(baslangic, hedef, yol=[]):
    
    yol = yol + [baslangic]
    
    if baslangic == hedef:
        return [yol] # her bir yol liste şeklinde ayrı ayrı gözüksün diye [] içinde aldım.
                     # aşağıdaki i değeri her seferinde baslangıcın yerini alıyor.base case.
    else:
        yollar = []
        
        for i in graph[baslangic]:
            if i not in yol: # aynı noktayı tekrar kullanmasın diye.yol burda geçtiğim düğümleri gösteriyor.
                yeniyollar = tumYollariBul(i, hedef, yol) # recursive bir şekilde devam ettiriyorum.
                for yeniyol in yeniyollar:
                    yollar.append(yeniyol) # her bir yolu yollar dizisine aktarıyorum.
        else: # The else keyword in a for loop specifies a block of code to be executed when the loop is finished.
            return yollar

result = tumYollariBul("D", "F")
print(result)