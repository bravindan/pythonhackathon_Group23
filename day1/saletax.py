#sales tax challenge
laborChargeHr = 20.00
aGallon =115.00
hours = 8
sqrFeetOfWallSpace = float(input("Enter the square feet of wall space: "))
paintPricePerGallon = float(input("Enter the price per gallon of paint: "))
laborCharge = laborChargeHr * hours
gallons = sqrFeetOfWallSpace / aGallon
paintCost = gallons * paintPricePerGallon
totalCost = laborCharge + paintCost
hoursRequired = hours * sqrFeetOfWallSpace/aGallon
print("The total gallons of paint required is: ", format(gallons, ',.2f'), sep='')
print("The total hours required is: ", format(hoursRequired, ',.2f'), sep='')
print("The total paint cost is: $", format(paintCost, ',.2f'), sep='')
print("The total labor charge is: $", format(laborCharge, ',.2f'), sep='')
print("The total cost of the job is: $", format(totalCost, ',.2f'), sep='')
