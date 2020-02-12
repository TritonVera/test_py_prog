#define PY_SSIZE_T_CLEAN
#include <Python.h>

PyObject *p_name, *p_module, *p_dict, *p_func;
PyObject *python_start() {

	Py_SetProgramName("window_python");
	Py_Initialize();

	do {
		// Загрузка модуля sys
        PyObject *sys = PyImport_ImportModule("sys");
        PyObject *sys_path = PyObject_GetAttrString(sys, "path");
        // Путь до наших исходников Python
        PyObject *folder_path = PyUnicode_FromString((const char*) ".");
        PyList_Append(sys_path, folder_path);

		//Перевод С строки в python unicode строку
		p_name = PyUnicode_FromString("window_python");
		if (!p_name) {
			break;
		}

		//Импорт python-файла и проверка на ошибки
		p_module = PyImport_Import(p_name);
		if (!p_module) {
			break;
		}

		//Извлечение словаря объектов
		p_dict = PyModule_GetDict(p_module);
		if (!p_dict) {
			break;
		}

		//Извлечение функции main
		p_func = PyDict_GetItemString(p_dict, "main");
		if (!p_func) {
			break;
		}

		Py_XDECREF(sys);
		Py_XDECREF(sys_path);
		Py_XDECREF(folder_path);
		return p_func;
	} while(0);

	PyErr_Print();			//Печать ошибки в случае неудачи
	return 0;
}

void python_clear() {
	//Возврат ресурсов системе
	Py_XDECREF(p_dict);
	Py_XDECREF(p_module);
	Py_XDECREF(p_name);

	//Завершение работы интерпретатора
	Py_Finalize();
}

int main(int argc, char *argv[]) {
	python_start();
	if (!python_start()) {
		return -1;
	}
	PyObject_CallObject(p_func, NULL);
	python_clear();
	return 0;
}