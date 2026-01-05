import pytest

@pytest.fixture(scope='function')
def functest():
    def ret_test():
        print('a')

    return ret_test
