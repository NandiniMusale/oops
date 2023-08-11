l=[]
data=[1,2,3,4,5,6,7]
def prob(data):
    for i in data:
        if i%2==0:
            l.append(i)
    return l
k=prob(data)
print(k)