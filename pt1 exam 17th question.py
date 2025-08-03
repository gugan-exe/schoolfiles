def get(x,y,z):
    x+=y
    y-=1
    z*(x-y)
    print(x,"#",y,"#",z)
def put(z,y,x):
    x*=y
    y+=1
    z*=(x+y)
    print(x,"$",y,"$",z)
a=10
b=20
c=5
put(a,c,b)
get(b,c,a)
put(a,b,c)
get(a,c,b)
    
    
