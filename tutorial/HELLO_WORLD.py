import calendar
print(calendar.month(2019, 5))
print(calendar.isleap(2020))

import datetime
print(datetime.date.today())
print(datetime.datetime.now())

d = datetime.datetime.now()
print(d.hour)
print(d.minute)
print(d.second)
today = datetime.date.today()
birth = datetime.date(2001, 7, 17)
print(today - birth)

import random
r = random.random()
print(r)
r = random.randint(1, 6)
print(r)
jan = random.choice(["グー", "チョキ", "パー"])
print(jan)

cnt = 0
while True:
    r = random.randint(1, 100)
    # print(r)
    cnt += 1
    if r == 77:
        break
print(f"{cnt}回目でレアキャラゲット")

