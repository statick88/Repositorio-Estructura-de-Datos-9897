'''
igual --> ==
diferente --> !=
mayor o igual que --> >=
menor o igual que --> <=
mayor que --> >
menor que --> <
'''

if 2 == 3:
    print("2 es igual a 2")
elif 0.5 > 1:
    print("2 es mayor que 1")
elif 8 < 3:
    print("3 es menor que 8")
elif 9 != 9:
    print("9 es distinto de 10")
elif 100 >= 101:
    print("100 es mayor o igual que 9")
elif 109 <= 100:
    print("9 es menor o igual que 100")
else:
    print("No se cumple ninguna condicion")

# Operadores Ternarios

if 2 < 10: print("2 es menor a 5")

print("Se imprime si la condición es verdadera") if 10 < 2 else print("Se imprime si la condición es falsa")

# And

if 2 < 9 and 3 < 10:
    print("2 es menor que 9 y 3 es menor que 10")

# Or

if 9 < 100 or 100 > 1000:
    print("9 es menor que 100 o 100 es mayor a 1000")
