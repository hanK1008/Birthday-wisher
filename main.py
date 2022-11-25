##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
# with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

# ________________________ Imports_____________________________
import datetime as dt
import pandas
import os
import random
import smtplib

# _________________my credential______________________________________

sender_email = "hank77981@gmail.com"
password = "pvpsjvhslpoagkpk"

# _____ Getting holding of date & month from birthday.csv_____________

data = pandas.read_csv("birthdays.csv")

# _____ checking today's date is matched with birthday date____________

now = dt.datetime.now()
current_month = now.month
current_day = now.day


for (index, row) in data.iterrows():
    if current_day == row.day and current_month == row.month:
        person_name = row["name"]
        person_email_id = row.email

        # pick random file from letter_template dir
        random_file = random.choice(os.listdir("letter_templates"))
        with open(file=f"./letter_templates/{random_file}", mode="r") as file:
            data = file.read()
            new_msg = data.replace("[NAME]", person_name)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=sender_email, password=password)
            connection.sendmail(from_addr=sender_email, to_addrs=person_email_id,
                                msg=f"Subject:Happy Birthday!!!\n\n{new_msg}")
