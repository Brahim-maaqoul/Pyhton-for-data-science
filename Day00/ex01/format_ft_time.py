import datetime
import time

current_time = time.time()

formatted_time = f"Seconds since January 1, 1970: {current_time:,.4f}"

scientific_notation = f"{current_time:.2e}"

print(f"{formatted_time} or {scientific_notation} in scientific notation$")
x = datetime.datetime.now()

print(x.strftime("%b"), x.day, x.year)