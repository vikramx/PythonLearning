light=(input("Enter traffic light colour here in all lower case:"))
if(light=="red"):
    print("Stop the vehicle")
elif(light=="orange"):
    print("Please wait for signal to turn green")
elif(light=="green"):
    print("You may move the vehicle")
else:
    print("Colour is invalid.Please recheck colour")