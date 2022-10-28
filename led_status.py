import time
state = True

def loop(a):
    global state
    while(True):
        if (a.value == 1):
            state = True
            print(f'LED: {state}')
        else:
            state = not state
            print(f'LED: {state}')
        time.sleep(1)
