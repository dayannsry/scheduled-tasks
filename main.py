from datetime import datetime
import random
import smtplib

MY_EMAIL = "serydayann@gmail.com"
MY_PASSWORD = "ggjr qhbq zqjq xmwz"
today = datetime.now()
today_tuple = (today.month, today.day)
import pandas
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {
    (data_row.month, data_row.day): data_row for (index, data_row)in data.iterrows()
}

if today_tuple in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        birthday_person = birthdays_dict[today_tuple]
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{content}"
        )
#update
