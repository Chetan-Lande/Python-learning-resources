#python
print("Python is the programming language")

a = 12
b = 6
c = 6
"""in python each object having unique id ,as object a having unique id ,
   but b & c have same value so they share same objectframe."""
print(a,id(a))
print(b,id(b))
print(c,id(c))
"""after executin we proved that object b & c stored in same memory queue not
   differently because they have same stored value(2). So they share a same memory
   queue."""
