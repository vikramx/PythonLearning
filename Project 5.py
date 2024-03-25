for i in range(5):
    name=input("Enter name here:")
    total=0
    for j in range(5):
        mark=float(input("Enter marks here:"))
        total+=mark
    print("The total marks of",name,"is:",total,"/500")