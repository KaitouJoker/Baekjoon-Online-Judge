import datetime

time = datetime.datetime.utcnow()

if int(time.strftime('%H')) > 15:
    time = time + datetime.timedelta(days=1)

print(time.date())