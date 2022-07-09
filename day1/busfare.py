from calendar import day_abbr
import datetime

date = datetime.datetime.now().date()
print(date)
#print(date.strftime("%a"))
day = day_abbr[date.weekday()]
print("Day:",day)
if day == "Sat":
    print("Fare:60")
elif day == "Sun":
    print("Fare:80")
else:
    print("Fare:100")
