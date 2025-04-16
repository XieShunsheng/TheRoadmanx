import sensor, image, time, os, tf, math, uos, gc,pyb
from pyb import UART
from pyb import LED
led2 = pyb.LED(2)
led1 = pyb.LED(1)
led1.on()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((240, 240))
sensor.skip_frames(time=2000)
net = None
labels = None
min_confidence = 0.5
uart = UART(3, 115200)
uart.init(115200, bits=8, parity=None, stop=1)
red_led   = LED(1)
green_led = LED(2)
blue_led  = LED(3)
ir_led	= LED(4)
try:
	net = tf.load("trained.tflite", load_to_fb=uos.stat('trained.tflite')[6] > (gc.mem_free() - (64*1024)))
except Exception as e:
	raise Exception('Failed to load "trained.tflite", did you copy the .tflite and labels.txt file onto the mass-storage device? (' + str(e) + ')')
try:
	labels = [line.rstrip('\n') for line in open("labels.txt")]
except Exception as e:
	raise Exception('Failed to load "labels.txt", did you copy the .tflite and labels.txt file onto the mass-storage device? (' + str(e) + ')')
colors = [
	(255,   0,   0),
	(  0, 255,   0),
	(255, 255,   0),
	(  0,   0, 255),
	(255,   0, 255),
	(  0, 255, 255),
	(255, 255, 255),
]
clock = time.clock()
while(True):
	clock.tick()
	img = sensor.snapshot()
	for i, detection_list in enumerate(net.detect(img, thresholds=[(math.ceil(min_confidence * 255), 255)])):
		if (i == 0): continue
		if (len(detection_list) == 0): continue
		print("********** %s **********" % labels[i])
		for d in detection_list:
			[x, y, w, h] = d.rect()
			center_x = math.floor(x + (w / 2))
			center_y = math.floor(y + (h / 2))
			print('x %d\ty %d' % (center_x, center_y))
			img.draw_circle((center_x, center_y, 12), color=colors[i], thickness=2)
		if(labels[i] == 'apple'):
			uart.write("1")
			green_led.on()
			time.sleep(0.5)
			green_led.off()
		if(labels[i] == 'pear'):
			uart.write("2")
			green_led.on()
			time.sleep(0.5)
			green_led.off()
		if(labels[i] == 'mango'):
			uart.write("3")
			green_led.on()
			time.sleep(0.5)
			green_led.off()
		if(labels[i] == 'plum'):
			uart.write("4")
			green_led.on()
			time.sleep(0.5)
			green_led.off()
		if(labels[i] == 'grape'):
			uart.write("5")
			green_led.on()
			time.sleep(0.5)
			green_led.off()
	print(clock.fps(), "fps", end="\n\n")
