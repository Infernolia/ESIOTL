import picamera
camera = picamera.PiCamera()
camera.resolution = (800, 600)
camera.start_preview()
sleep(5)
camera.capture(‘31301_a3.jpg’, resize=(640, 480))
camera.stop_preview()


camera.start_preview()
camera.start_recording('31301_b3.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()