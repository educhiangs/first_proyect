list_item = [99, 'no data', 95, 94, 'no data']
# resultado = []  
# for item in list_item:
#     # Aca abajo estoy comparando si el item es un string
#     if type(item) == str: # si item es un string deberia marcar True
#         resultado.append(0) #Por que no remplasa el string por el 0
#     else:
#         resultado.append(item)
# print(resultado)


# def foo(lst):
#     return [item if isinstance(item, (int, float)) else 0 for item in lst]
# print(foo(list_item))

# isinstance() es mejor porque reconoce varios tipos de objetos
# for item in list_item:
#     print(isinstance(item, str))

# def foo(lst):
#     return sum(float(item) for item in lst)

# print(foo(['1.2', '2.6', '3.3']))

# Cheatsheet: List Comprehensions

# In this section, you learned that:

# A list comprehension is an expression that creates a list by iterating over another container.

# A basic list comprehension:

# [i*2 for i in [1, 5, 10]]
# Output: [2, 10, 20]

# List comprehension with if condition:

# [i*2 for i in [1, -2, 10] if i>0]
# Output: [2, 20]

# List comprehension with an if and else condition:

# [i*2 if i>0 else 0 for i in [1, -2, 10]]
# Output: [2, 0, 20]

# def foo(x, y):
#     return x+y

# print(foo("abc", "def"))

# myfile = open("fruits.txt")
# content = myfile.read()
# myfile.close()

# with open("files/vegetable.txt", "w") as myfile:
#     myfile.write("Tomato\nCucumber\nGarlic")

# with open("files/fruits.txt", "w") as my_file:
#     my_file.write("Pear\napple\norange\nmandarin\nwatermelon\npomegranate")

# myfile = open("files/bear.txt")
# content = myfile.read() 
# print(type(content))
# print(content)

# with open("files/msg.txt", "w") as my_file:
#     content = my_file.write("Hello mamita pobechicha")
# print(content)
# try:
#     with open("files/msg.txt", "w") as my_file:
#         my_file.write("Hello mamita pobechicha")
#     print("archivo creado con exito")
# except FileExistsError:
#     print("El archivo existe asi que no hice nada")

# with open("files/bear.txt") as my_file:
#     content = my_file.read()
# print(content[:90])

# with open("files/fruits.txt", "+a") as myfile:
#     myfile.write("\nhello")
#     myfile.seek(0)
#     content = myfile.read()
# print(content)

# with open("files/bear1.txt", "r") as file1:
#     content = file1.read()

# with open("files/bear2.txt", "a+") as file2:
#     file2.write(content)
#     file2.seek(0)
#     content = file2.read()

# with open("files/data.txt", "a+") as file:
#     file.seek(0)
#     content = file.read()
#     file.seek(0)
#     if not content.endswith("\n"):
#         content += "\n"
#     file.write("\n" + content)
    
# print(content)
print("hello")