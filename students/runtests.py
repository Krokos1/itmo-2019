# -*- coding: utf-8 -*-

"""Framework for tests."""
import importlib
import inspect
import os
import pathlib
import sys
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
    """Checks if dir is correct."""
    if path_select(dir_name):
        sys.path.append(dir_name)
    elif (dir_name == ''):
        dir_name = os.getcwd()
    else:
        print('Enter valid path')  # noqa: T001
        sys.exit()
    return dir_name


def prints(dirs, func_list):
    """Checing all given files and program outputs."""
    for counter in range(len(dirs)):  # noqa: WPS518
        if (dirs[counter][0] != '_'):
            funk = getattr(func_list, dirs[counter])
            if (inspect.ismodule(funk)):
                __import__(dirs[counter])  # noqa: WPS220, WPS421
            elif (inspect.isfunction(funk)):  # noqa: WPS220
                try:
                    funk()
                except AssertionError:
                    print(  # noqa: T001
                        '{0} {1} {2} {3}{4}{5} {6} {7}'.format(
                        'Test name:',
                        dirs[counter],
                        'with path:',
                        os.getcwd(),
                        '\\',
                        file1,
                        '- fail\n',
                        traceback.format_exc(),
                        ),
                    )
                else:
                    print('{0} {1} {2} {3}{4}{5} {6}'.format(  # noqa: T001
                        'Test name:',
                        dirs[counter],
                        'with path:',
                        os.getcwd(),
                        '\\',
                        file1,
                        '- ok',
                        ),
                    )


if __name__ == '__main__':
    dir_name = input('Enter your path: ')  # noqa: WPS421, S322, E501
    dir_name = get_dirname(dir_name)
    file_list = os.listdir(dir_name)
    for file1 in file_list:
        if (file_select(dir_name, file1)):
            func_list = importlib.import_module(file1[0:-3])
            dirs = dir(func_list)  # noqa: WPS421
            prints(dirs, func_list)
        else:
            print('{0} {1}'.format(  # noqa: T001
            file1,
            'does not meet requirements',
            ),
            )
