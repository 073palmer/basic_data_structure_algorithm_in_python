#�ö�ά�����ʾͼ���ڵ��ֵ��ʾ������inf��ʾ����䲻��ͨ
inf=65536
\
    
adj_matrix=[[inf, 8 , 7 ,inf, 4 ,inf],
            [inf,inf, 5 ,inf,inf,inf],
            [inf,inf,inf,50 ,inf,inf],
            [inf,inf,inf,inf,inf,10 ],
            [inf,inf,inf,20 ,inf,60 ],
            [inf,inf,inf,inf,inf,inf]
            ]
#sΪ�Ѿ��ҵ������·����TΪ��δ�������·���Ľڵ�ļ���
T=[]
s=[]

def initial():
    i=0
    for vex in adj_matrix[0]:
        T.append([i,vex,[],0])#������Ԫ�ص��б����ڴ洢��Դ���õ㾭����Щ�㣬��4��Ԫ�ر�Ǹõ��Ƿ���뵽���·����
        i=i+1
    print T

      
def add_shortest_to_s():
    shortest=T[0]
    for node in T:
        if node[1]<shortest[1] and node[3]==0:
            shortest=node
    shortest[3]=1#���õ���Ϊ�Ѿ��������·��
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

