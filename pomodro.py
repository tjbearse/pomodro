from datetime import datetime, timedelta
import time
import threading
import sys

#day, second, micro milli min hour week
target = datetime.today()
#times = [timedelta(0, 0, 0, 0, 20), timedelta(0, 0, 0, 0, 5)]
times = [timedelta(0, 10)]
time_index = 0

def td_to_string(td):
    s = td.total_seconds()
    hours, remainder = divmod(s, 3600)
    minutes, seconds = divmod(remainder, 60)
    return "%02d:%02d:%02d" % (hours, minutes, seconds)

def flash(sem):
    while sem.acquire(False):
        print "flash"
        sem.release()
        time.sleep(.5)
        
def alarm():
    sem = threading.Semaphore(1)
    t = threading.Thread(target=flash, args=(sem,) )
    t.start()
    #time.sleep(3)
    #print '\rStarting timer for %s\n' % td_to_string(times[time_index])
    raw_input()
    sem.acquire()

def updateTimer():
    global target
    global time_index
    global times
    if(target < datetime.today()):
        alarm()
        target = datetime.today() + times[time_index] 
        time_index += 1
        time_index %= len(times)
    diff = (target - datetime.today())
    sys.stdout.write("\r%s" % td_to_string(diff))
    sys.stdout.flush()
    threading.Timer(1, updateTimer).start()

updateTimer()
