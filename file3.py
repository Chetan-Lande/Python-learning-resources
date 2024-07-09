#List
#define by 1st way
a = [1,4,9,16,25,36,49,64]
print(a[0],a[-8])
#accesing each data-item by positive index, negative index
print(a[1],a[-7])
print(a[2],a[-6])
print(a[3],a[-5])
print(a[4],a[-4])
print(a[5],a[-3])
print(a[6],a[-2])
print(a[7],a[-1])

#define by 2nd way
b = list(("abcde",23,6.7,"_",2+5j))
print(type(b[-2]))
print(b,type(b))
print(b[1])
print(b[2])
print(b[0][2])  #extracting letter of string by using list
print(b[-1].real, b[-1].imag)

#list slicing
c = list((0,1,2,3,4,5,6,7,8,9))
even = c[0:9:2]
print(even)
odd = c[-1:-10:-2]
print(odd)
print(c[2:])
print(c[ : : -3])
print(c[3:6])
print(c[-1:2:-2])  #mix indexing used


