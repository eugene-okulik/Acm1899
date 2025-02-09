from datetime import datetime

date_str = "Jan 15, 2023 - 12:05:33"
date_obj = datetime.strptime(date_str, "%b %d, %Y - %H:%M:%S")
full_month_name = date_obj.strftime("%B")
print(full_month_name)
date_new_form = date_obj.strftime("%d.%m.%Y, %H:%M")
print(date_new_form)
