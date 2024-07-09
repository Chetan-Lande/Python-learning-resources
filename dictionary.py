#Dictionary
student = {
    'name' : 'chetan',
    'age' : 20,
    'roll_no' : 6,
    'dep' : 'computer',
    'result' : True
    }
d = dict(name = 'aaa', age = 12)
print(student,type(student))
print(student['result'])     #acess a element
print(student.get("country"))
student['country'] = 'india' #add a element
student['roll_no'] = 54
print(student)
#remove functions
student.pop('age')
student.clear() #removes only all element not dict
print(student)
del student     #removes whole dict

a = {
    'x' : 2,
    'y' : 5,
    'z' : 3
    }
print(a.items)
print(a.keys())      #acess all keys
print(a.values())    #acess all values
b = a.copy()
a.update({
    "x" : 'a',
    "z" : 2,
    "y" : 4
    })
print(a)
print(d)

#nested dict
emp = {
    "name" : "a", "id" : 12, "age" : 29, "gender": "female"
    }
company = {
    "e1" : {
        "name" : "a", "id" : 24,
        "age" : 23, "gender" : "female"
        },
    "e2" : {
        "name" : "b", "id" : 34,
        "age" : 26, "gender" : "male"
        }
    }
print(company)
print(type(company))
print(company["e1"])
print(company["e2"])
print(company.get("e2"))
print(company["e1"]["name"])
print(company.get("e3"))
print(company.get("e2")["id"])

#create nested dict another way
e1 = {"name" : "ab", "age" : 25}
e2 = {"name" : "bc", "age" : 27}
e = {
    1:e1,
    2:e2
    }
print(e)     
print(e[2]['name'])     #acess e2
print(e[2].get('name')) #acess e2



