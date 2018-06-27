# excersizing datetime timedelta object

import datetime
checkin = datetime.date(2018, 3, 5)
stay = datetime.timedelta(11)
checkout = checkin + stay
print checkout

# Converting string into datetime object
moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)
print(moon_landing_datetime.strftime("%A, %B %d, %Y"))
