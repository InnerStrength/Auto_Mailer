import smtplib
import pandas
from random import choice
import datetime as dt
letter_choice = choice(["letter_1.txt", "letter_2.txt", "letter_3.txt"])

with open(f"./letter_templates/{letter_choice}") as letter:
    message = ' '.join(letter.readlines())

data = pandas.read_csv("birthdays.csv")
now = dt.datetime.now()
birthday = (now.day, now.month)
todays_birthdays = (data[(data.month == birthday[1]) & (data.day == birthday[0])]).to_dict()

for i in range(len(todays_birthdays['name'])):
    personal_message = message.replace("[NAME]", todays_birthdays['name'][i])
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user="pwtonkinson@gmail.com", password="Tonki9513!")
        connection.sendmail(
            from_addr="pwtonkinson@gmail.com",
            to_addrs=todays_birthdays['email'][i],
            msg=f"Subject: HAPPY BIRTHDAY! \n\n{personal_message}"
        )
