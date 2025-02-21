import os
import datetime

current_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(current_path))
target_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

def read_file():

    with open(target_file_path, encoding="utf8") as data_file:
        for line in data_file.readlines():
            yield line


date_list = []
for data_line in read_file():
    date_str = data_line[3:29]
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
    date_list.append(date)

print(date_list[0] + datetime.timedelta(days=7))
print(date_list[1].strftime('%A'))
delta = datetime.datetime.now() - date_list[2]
print(delta.days)
