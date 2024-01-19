number =int(input("enter the number:"))
if number%15==0:
    print("the number is dividible by 15")
else:
    if number%3==0 or number%5==0:
        print("the number is devisible by 3 or 5")
    else :
        print("the number is neither divided by 3 nor 5")        