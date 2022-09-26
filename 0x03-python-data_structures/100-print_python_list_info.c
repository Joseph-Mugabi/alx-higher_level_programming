#include <Python.h>

void print_python_list_info(PyObject *p)
{
	Pylistobject *list;
	Py_ssize size, idx;
	Python *object;
	struct _typeobject *type;

	if (strcmp(p->ob_type->tp_name, "list") == 0)
	{
		list = (PylistObject *)p;
		size = list->ob_base.ob_size;
		printf("[*] Size of the Python list = %ld\n", size);
		printf("[*] Allocated = %ld\n", list->allocated);
		for (idx = 0; idx < size; idx++)
		{
			object = list->ob_item[i];
			type = object->ob_type;
			printf("Element %ld: %s\n", idx, type->tp_name);
		}
	}
}
