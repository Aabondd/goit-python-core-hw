from datetime import datetime, timedelta

WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
users=[
    {'name':'Tom', 'birthday': datetime(year=1988, month=12, day=10)},
    {'name':'Jef', 'birthday': datetime(year=1985, month=3, day=4)},
    {'name':'Alex', 'birthday': datetime(year=1986, month=4, day=12)},
    {'name':'Bob', 'birthday': datetime(year=2011, month=5, day=10)},
    {'name':'Alla', 'birthday': datetime(year=1971, month=5, day=11)},
    {'name':'Inna', 'birthday': datetime(year=1984, month=8, day=7)},
    {'name':'Rock', 'birthday': datetime(year=2018, month=9, day=23)},
    {'name':'Max', 'birthday': datetime(year=1999, month=1, day=7)},
    {'name':'Ben', 'birthday': datetime(year=2011, month=1, day=9)},
    {'name':'Steve', 'birthday': datetime(year=1971, month=11, day=26)},
    {'name':'Igor', 'birthday': datetime(year=1984, month=12, day=7)},
    {'name':'Kim', 'birthday': datetime(year=2018, month=3, day=16)},
    {'name':'Denys', 'birthday': datetime(year=1999, month=2, day=15)}
    ]
CURRENT_DATE = datetime.today()

def get_birthdays_per_week(users):
    names_per_day = [[], [], [], [], []]
    mon_date = CURRENT_DATE - timedelta(days=CURRENT_DATE.weekday())
    dates_list = [(mon_date+timedelta(days=x)).strftime('%d.%m') for x in range(-2, 5)]
    grouped_dates_list = [dates_list[:3]]+dates_list[3:]
    for item in users:
        item['birthday'] = datetime.strftime(item['birthday'], '%d.%m')
        for d in range(len(grouped_dates_list)):
            if item['birthday'] in grouped_dates_list[d]:
                if item['birthday'] == dates_list[0] or item['birthday'] == dates_list[1]:
                    entry = (f"{item['name']} (was on {item['birthday']})")
                    names_per_day[d].append(entry)
                else:
                    entry = (f"{item['name']}")
                    names_per_day[d].append(entry)
    return names_per_day

def congratulate_colleques():
    print('This week we congratulate:')
    bday_guys = get_birthdays_per_week(users)
    for d in range(len(bday_guys)):
        if len(bday_guys[d]) != 0:
            print(f"{WEEKDAYS[d]}: {', '.join(bday_guys[d])}")

if __name__ == '__main__':
    congratulate_colleques()