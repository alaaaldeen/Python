import csv
from datetime import datetime

path = '/users/alaa/downloads/google.csv'
f = open(path)
reader = csv.reader(f)

header = next(reader)
data = []


# [date, float, float, float, float, int, float]
for row in reader:
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1])  # open is name of builtinfile function
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])

    data.append([date, open_price, high, low, close, volume, adj_close])


# Compute and store the daily stock returns
returns_path = '/users/alaa/downloads/google_returns.csv'
f = open(returns_path, 'w')
writer = csv.writer(f)
writer.writerow(["Date", "Return"])

for i in range(len(data) - 1):
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]
    yesterdays_row = data[i+1]
    yesterdays_price = yesterdays_row[-1]

    daily_return = (todays_price - yesterdays_price) / yesterdays_price
    formatted_date = todays_date.strftime('%m/%d/%Y')
    writer.writerow([formatted_date, daily_return])
