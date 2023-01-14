import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    return driver


## it is hook for adding environment info to html report
def pytest_configure(config):
    config._metadata['projectname'] = 'nopcommerce1'
    config._metadata['Tester'] = 'abhay'

