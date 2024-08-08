def seconds_to_time(seconds):

    if seconds < 0 or seconds >= 8640000:
        return "Число повинно бути в межах від 0 до 8639999 включно."

    seconds_per_day = 86400

    seconds_per_hour = 3600

    seconds_per_minute = 60

    days, remainder = divmod(seconds, seconds_per_day)

    hours, remainder = divmod(remainder, seconds_per_hour)

    minutes, seconds = divmod(remainder, seconds_per_minute)

    if days % 10 == 1 and days % 100 != 11:
        day_str = f"{days} день"
    elif days % 10 in (2, 3, 4) and not (days % 100 in (12, 13, 14)):
        day_str = f"{days} дні"
    else:
        day_str = f"{days} днів"

    formatted_time = f"{day_str}, {hours:02}:{minutes:02}:{seconds:02}"
    return formatted_time

user_input = int(input("Введіть кількість секунд: "))
result = seconds_to_time(user_input)
print(result)
