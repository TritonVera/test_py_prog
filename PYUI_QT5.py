#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import sys
import Radiopulse
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
QDesktopWidget, QMainWindow, QLineEdit, QVBoxLayout, QFrame, QSizePolicy
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plot

class window(QMainWindow):
	def __init__(self):
		super().__init__()
		self.init_window()

	def init_window(self):
		self.statusBar().showMessage("I'm work")
		self.main_widget = widget()						#Создание центрального виджета
		self.setCentralWidget(self.main_widget)			#Установка в главное окно

		self.setGeometry(300, 300, 250, 150)			#Параметры размеров окна
		self.setWindowTitle('Проект Родина')


	def center(self):
		window_frame = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		window_frame.moveCenter(cp)
		self.move(window_frame.topLeft())


class widget(QWidget):
	def __init__(self):
		super().__init__()
		self.init_widget()

	def init_widget(self):
		#Строки ввода
		self.frequence_line = QLineEdit(self)
		self.length_line = QLineEdit(self)

		#Объекты отображения
		self.signal_plot = PlotCanvas(self, width = 5, height = 4)

		#Работа и размещение объекта отображения
		self.frequence_line.move(100,50)
		self.length_line.move(100,80)

		#Кнопки
		quit_button = QPushButton("Выход", self)
		quit_button.clicked.connect(QCoreApplication.instance().quit)
		work_button = QPushButton("Запуск", self)
		work_button.clicked.connect(self.Start_button)

		#Размещение кнопок на поле
		quit_button.move(100, 0)
		self.signal_plot.move(0, 0)

	def Start_button(self):
		y_points, x_points = Radiopulse.main()   #Извлечение координат точек сигнала
		self.signal_plot.plot(y_points)


class PlotCanvas(FigureCanvas):
    def __init__(self, parent = None, width = 5, height = 4, dpi = 100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def plot(self, y_point):
        ax = self.figure.add_subplot(111)
        ax.plot(y_point, 'r-')
        ax.set_title('PyQt Matplotlib Example')
        self.draw()



def main():
	app = QApplication(sys.argv)

	wnd = window()					#Генерация окна методами класса window
	wnd.show()						#Запуск показа окна
	wnd.center()					#Установка окна в центр
	#print("Ширина окна: %d, Отступ: %d" %(wnd.main_widget.width(), wnd.main_widget.width()\
	# - wnd.main_widget.quit_button.width()))

	sys.exit(app.exec_())

#Первичная инициализация программы
if __name__ == '__main__':
	main()