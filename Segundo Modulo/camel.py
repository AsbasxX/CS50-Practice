#Variables camel a snake

variableCamel = input("Escribe una variable en camelCase: ")
variable_snake = ""
for char in variableCamel:
    if char.isupper():
        variable_snake += "_" + char.lower()
        print(variable_snake)
    else:
        variable_snake += char
        print(variable_snake)

print(variable_snake)