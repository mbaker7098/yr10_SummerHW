numberToTimes = int(input("What number would you like to times: "))#the number they want to know the timestable to
howMany = int(input("How far do you want to go up to: "))#the number they wish to go up to
for x in range(1,(howMany+1)):#x is the value that the number is timesed by, it ends at the users number they wished to up to
    print(numberToTimes * x)#prints the number they wanted times by the number in x each time until the loop ends at the number they also chose
