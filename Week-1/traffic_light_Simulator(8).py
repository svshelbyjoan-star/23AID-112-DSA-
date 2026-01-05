signal = input ("Enter the traffic light color (red, yellow, green): ").lower()
if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Prepare to stop")
elif signal == "green":
    print("Go")
else:
    print("Wrong input")