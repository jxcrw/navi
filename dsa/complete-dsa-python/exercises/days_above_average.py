#!/usr/bin/env python3
"""Calculate the number of days above the average temperature."""

day_count = int(input("How many days of data to input? "))

temps = []
for i in range(day_count):
    daily_high = float(input(f"Day {i+1}'s High Temp: "))
    temps.append(daily_high)

average_temp = sum(temps) / len(temps)

above_average_binary = [1 if _ > average_temp else 0 for _ in temps]
days_above_average = sum(above_average_binary)

print(f'average_temp: {average_temp}')
print(f'days_above_average: {days_above_average}')
