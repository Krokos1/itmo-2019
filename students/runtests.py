# -*- coding: utf-8 -*-

import os
import pathlib
import sys
import inspect
import traceback


def path_select(dir_name):
    """Returns True dir exists on a computer."""
    return os.path.isdir(dir_name)


def file_select(dir_name, file1):
    """Returns True if file meets requirements."""
    path1 = '{0} + {1} + {2}'.format(dir_name, '/', file1)
    if (pathlib.Path(path1).suffix == '.py'):
        if (file1[0:5] == 'test_'):
            return True


def get_dirname(dir_name):
    if path_select(dir_name):
        sys.path.append(dir_name)
    elif (dir_name == ''):
        dir_name = os.getcwd()
    else:
        print('Enter valid path')  # noqa: T001
        sys.exit()
    return dir_name


if __name__ == '__main__':
    dir_name = input('Enter your path: ')  # noqa: WPS421, S322, E501
    dir_name = get_dirname(dir_name)
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
                            print('{0} {1} {2} {3}{4}{5} {6} {7}'.format(
                                'Test name:', dir(func_list)[counter],
                                'with path:', os.getcwd(), '\\',
                                file1, '- fail\n',
                                traceback.format_exc()))  # noqa: T001
                        else:
                            print('{0} {1} {2} {3}{4}{5} {6}'.format(
                                'Test name:',
                                dir(func_list)[counter],
                                'with path:', os.getcwd(),
                                '\\', file1, '- ok'))  # noqa: T001
        else:
            print('{0} {1}'.format(file1,
            'does not meet requirements'))  # noqa: T001
