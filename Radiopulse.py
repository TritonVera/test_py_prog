import math
import matplotlib.pyplot as plot

#point_list

class Radiopulse():
	def __init__(self, length, period_pulse, number, period_packet, frequency):
		self.length = length
		self.period_pulse = period_pulse
		self.number = number
		self.period_packet = period_packet
		self.frequency = frequency
		self.points = self.gen_signal()

	def gen_signal(self, step = 0.001, end_time = 10.0):
		#print(self.time_step(0.0, step, end_time))
		point = []
		for time in self.time_step(0.0, step, end_time):
			in_time = time
			while in_time > self.period_packet:
				in_time = in_time - self.period_packet
			if in_time > (self.number * self.period_pulse):
				point.append(0)
			else:
				while in_time > self.period_pulse:
					in_time = in_time - self.period_pulse
				if in_time > self.length:
					point.append(0)
				else:
					point.append(garmonic(in_time, self.frequency))
		return point

	def send_test(self):
		print("I am working")

	def time_step(self, start, step, end):
		rang = []
		point = start
		rang.append(point)
		while point < end:
			point += step
			rang.append(point)
		return rang
		

def main():
	frequency = 2 #МГц
	length_pulse = 2.0 #мкс
	period_pulse = 4.0 #мкс
	period_packet = 100 #мкс
	number_pulse = 10 
	print('Длина импульса: %f мкс и минимальная частота: %d МГц'\
	 % (length_pulse, frequency))
	radiopulse = Radiopulse(length_pulse, period_pulse, number_pulse,\
	 period_packet, frequency) 
	make_plot(radiopulse.points)

def garmonic(tm, freq, amp = 1.0, phs = 0.0):
	signal = amp * math.sin((2 * math.pi * freq * tm) + phs)
	print(signal)
	return signal

def make_plot(point):
	fig = plot.figure()
	plot.plot(point)
	plot.show()

#Первичная инициализация программы
if __name__ == '__main__':
	main()