#include <Python.h>

void print_python_bytes(PyObject *p) {
    PyBytesObject *bytes = (PyBytesObject *)p;
    ssize_t size, i;
    char *string;

    printf("[.] bytes object info\n");
    printf("  size: %zd\n", Py_SIZE(bytes));
    printf("  trying string: %s\n", PyUnicode_AsUTF8AndSize(p, &size));
    printf("  first 10 bytes: ");
    if (size > 10)
        size = 10;
    string = PyBytes_AsString(p);
    for (i = 0; i < size; i++) {
        printf("%02x", (unsigned char)string[i]);
        if (i < size - 1)
            printf(" ");
    }
    printf("\n");
}

void print_python_list(PyObject *p) {
    PyListObject *list = (PyListObject *)p;
    ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", Py_SIZE(list));
    printf("[*] Allocated = %zd\n", list->allocated);
    for (i = 0; i < Py_SIZE(list); i++) {
        item = PyList_GetItem(p, i);
        printf("Element %zd: ", i);
        if (PyBytes_Check(item))
            print_python_bytes(item);
        else if (PyList_Check(item))
            print_python_list(item);
        else
            printf("%s\n", Py_TYPE(item)->tp_name);
    }
}

