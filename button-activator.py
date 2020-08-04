import RPi.GPIO as GPIO
import requests
import signal

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN)

def main():
	signal.signal(signal.SIGALRM, handler)
	# while True:
	# 	if GPIO.input(16) == 0:
	print('button pressed')
	signal.alarm(5)
	request_camera()


def request_camera():
	requests.get("http://localhost:5000/video_feed")


def handler(signum, frame):
	print('request done')
	main()


if __name__	== '__main__':
	main()