food=input("What meal did you have?")


if food=="pilau":
    x=800
    print(x)
elif food=="chicken":
    x=500
    print(x)
elif food=="fries":
    x=150
    print(x)
elif food=="fried rice":
    x=400
    print(x)
else:
  print("Unkown")

price=x

tip= eval(input("How much tip would like to give?"))

print("Total cost for your meal: ", tip+ price)
print("tip given is:",tip)
