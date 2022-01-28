##################### Extra Hard Starting Project ######################
import pandas
import random
import os
import smtplib
from datetime import datetime


def send_message(to_email, send_to):
    message = change_letter(send_to)
    my_email = "kursataslanwarsaw@gmail.com"
    password = "bagazici123"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject:Happay Birthday\n\n{message}"
        )
    print(to_email)
    print(message)


def random_letter():
    dir = "letter_templates/"
    path = random.choice(os.listdir("letter_templates"))
    path = dir + path
    return path


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

def change_letter(name):
    path = random_letter()
    with open(path) as letter:
        message = letter.read()
    new_letter = message.replace("[NAME]", name)
    return new_letter


# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
all_data = data.to_dict()

# 2. Check if today matches a birthday in the birthdays.csv
now = datetime.now()
current_month = int(now.strftime("%m"))

current_day = int(now.strftime("%d"))

name=""
email=""
for x in all_data["month"]:
    try:
        if current_month == int(all_data["month"][x]) and \
                current_day == int(all_data["day"][x]):
            name = all_data["name"][x]
            email = all_data["email"][x]
            send_message(email, name)


    except ValueError:
        pass

# 4. Send the letter generated in step 3 to that person's email address.
