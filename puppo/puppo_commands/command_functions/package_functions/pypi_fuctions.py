"""Use this file for packaging up PYPI packages.

This file contains functions used for packaging and uploading python packages
to the PYPI store.
"""
from os import getcwd

from puppo.decorator_functions.package_decorator import packaging_handler
from puppo.utility_functions.terminal_functions import run_command


def package_application(testpypi, verbose):
    """Use this function to package the application.

    This function is the root function, which when called, while create the
    distribution and upload it to the PYPI store.

    :param testpypi: boolean value saying whether or not to send to test PYPI.
    :param verbose: used to decide whether or not to print additional
                    information.
    """
    __create_package(verbose)
    __upload_package(testpypi, verbose)


@packaging_handler
def __create_package(verbose):
    """Use this function to create the distributed package.

    :param verbose: used to decide whether or not to print additional
                    information.
    """
    base_command = ['{}/setup.py'.format(getcwd()), 'sdist']
    try:
        result = run_command(['python3'] + base_command)
    except Exception:
        result = run_command(['python'] + base_command)
    print(result)


def __upload_package(testpypi, verbose):
    """Use this function to upload the distribution package to the PYPI store.

    :param testpypi: boolean value saying whether or not to send to test PYPI.
    :param verbose: used to decide whether or not to print additional
                    information.
    """
    base_command = ['twine', 'upload']
    dist_location = ['{}/dist/*'.format(getcwd())]
    if testpypi:
        try:
            result = run_command(
                base_command + ['--repository', 'testpypi'] + dist_location)
        except Exception:
            result = run_command(
                base_command +
                ['--repository-url' 'https://test.pypi.org/legacy/'] +
                dist_location
                )
    else:
        try:
            result = run_command(base_command + dist_location)
        except Exception:
            result = run_command(
                base_command +
                ['--repository-url' 'https://test.pypi.org/legacy/'] +
                dist_location
                )
    print(result)