#List
a = [5.5,'abc',67,28.0,2-6j,True]
a[0]  #acess by positive indexing 
a[-3] #acess by negative indexing

#list slicing
print(a[0:5:2])
print(a[-1:0:-1])
print(a,type(a))
print(a[2])
b = [1,2,3,5,8,13,[1,2,3],21,35]
print(type(b))
print(b[-3][1])
c = [a,b]
print(c)

#operations on list
a.insert(5,[11,47,67])
a.insert(-1,200)      #insert by indexing
e = [11,22,33,44,55]
e.extend([11,22,33])
print(e)
e.append('abc')
e.extend("efg")
e.extend(['abc'])
a.remove(67)        #by elements value
a.pop(5)           #by indexing
print(a)
del a [0:5:1]
print(a)
b[-3].insert(2,100)
b[-3].remove(3)
print(b)
print(a.count(2))
print(b.count(1))
print(b.index(2))
b.reverse()
print(b)
s = [1,2,5,3,25,23]
s.sort()
print(s)
s.sort(reverse = True)
print(s)
c = b.copy()
