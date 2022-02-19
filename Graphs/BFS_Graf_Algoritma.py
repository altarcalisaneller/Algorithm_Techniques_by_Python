# breadth first search (BFS) 
# Ağırlıksız graflarda kullanılır.
# tüm komşulara gidilir. giderken kutruk veri yapısı kullanılır.kuyruğa eklenen düğüm ziyaret edilmiş sayılır. ilk önce komşular outout edilir.
# time complexty yüksektir.

graph = { 
    "A": ["B", "C"],
    "B": ["A", "C", "E", "D"],
    "C": ["B", "A", "E"],
    "D": ["B", "E", "F"],
    "E": ["C", "B", "D", "F"],
    "F": ["D", "E"]  
    }

def BFS(baslangic):
    visited = {}
    output = []
    kuyruk = []
    
    kuyruk.append(baslangic)
    if baslangic not in visited:
        visited[baslangic] = True
    while kuyruk: # kuyruk boş olmadıkça..
        x = kuyruk.pop(0) # kuyruğun en başındakini (0. index) listeden çıkartıyorum.
        output.append(x)
        for i in graph[x]:
            if i not in visited:
                kuyruk.append(i)
                visited[i] = True
    return output

result = BFS("A")
print(result)