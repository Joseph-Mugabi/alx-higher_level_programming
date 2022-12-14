#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
/**
 *  print_python_bytes - orints bytes of an objects
 *  @p: object
 */
void print_python_bytes(PyObject *p)
{
	long int size;
	int j;
	char *str_2_try = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}
	PyBytes_AsStringAndSize(p, &str_2_try, &size);
	printf("  size: %li\n", size);
	printf("  trying string: %s\n", str_2_try);
	if (size < 10)
		printf("  first %li bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (j = 0; j <= size && j < 10; j++)
		printf(" %02hhx", str_2_try[j]);
	printf("\n");
}
/**
 * print_python_list - prints the list of objects
 * @p: object
 *
 */
void print_python_list(PyObject *p)
{
	long int size = PyList_Size(p);
	int j;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", list->allocated);
	for (j = 0; j < size; j++)
	{
		type = (list->ob_item[j])->ob_type->tp_name;
		printf("Element %i: %s\n", j, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(list->ob_item[j]);
	}
}
