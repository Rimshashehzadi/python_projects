"""
Dictionary

collection of key+value = pair = data1

letf-side = key
right-side = value
{key1:value1, key2:value2}
 we can perform  multiple operation in dictionary
 add
 update
 delete
 view (get) use by "print" function

"""
var = {'key1' :100, 'key2':200}
print(var)

# Creating Dictionary by student

student = {
    'Rimsha': 400,
     'Alina': 300
}

#Accessing an element
print(student['Alina'])

#Update
student['Alina'] = 800
print(student)
print(student.update({'Rimsha':700}))
print(student)

#Delete
student.pop('Rimsha')
print(student)

