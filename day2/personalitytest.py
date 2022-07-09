#personality test

numberOfBooksPurchased = int(input("How many books did you purchase? "))
if numberOfBooksPurchased == 0:
    pointsAwarded = 0
    print("You are awarded",str(pointsAwarded)+" points")
elif numberOfBooksPurchased == 1:
    pointsAwarded = 6
    print("You are awarded",str(pointsAwarded)+" points" )
elif numberOfBooksPurchased == 2:
    pointsAwarded = 16
    print("You are awarded",str(pointsAwarded)+" points")
elif numberOfBooksPurchased == 3:
    pointsAwarded = 32
    print("You are awarded",str(pointsAwarded)+" points" )
elif numberOfBooksPurchased >= 4:
    pointsAwarded = 60
    print("You are awarded",str(pointsAwarded)+" points" )