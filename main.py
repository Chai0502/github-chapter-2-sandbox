import datetime, bday_messages
today = datetime.date.today()
next_birthday = datetime.date(2025, 5, 30)
days_away = (next_birthday - today).days


if today == next_birthday:
    print(bday_messages.random_message)
else:
    print(f'My birthday is in {days_away} days away!')

