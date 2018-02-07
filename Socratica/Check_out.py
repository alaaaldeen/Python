# excersizing datetime timedelta object

import datetime
checkin = datetime.date(2017, 7, 2)
stay = datetime.timedelta(90)
checkout = checkin + stay
print checkout
