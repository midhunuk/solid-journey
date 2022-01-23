import queue

def findConnectionLevel(vertices, Amat, personX, personY):
    level = {}
    for i in range(vertices):
        level[i] = -1
    q = queue.Queue()
    
    level[personX] = 0
    q.put(personX)
    
    while(not q.empty()):
        j = q.get()
        for i in range(vertices):
            if (Amat[j][i] == 1 and level[i] == -1):
                level[i] = level[j] + 1
                q.put(i)
                if i == personY:
                    return level[i]    
    return 0

inp = ["0 1 1 0 0 0 0",
"1 0 1 1 1 1 0",
"1 1 0 1 1 1 0",
"0 1 1 0 1 0 0",
"0 1 1 1 0 1 0",
"0 1 1 0 1 0 1",
"0 0 0 0 0 1 0"]

Amat = []
for i in inp:
  row = [int(item) for item in i.split(" ")]
  Amat.append(row)

print(findConnectionLevel(7, Amat, 6, 0))