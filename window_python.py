#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from tkinter import Tk, Frame, Label, BOTH, TOP, LEFT
import Radiopulse

#Создание нового класса похожего на Frame
class App_frame(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent, background = "black")		#Инициализация главного Frame
		self.parent = parent									#Присвоение методу parent главного фрейма переданного значения parent
		self.parent.title("Hello")								#Установка имени главного окна
		self.center_window()									#Вызов функции центрирования окна
		self.pack(fill = BOTH, expand = 1)						#Отображение и заполнение главного окна фреймом

	def center_window(self):
		width = 300												#Установка ширины окна
		height = 500											#Установка высоты окна
		width_screen = self.parent.winfo_screenwidth()			#Запрос ширины экрана
		height_screen = self.parent.winfo_screenheight()		#Запрос высоты экрана
		padding_width = (width_screen - width)/2				#Расчёт отступа слева
		padding_height = (height_screen - height)/2				#Расчёт отступа сверху
		self.parent.geometry('%dx%d+%d+%d' \
			% (width, height, padding_width, padding_height))	#Установка положения и размеров окна
		self.parent.minsize(250,250)							#Установка минимального размера окна
		self.parent.maxsize(width_screen - 50,\
		 height_screen - 50)									#Установка максимального размера окна

#Создание класса кнопки из Label (для стилизовки)
class App_button(Label):
	#Инициализация главного Label
	def __init__(self, parent, txt_btn, cmd_btn = "None"):
		Label.__init__(self, parent, text = txt_btn,\
		  fg = 'blue')
		self.parent = parent									#Сохранение ссылки на родителя
		self.configure(bg = self.parent.cget('bg'))				#Установка одинакового фона ребенка и родителя
		self.command = cmd_btn

		#Реализация обработчика команд
		self.bind("<ButtonPress-1>", self.change_color)			#Вызов обработчика нажатия кнопки
		self.bind("<B1-Motion>", self.undo_color)				#Вызов обработчика движения мыши
		self.bind("<ButtonRelease-1>", self.run_cmd)			#Вызов обработчика отпускания кнопки

	#Обработка нажатия кнопки
	def change_color(self, event):
		self.configure(fg = 'red')								#Изменение цвета кнопки при нажатии на нее

	#Обработка выхода курсора из зоны кнопки
	def undo_color(self, event):
		#Проверка на нахождение курсора мыши на кнопке
		if (event.x > 0 and event.x < self.winfo_width()) \
		and (event.y > 0 and event.y < self.winfo_height()):
			self.configure(fg = 'red')							#Изменение цвета кнопки при появлении курсора
		else:
			self.configure(fg = 'blue')							#Изменение цвета кнопки при уходе курсора

	#Обработка отпускания кнопки
	def run_cmd(self, event):
		#Проверка на нахождение курсора мыши на кнопке
		if (event.x > 0 and event.x < self.winfo_width()) \
		and (event.y > 0 and event.y < self.winfo_height()):
			exec(self.command)									#Выполнение команды
			self.configure(fg = 'blue')
		else:
			self.configure(fg = 'blue')							#Изменение цвета кнопки при отпускании

#Конфигурация главного окна
def make_window(main_frame):
	top_frame = Frame(main_frame, bg = 'white')					#Создание верхнего фрейма
	top_frame.pack(side = TOP, fill = BOTH, expand = 1)			#Размещение верхнего фрейма в главном
	middle_frame = Frame(main_frame, bg = 'blue')				#Создание среднего фрейма
	middle_frame.pack(side = TOP, fill = BOTH, expand = 1)		#Размещение среднего фрейма в главном
	bottom_frame = Frame(main_frame, bg = 'red')				#Создание нижнего фрейма
	bottom_frame.pack(side = TOP, fill = BOTH, expand = 1)		#Размещение нижнего фрейма в главном
	quit_button = App_button(top_frame,\
	 "Выход", "quit()")											#Создание кнопки
	quit_button.pack(side = LEFT, padx = 10, pady = 10)			#Размещение кнопки в окне
	test_button = App_button(top_frame,\
		"Тест", "Radiopulse.main()")
	test_button.pack(side = LEFT, padx = 10, pady = 10)

#Функция создания главного окна
def main():
	main_window = Tk()											#Создание окна
	main_frame = App_frame(main_window)							#Создание главного фрейма внутри главного окна
	make_window(main_frame)										#Ссылка на метод создания окна
	main_window.mainloop()										#Основной цикл

#Первичная инициализация программы
if __name__ == '__main__':
	main()
