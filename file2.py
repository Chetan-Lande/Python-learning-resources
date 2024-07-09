#Constant
print("constant",123,65.8)

#variable
a,b = 123,65.4
_abc = 23.5
mnh0 = "_"
x1y = "7er_c"

#data types
#check data types of var
print(a,type(a))
print(b,type(b))
print(_abc,type(_abc))
print(mnh0,type(mnh0))
print(x1y,type(x1y))

print(a,end = "#")
print(a,b,sep = "@",end = "!")

#Numbers

#int
x = 12
print(x,type(x))

#float
y = 2.14
print(y,type(y))
print(x*y,type(x*y))

#complex
z = 4+5j    #1st way of define complex no.
print(z,type(z))
print(z.real,z.imag)
c = complex(x,y)
print(c)    #2nd way of define complex no.
print(z+c,type(z+c))   #add complex no.
print(z-c,type(z-c))   #sub complex no.
print(z*c,type(z*c))   #multi complex no.
print(z/c,type(z/c))   #divi complex no.

#String
s = 'hello world'
print(s,type(s))
print(s[0])     #extract the letter from string
print(s[0]+s[2])
print(s[-2])
print(s*2)
print(s+s[4])
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
print(s.swapcase())
print(s.startswith("h"))
