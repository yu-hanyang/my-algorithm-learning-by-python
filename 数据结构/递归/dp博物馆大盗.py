tr=[None,{'w':2,'v':3},{'w':3,'v':4},{'w':4,'v':8},{'w':5,'v':8},{'w':9,'v':10}]

max_w=20

#初始化表格
m={(i,w):0 for i in range(len(tr))
                for w in range(max_w+1)}

#逐个填写表格
for i in range(1,len(tr)):
    for w in range(1,max_w+1):
        if tr[i]['w'] > w:
            m[(i,w)]=m[(i-1,w)]
        else:
            m[(i,w)]=max(m[(i,w)],m[i-1,w-tr[i]['w']]+tr[i]['v'])

print(m[(len(tr)-1),max_w])