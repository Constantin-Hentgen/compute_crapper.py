question = '1*3+8'
nombre =  ''
nombre1 =  ''
i = 0
new = 0
result = 0
operation = ''
for lettre in question:
    
    if new == 1  and str.isdigit(lettre) == True:
        nombre1 += lettre
        
    elif str.isdigit(lettre) == True and str.isdigit(question[i]) == True:     
        nombre += lettre      
        i += 1     
        
    elif str.isdigit(lettre) == False:
        new = 1        
        if lettre ==  "*" or lettre == 'x':
            operation = 'mult'
        elif lettre ==  "-":
            operation = 'sub'
        elif lettre ==  "+":
            operation = 'add'
        elif lettre ==  "/":
            operation = 'div'
        
print(operation)
        
if operation == 'mult':
    result = int(nombre)*int(nombre1)
elif operation == 'sub':
    result = int(nombre)-int(nombre1)
elif operation == 'add':
    result = int(nombre)+int(nombre1)
elif operation == 'div':
    result = int(nombre)/int(nombre1)
if operation == 'mult' and nombre1 == 0:
    print('Ah bah bravo maintenant je vais crash')
        
print('nombre : ' , nombre)
print('nombre1 : ' , nombre1)
print(result)
print(int(nombre)/int(nombre1))
