import time


def get_data(unix_time):
    ltime=time.localtime(unix_time)
    timeStr=time.strftime("%Y-%m-%d %H:%M", ltime)
    return timeStr