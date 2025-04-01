import math
from datetime import datetime


def format_date(date:datetime):
    month = date.month
    month_sin = math.sin(2*math.pi*month/12)
    month_cos = math.cos(2*math.pi*month/12)

    day = date.day
    day_sin = math.sin(2*math.pi*day/30)
    day_cos = math.cos(2*math.pi*day/30)

    hours = date.hour
    hours_sin = math.sin(2*math.pi*hours/24)
    hours_cos = math.cos(2*math.pi*hours/24)

    date = int(date.timestamp())
    return [[date,day,day_sin,day_cos,month,month_sin,month_cos,hours,hours_sin,hours_cos]]
