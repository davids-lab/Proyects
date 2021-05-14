print("**Hello, this is a TIP calculator**\n\n")

monto = input("Please put the total amount of the bill: \n$")
propina = input("Please put the percentage of tip you want to give(10, 12 or 15): \n%")
personas = input("How many people to split the bill:\n")

monto_as_int = float(monto)
propina_as_int = int(propina)
personas_as_int = int(personas)

total = (((propina_as_int/100)*monto_as_int) + monto_as_int)
total_x_persona = "{:.2f}".format(total/personas_as_int,2)

print(f"Cada persona debe pagar: {total_x_persona}")

