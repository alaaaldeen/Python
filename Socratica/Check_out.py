# excersizing datetime timedelta object

import datetime
checkin = datetime.date(2017, 7, 2)
stay = datetime.timedelta(90)
checkout = checkin + stay
print checkout

# Converting string into datetime object
moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)
print(moon_landing_datetime.strftime("%A, %B %d, %Y"))
