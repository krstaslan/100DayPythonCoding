##################### Extra Hard Starting Project ######################
import pandas
from datetime import datetime
# 1. Update the birthdays.csv
data=pandas.read_csv("birthdays.csv")
all_data = data.to_dict()

# 2. Check if today matches a birthday in the birthdays.csv
now = datetime.now()
current_month = now.strftime("%m")
print(current_month)
current_day = now.strftime("%d")
if current_month in all_data["month"]:
    

#for i in all_months:
#    print(i)
#    if int(i) == int(current_month):
#        print("yes")
#
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




