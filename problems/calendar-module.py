#https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true
import calendar

month, day, year = map(int, input().split())
weekday_n = calendar.weekday(year, month, day)
day_name = calendar.day_name[weekday_n].upper()

print(day_name)