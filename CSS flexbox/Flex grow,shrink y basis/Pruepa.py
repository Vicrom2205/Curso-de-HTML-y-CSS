def Triangle():
    #Imprimir un triangulo
    a = 0
    while a < 5:
        a += 1
        for n in range(a):
            print("*", end="")
        print()
Triangle()
print("finish")