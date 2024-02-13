# 4.	Write a Python program to extract year, month, date and time using Lambda.
# Sample Output:
# 2020-01-15 09:03:32.744178
# 2020
# 1
# 15
# 09:03:32.744178

date_time = "2024-02-13 1:03:32.744178"

extract = lambda date_str: (
    date_str[:4], 
    int(date_str[5:7]),  
    int(date_str[8:10]),
    date_str[11:] 
)

year, month, day, time = extract(date_time)
print(date_time)
print(year)
print(month)
print(day)
print(time)

