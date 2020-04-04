import os
import datetime

def alarm():
    t1 = '01:00'
    t2 = '08:00'
    now = datetime.datetime.now().strftime("%H:%M")
    print("current tiem:" + now)
    if t1 < now < t2:
        print("sleeping, not alert")
        return

    duration = 60  # second
    freq = 440  # Hz
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))
