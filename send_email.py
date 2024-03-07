from datetime import date  # core python module
import pandas as pd  # pip install pandas
from send_email import send_email  # local python module

import time
# Public GoogleSheets url - not secure!
SHEET_ID = "1gKRYKZHrqJntVN67ShgwGt8dHgs9j2TFTyFjwh9IN6E"
SHEET_NAME = "Sheet1"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"


def load_df(url):
  parse_dates = ["due_date", "reminder_date"]
  df = pd.read_csv(url, parse_dates=parse_dates)
  return df


print(load_df(URL))


def query_data_and_send_emails(df):
  present = date.today()
  email_counter = 0
  for _, row in df.iterrows():
    if (present >= row["reminder_date"].date()) and (row["wished"] == "no"):
      send_email(
          subject=f'Birthday Greetings on your birthday🎉🎉🎁 {row["birthday"]}',
          receiver_email=row["email"],
          name=row["name"],
          due_date=row["due_date"].strftime(
              "%d, %b %Y"),  # example: 11, Aug 2022
      )
      email_counter += 1
  return f"Total Emails Sent: {email_counter}"


df = load_df(URL)
result = query_data_and_send_emails(df)
print(result)

while 1:
  print("Restarting...")

  time.sleep(86400)
