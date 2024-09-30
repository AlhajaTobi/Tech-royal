import time


c = time.time()
print(c)

total_seconds = int(c)
seconds = int(input("Enter how many seconds in a minute(60) :"))
minutes = int(input("enter the minutes to convert to seconds"))
convert_minutes = minutes * seconds
convert_minutes_to_seconds = total_seconds % seconds

print(f"{minutes} minutes is equal to {convert_minutes_to_seconds} seconds.")
print(f"current time(hours,minutes, and seconds): {time.strftime('%H:%M:%S', time.localtime())}")


 