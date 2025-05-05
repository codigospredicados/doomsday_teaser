from datetime import datetime, date, timedelta
import random

def wd(d:datetime):
    x = d.weekday() + 2
    return (x if x < 8 else 1) % 7

def wd_desc(d):
    return {0:"Sábado", 1:"Domingo", 2:"Segunda-feira", 3:"Terça-feira", 4:"Quarta-feira", 5:"Quinta-feira", 6:"Sexta-feira"}[d]

century_doomsdays = {16:3, 17:1, 18:6, 19:4, 20:3, 21:1}

inq_date = date(random.randint(1600, 2199), 1, 1) + timedelta(days=random.randint(0,366))
year = inq_date.year
century = int(year / 100)
just_year = year - century * 100

print("CONWAY's doomsday! v 3")
print("======================")
print(f"Date: {inq_date}")

print("Century doomsday")
input(" ?")

century_doomsday = century_doomsdays[century]
print(f" L_ {wd_desc(century_doomsday)}")
print("")

print("Year doomsday:")
input(" ?")

year_doomsday = (century_doomsday + just_year + int(just_year/4)) % 7
print(f" L_ {wd_desc(year_doomsday)}")
print("")

print(f"{inq_date} weekday:")
input(" ?")

print(f" L_ {wd_desc(wd(inq_date))}")
print("")

