risshun = list(map(int, input("何年何月何日が立春？").split()))
y = risshun[0]
m = risshun[1]
d = risshun[2]
daymonth = [0,31,28,31,30,31,30,31,31,30,31,30,31]
lp_month = [0,31,29,31,30,31,30,31,31,30,31,30,31]

days = 88
dayleft = d + days - 1

import calendar

if calendar.isleap(y):
    while dayleft > lp_month[m]:
        dayleft = dayleft - lp_month[m]
        m = m + 1
else:
    while dayleft > daymonth[m]:
        dayleft = dayleft - daymonth[m]
        m = m + 1

import datetime

date = datetime.date(y, m, dayleft)
n = date.weekday()
yobi = ["月", "火", "水", "木", "金", "土", "日"]

print("", y, "年の八十八夜は", m ,"月", dayleft, "日", yobi[n], "曜日です！")