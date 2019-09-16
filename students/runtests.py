# -*- coding: utf-8 -*-

import os
import pathlib
import sys
import traceback
import inspect


def path_select(dir_name):
    """Returns True dir exists on a computer."""
    return os.path.isdir(dir_name)


def file_select(dir_name, file1):
    """Returns 'True' if file has .py extention and starts with test_."""
    if (pathlib.Path(dir_name + '/' + file1).suffix == 
        '.py' and file1[0:5] == 'test_'):
        return True


if __name__ == '__main__':
    while True:
        dir_name = input('Enter your path: ')  # noqa: WPS421, S322, E501
        print(dir_name)
        if path_select(dir_name):
            sys.path.append(dir_name)
            break
        elif (dir_name == ''):
            dir_name = os.getcwd()
            break
        else:
            print('Enter valid path')
    file_list = os.listdir(dir_name)
    for file1 in file_list:
        if (file_select(dir_name, file1)):
            func_list = __import__(file1[0:-3])
            for i in range(len(dir(func_list))):
                if (dir(func_list)[i][0] != '_'):
                    f = getattr(func_list, dir(func_list)[i])
                    if (inspect.ismodule(f)):
                        __import__(dir(func_list)[i])
                    elif (inspect.isfunction(f)):
                        try:
                            f()
                        except AssertionError:
                            print('Test name: ' + dir(func_list)[i] + ' with path: ' 
                                + os.getcwd() + '\\' + file + ' - fail')  # noqa: T001
                            exc_type, exc_value, exc_traceback = sys.exc_info()
                            traceback.print_exception(exc_type, exc_value, exc_traceback,
                             limit=2, file=sys.stdout)
                        else:
                            print('Test name: ' + dir(func_list)[i] + 
                                ' with path: ' + os.getcwd() + '\\' +file1 + ' - ok')  # noqa: T001
        else:
            print(file1 + ' does not meet requirements')  # noqa: T001
