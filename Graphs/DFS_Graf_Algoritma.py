# Depth-first Search (DFS) Algoritması
# ağırlığın bir önemi yoktur.
# başlangıç noktasından gidebildiği yere kadar gider, gidecek yer kalmazsa geri döner başka yol arar.
# stack veri yapısını kullanır. BFS ise queue yapısını kullanıyordu.
# stack veri yapısında eleman kalmayınca algoritma sona erer.
# stack veri yapısını kullandığından recursive olarak da yazılması mümkündür.

graph = { 
    "A": ["B", "C"],
    "B": ["A", "C", "E", "D"],
    "C": ["B", "A", "E"],
    "D": ["B", "E", "F"],
    "E": ["C", "B", "D", "F"],
    "F": ["D", "E"]  
    }

def DFS_iterative(baslangic):
    
    ziyaret_edilenler=[]
    stack=[]
    stack.append(baslangic)
    output = []
     
    while len(stack):
        enTepe = stack[-1]
        stack.pop() # If the index is not given, then the last element is popped out and removed.
    
        if enTepe not in ziyaret_edilenler:
            ziyaret_edilenler.append(enTepe)
            output.append(enTepe)
      
        for komsu in graph[enTepe]:
            if komsu not in ziyaret_edilenler:
                stack.append(komsu)
    
    return output

result = DFS_iterative("A")
print(result)




def DFS_recursive(ziyaret, dugum):
    if dugum not in ziyaret:
        print(dugum)
        ziyaret.append(dugum)
        for komsu in graph[dugum]:
            DFS_recursive(ziyaret, komsu)

ziyaret = []
result = DFS_recursive(ziyaret, "A")

print(result)



