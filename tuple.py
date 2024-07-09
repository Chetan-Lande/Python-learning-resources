#Tuple
a = (2,2.5,True,3+9j,[2,5,6])
t = tuple({2,8,'abc'})
print(a,type(a))
print(a[0],type(a[0]))  #acessing a particular element
print(a[-3],type(a[-3]))
print(a[0:3:2])         #acessing multiple elements

#opeartions
print(a.index(True))
print(a.count(2))
x = (a,'b','c','d',True,False,1,0,1,1)
print(x.count(True),x.count(False))
a1 = (1,2,3)
a2 = (3,2,1)
print(a1+a2,type(a1+a2))
print(a1*2)
print(t,type(t))
print(t[2],type(t[2]))

