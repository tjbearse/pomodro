from datetime import datetime, timedelta
import threading
import sys

#day, second, micro milli min hour week
target = datetime.today()
times = [timedelta(0, 10), timedelta(0, 5)]
time_index = 0

def td_to_string(td):
    s = td.total_seconds()
    hours, remainder = divmod(s, 3600)
    minutes, seconds = divmod(remainder, 60)
    return "%02d:%02d:%02d" % (hours, minutes, seconds)

def updateTimer():
    global target
    global time_index
    global times
    if(target < datetime.today()):
        print '\rStarting timer for %s' % td_to_string(times[time_index])
        raw_input()
        target = datetime.today() + times[time_index] 
        time_index += 1
        time_index %= len(times)
    diff = (target - datetime.today())
    sys.stdout.write("\r%s" % td_to_string(diff))
    sys.stdout.flush()
    threading.Timer(1, updateTimer).start()

updateTimer()
