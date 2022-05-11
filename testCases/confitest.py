from selenium import webdriver
import pytest
import unittest

@pytest.fixture()
def setup():
    driver=webdriver.Chrome("C:\Program Files (x86)\Driver\chromedriver")

    return setup
