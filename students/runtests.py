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
    """Returns True if file has .py extention and starts with test_."""
    if (pathlib.Path(dir_name + '/' + file1).suffix == 
        '.py' and file1[0:5] == 'test_'):
        return True


if __name__ == '__main__':

    dir_name = input('Enter your path: ')  # noqa: WPS421, S322, E501
    if path_select(dir_name):
        sys.path.append(dir_name)
    elif (dir_name == ''):
        dir_name = os.getcwd()
    else:
        print('Enter valid path')  # noqa: T001
        sys.exit()
    file_list = os.listdir(dir_name)
    for file1 in file_list:
        if (file_select(dir_name, file1)):
            func_list = __import__(file1[0:-3])
            for counter in range(len(dir(func_list))):
                if (dir(func_list)[counter][0] != '_'):
                    funk = getattr(func_list, dir(func_list)[counter])
                    if (inspect.ismodule(funk)):
                        __import__(dir(func_list)[counter])
                    elif (inspect.isfunction(funk)):
                        try:
                            funk()
                        except AssertionError:
                            print('Test name: ' + dir(func_list)[counter] + ' with path: '
                                + os.getcwd() + '\\' + file1 + ' - fail\n'
                                + traceback.format_exc())  # noqa: T001
                        else:
                            print('Test name: ' + dir(func_list)[counter] + 
                                ' with path: ' + os.getcwd() + '\\' +
                                file1 + ' - ok')  # noqa: T001
        else:
            print(file1 + ' does not meet requirements')  # noqa: T001
