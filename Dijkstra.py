#用二维矩阵表示图，节点的值表示弧长，inf表示两点间不连通
inf=65536
\
    
adj_matrix=[[inf, 8 , 7 ,inf, 4 ,inf],
            [inf,inf, 5 ,inf,inf,inf],
            [inf,inf,inf,50 ,inf,inf],
            [inf,inf,inf,inf,inf,10 ],
            [inf,inf,inf,20 ,inf,60 ],
            [inf,inf,inf,inf,inf,inf]
            ]
#s为已经找到的最短路径，T为还未加入最短路径的节点的集合
T=[]
s=[]

def initial():
    i=0
    for vex in adj_matrix[0]:
        T.append([i,vex,[],0])#第三个元素的列表用于存储从源到该点经过哪些点，第4个元素标记该点是否加入到最短路径中
        i=i+1
    print T

      
def add_shortest_to_s():
    shortest=T[0]
    for node in T:
        if node[1]<shortest[1] and node[3]==0:
            shortest=node
    shortest[3]=1#将该点标记为已经加入最短路径
    shortest[2].append(shortest[0])
    s.append(shortest[:-1])
    
def renew():
    col=0
    line=s[-1][0]
    for vex in adj_matrix[line]:
        if s[-1][1]+vex<T[col][1]:
            T[col][1]=s[-1][1]+vex
            T[col][2]=T[line][2][:]
        col=col+1
            
def Dijkstra():
    initial()
    length=len(adj_matrix)
    i=0
    while(i<length-1):
        add_shortest_to_s()
        renew()
        i=i+1
        
   

Dijkstra()

print s

