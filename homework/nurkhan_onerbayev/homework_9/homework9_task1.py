from datetime import datetime


task_date = "Jan 15, 2023 - 12:05:33"

python_date = datetime.strptime(task_date, '%b %d, %Y - %H:%M:%S')

print(python_date.month)


task_date2 = python_date.strftime('%d.%m.%Y, %H:%M')

print(task_date2)
