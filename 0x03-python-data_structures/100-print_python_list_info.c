#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
        PyObject *obj;
	PyListObject *List_obj;
	int list_size, i = 0;
	/* print size of the list and allocations */
        list_size = PyList_Size(p);
        list_obj = (PyListObject *)p;
        printf("[*] Size of the Python List = %d\n", list_size);
        printf("[*] Allocated = %d\n", (int)(list_obj->allocated));
	/* print elements of tbe list */
        while (i < list_size)
        {
                obj = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i,py_TYPE(obj)->tp_name);
                i++;
        }
}
