import pytest

#Reusability of use in multiple python files for mark fixtures
@pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
class BaseTest:
    pass