import time

def current_time_ms():
    return time.time()

starttime = current_time_ms()

i = 0
while i != 1000000000:
    i+=1

endtime = current_time_ms()
timeelapsed = endtime - starttime

print(f"Time taken by Python: {timeelapsed} secs")