principle = 0
time = 0
rate = 0
while True:
    principle=float(input("Enter the principle amount:  "))
    if principle <= 0 :
        print("Principle can not be less than or equal to zero")
    else:
        break
while True:
    rate=int(input("Enter the interest rate:  "))
    if rate <= 0 :
        print("Interest can not be less than or equal to zero")
    else:
        break
while True:
    time=int(input("Enter the time in years:  "))
    if time <= 0 :
        print("Time can not be less than or equal to zero")
    else:
        break
Total = principle*pow((1+rate/100),time)
print(f"Balance after {time} year/s: ${Total:.2f}")