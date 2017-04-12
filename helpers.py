import time

def delay_print(s):
    if isinstance(s, str):
        if len(s.split()) > 1:
            for line in s.split('\n'):
                print(line)
                time.sleep(.25)
        else:
            print(s)
            time.sleep(.25)
    else:
        print(s)
        time.sleep(.25)
