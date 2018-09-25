from cffi import FFI
import os, sys


def compile_C():
    # Check that we have a build directory
    if not os.path.isdir('build'):
        os.mkdir('build')

    # Compile the C code into an shared object library
    linking = '-lgslcblas -lgsl -ggdb -fopenmp'
    optimization = '-O3'
    warnings = '-Wall -Werror -W -Wconversion -Wshadow'
    os.system('gcc -shared -o build/libadd.so -fPIC include/add.h src/add.c {} {} {}'.format(linking, optimization, warnings))

    return

def cffi_setup():
    ffibuilder = FFI()

    # Tell cffi which functions to add to the lib
    ffibuilder.cdef("""
        double add(double x, double y);
        double sum_array(double arr[], int length);
        double do_things(double arr[], int length);
    """)

    # Tell cffi, 
    # 1. What to name library
    # 2. What header files?
    # 3. What library to link (This will linke build/libadd.so)
    ffibuilder.set_source("_add",
    """
        #include "include/add.h"
    """,
        libraries=['{}/build/add'.format(os.getcwd())])

    return ffibuilder



if __name__ == "__main__":
    # First compile the C code
    compile_C()

    # Set up cffi stuff
    ffibuilder = cffi_setup()

    # Compile the library
    ffibuilder.compile(verbose=True)
