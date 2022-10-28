import socketio
import multiprocessing
import led_status
sio = socketio.Client()

flag = multiprocessing.Value('i')

@sio.event
def updateThing(data):
    print(data)

@sio.event
def findAllThing(sid, data):
    print(sid, data)
    return "OK", 123

@sio.event
def connect():
    flag.value = 1
    print('connection established')


@sio.event
def updateThing(data):
    print(data)

@sio.event
def disconnect():
    flag.value = 0
    print('disconnected from server')


if __name__ == '__main__':
    try:
        p1 = multiprocessing.Process(
            name='led', target=led_status.loop, args=(flag,))
        sio.connect('http://35.154.151.227:3000')
        p1.start()
        sio.emit('findAllThing', {}, callback=findAllThing)
        sio.wait()

    except KeyboardInterrupt:
        sio.disconnect()
        print("disconnected")
