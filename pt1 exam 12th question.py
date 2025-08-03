def foo(s1,s2):
    a1=[]
    a2=[]
    for x in s1:
        a1.append(x)
    for x in s2:
        a2.append(x)
    return a1,a2
a,b=foo("FUN","DAY")
print(a,b)
