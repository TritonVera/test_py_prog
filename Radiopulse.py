import math
import matplotlib.pyplot as plot

#Параметры сигнала
frequency = 2 #МГц
length_pulse = 2.0 #мкс
period_pulse = 4.0 #мкс
period_packet = 100 #мкс
number_pulse = 10 

class Radiopulse():
	#Конструктор объекта
	def __init__(self, length, period_pulse, number, period_packet, frequency):
		self.__length = length
		self.__period_pulse = period_pulse
		self.__number = number
		self.__period_packet = period_packet
		self.__frequency = frequency
		self.gen_signal()

	#Конфигуратор объекта
	def configure(self, length = None, period_pulse = None,
				  number = None, period_packet = None,
				  frequency = None):
		if (length != None):
			self.__length = length
		if (period_pulse != None):
			self.__period_pulse = period_pulse
		if (number != None):
			self.__number = number
		if (period_packet != None):
			self.__period_packet = period_packet
		if (frequency != None):
			self.__frequency = frequency

	#Функция генерирования массивов точек радиосигнала
	def gen_signal(self,start_time = 0.0, step = 0.001, end_time = 10.0):
		#Инициализация внутренних переменных
		start_time_c = start_time
		step_c = step
		end_time_c = end_time

		#Создание дискретов времени
		self.xpoints = self.__time_step(start_time_c, step_c, end_time_c)

		#Создание пустых массивов точек
		self.Ipoints = []		#Косинусоидальная квадратура сигнала
		self.Qpoints = []		#Синусоидальная квадратура сигнала
		self.Zpoints = []		#Комплексный сигнал

		#Алгоритм заполнения массивов
		for time_c in self.xpoints:
			in_time_c = time_c
			while in_time_c > self.__period_packet:
				in_time_c = in_time_c - self.__period_packet
			if in_time_c > (self.__number * self.__period_pulse):
				self.Ipoints.append(0)
				self.Qpoints.append(0)
				self.Zpoints.append(0)
			else:
				while in_time_c > self.__period_pulse:
					in_time_c = in_time_c - self.__period_pulse
				if in_time_c > self.__length:
					self.Ipoints.append(0)
					self.Qpoints.append(0)
					self.Zpoints.append(0)
				else:
					self.Ipoints.append(self.garmonic(in_time_c, self.__frequency))
					self.Qpoints.append(self.garmonic(in_time_c, self.__frequency, 
													  phs = math.pi/2))
					self.Zpoints.append(self.Ipoints[-1] - self.Qpoints[-1])
	
	#Функция гармонического сигнала
	def garmonic(self, tm, freq, amp = 1.0, phs = 0.0):
		signal = amp * math.sin((2 * math.pi * freq * tm) + phs)
		return signal

	def send_test(self):
		print("I am working")

	def __time_step(self, start, step, end):
		rang = []
		point = start
		rang.append(point)
		while point < end:
			point += step
			rang.append(point)
		return rang
		

def main():
	print('Длина импульса: %f мкс и минимальная частота: %d МГц'\
	 % (length_pulse, frequency))
	radiopulse = Radiopulse(length_pulse, period_pulse, number_pulse,\
	 period_packet, frequency)
	print(radiopulse.Zpoints)			#Печать комплексных чисел в консоль
	make_plot(radiopulse.xpoints, radiopulse.Zpoints)
	return radiopulse.Zpoints, radiopulse.xpoints

def make_plot(xpoint, ypoint):
	fig = plot.figure()
	plot.plot(xpoint, ypoint)
	plot.show()

#Первичная инициализация программы
if __name__ == '__main__':
	main()
