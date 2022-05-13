opt=float(input("Ingrese el ejercicio deseado: \n  1. Area de un triangulo:\n 2. Suma de dos numeros :\n 3. Cuadro de un numero :\n 4. Conversion euros a dolres:\n 5. Area y perimetro cuadrado:\n 6. volumen y area del cilindro :\n 7. Area de un circulo:\n 8. Suma y promedio numeros\n CONDICIONALES:\n 1.1.Algoritmo numero positivo o negativo: \n 1.2.Menor mayor o igual que:\n 1.3.Numeros positivos enteros mayor y menor:\n 1.4.Suma o resta de a y b:\n 1.5.Division de dos numeros:\n 1.6 Suma de numeros negativos o multiplicacion de numeros positivos:\n 1.7.Años bisiestos:\n CICLOS:\n 2.1 Multiplos de 3:\n 2.2 Impares entre 0 y 100:\n 2.3 Pares de 1 a 100:\n 2.4 Cuadrado de un numero:\n 2.5 Numeros naturales al cuadrado:\n 2.6 Secuencias ascendente:\n 2.7 Suma de todos lo numeros ingresados:\n "))
if opt== 1:
#Ejercicio 1
  base = float(input("Ingrese la base del triangulo: "))
  altura = float(input("Ingrese la altura de un triangulo: "))
  area=base*altura/2
  print("El area es:" + str (area))
if opt== 2:
    x=float(input("Ingrese el primer numero"))
    print("Dame otro numero")
    y=float(input("Ingrese el segundo numero"))
    print("Su suma es")
    print(x + y)
if opt== 3:
    numero1=float(input("Ingresa el primer numero"))
    numero2=float(input("Ingresa el segundo numero"))
    print("Su numero elevado es")
    print(numero1 ** numero2)
if opt== 4:
    numero_de_dolares = float(input("Ingrese dolares a convertir"))
    numero_de_euros = numero_de_dolares * 0.95
    print("el numero de euros que tiene es $" + str (numero_de_euros))
if opt==5:
    lc = float(input ("Digite el lado de un cuadrado:"))
    area= lc  **2
    perimetro= lc + lc + lc + lc
    print ("El valor del area y el perimetro equivale a :" + " " + str (area) + " " + str (perimetro))
  
if opt==6:
    radio=float(input("Ingrese el radio del cilindro\n"))
    altura = float(input("Ingrese la altura del cilindro\n"))
    area = 2*(3.1416*radio**2)+2*3.1416*radio*altura
    print("El area del cilindro es",area)
  #Ejercicio 7
if opt==7:
    radio=float(input("Ingrese el radio del circulo\n"))
    perimetro=2*3.1416*radio
    area=3.1416*radio**2
    print("El perimetro del circulo es",perimetro)
    print("El area del circulo es",area)
  
if opt==8:
    numero1=float(input("Ingrese el primer numero\n"))
    numero2=float(input("Ingrese el segundo numero\n"))
    numero3=float(input("Ingrese el Tercer numero\n"))
    formula=(numero1+numero2+numero3)/3
    print("El promedio de los numeros es",formula) 


#Condicionales
if opt==1.1:
    primer1=float(input("Digite un numero"))
    if primer1 >0:
        print("positivo")
    elif primer1 <0:
        print("negativo")
    else:
        print("El numero ingresado es neutro")
if opt==1.2:  
    primer=float(input("Digite un numero"))
    segundo=float(input("Digite el segundo numero"))
    if primer==segundo:
        print("Iguales")
    elif primer > segundo:
          print("El numero mayor es",primer,"El numero menor es",segundo)
    elif primer < segundo:
        print("El numero menor es",primer,"El numero mayor es",segundo)
if opt==1.3:
    primer=int(input("Digite un numero"))
    segundo=int(input("Digite el segundo numero"))
    tercer=int(input("Digite el tercer numero"))
    if primer < segundo and primer < tercer:
        print("El numero menor es",primer )
    elif segundo < primer and segundo < tercer:
        print("El numero menor es",segundo )
    elif tercer < primer and tercer < segundo:
        print("El numero menor es",tercer )
    if primer > segundo and primer  > tercer:
        print("El numero mayor es",primer )
    elif segundo > primer and segundo  > tercer:
        print("El numero mayor es",segundo )
    elif tercer > primer and tercer > segundo:
        print("El numero mayor es",tercer )
if opt==1.4:
    a=float(input("Digite un numero"))
    b=float(input("Digite un numero"))
    if a<b:
        print(a+b)
    elif a>b:
        print(a-b)
if opt==1.5:
    A=float(input("Digite un numero"))
    B=float(input("Digite un numero"))   
    if B!=0:
          print(A/B)
    elif B==0:
          print("No se puede divividir por 0")
if opt==1.6:
    a=float(input("Digite un numero"))
    b=float(input("Digite un numero"))
    if a<0 or b<0:
        print(a+b)
    elif a>0 and b>0:
        print(a*b)
if opt==1.7:
    aho=float(input("Digite un Año"))
    if aho%4==0:
        print("Año bisiesto")
    else:
        print("Año no bisiesto")
if opt==2.1:
    i=3
    while i<=100:
        print(i)
        i=i+3   
if opt==2.2:
    i=1
    for i in range(1,101,2):
        print(i)
if opt==2.3:
    i=2
    for i in range(2,101,2):
        print(i)
if opt==2.4:
    i=1
    for i in range(1,31,1):
        print(i**2)  
if opt==2.5:
    x=1
    for x in range(1,101,1):
        suma=0
        suma+=x**2
    print(suma)
if opt==2.6: 
    a=int(input("Digite un numero"))
    b=int(input("Digite un numero"))    
    for a in range(a,b+1,1):
        print(a)
if opt==2.7:   
    condicion=True
    suma=0
    while condicion:
        f=float(input("Digite un numero")) 
        suma=suma+f
        print("La suma es",suma)
        if f==0:
            print("No puedes ingresar el numero 0")
            condicion=False
   
