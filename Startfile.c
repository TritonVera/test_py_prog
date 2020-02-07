#define PY_SSIZE_T_CLEAN
#include <Python.h>

PyObject *p_name, *p_module, *p_dict;
PyObject *python_start() {

	Py_Initialize();

	/*do {
		// Загрузка модуля sys
        PyObject *sys = PyImport_ImportModule("sys");
        PyObject *sys_path = PyObject_GetAttrString(sys, "path");
        // Путь до наших исходников Python
        PyObject *folder_path = PyUnicode_FromString((const char*) "./src/python");
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

		Py_XDECREF(sys);
		Py_XDECREF(sys_path);
		Py_XDECREF(folder_path);
		return p_dict;
	} while(0);

	PyErr_Print();			//Печать ошибки в случае неудачи
	return 0;*/
}

void python_clear() {
	//Возврат ресурсов системе
	Py_XDECREF(p_dict);
	Py_XDECREF(p_module);
	Py_XDECREF(p_name);

	//Завершение работы интерпретатора
	Py_Finalize();
}

int main() {
	FILE *p_file = fopen("window_python.py", "r");
	python_start();
	PyRun_SimpleFile(p_file, "window_python");
	///if (!python_start()) {
	///	return -1;
	///}
	python_clear();
	return 0;
}