#мій калькулятор

what = input( "Що робити (+, -, *, /): " )

a = float( input ("Ведіть перше число: ") )
b = float( input ("Ведіть друге число: ") )

if what == "+":
    c = a + b
    print(" Результат " + str(c))
elif what == "-":
    c = a - b
    print(" Результат " + str(c))
elif what == "*":
    c = a * b

elif what == "/":
    c = a / b
    print(" Результат " + str(c))
else:
   print("Вибрана неправильна операція")




