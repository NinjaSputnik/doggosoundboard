import debounce.py

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
cb = ButtonHandler(4, real_cb, edge='rising', bouncetime=100)
cb.start()
GPIO.add_event_detect(4, GPIO.RISING, callback=cb)