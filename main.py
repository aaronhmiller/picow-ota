from machine import Pin, Timer
led = machine.Pin("LED", machine.Pin.OUT)

def tick(timer):
    led.toggle()

Timer().init(freq=2, callback=tick) # call tick twice a sec