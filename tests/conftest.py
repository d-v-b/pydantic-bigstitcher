import pytest


@pytest.fixture(scope='session')
def demo_xml_0():
  with open('tests/fixture/bigstitcher_0.xml') as fh:
    return fh.read()

@pytest.fixture(scope='session')
def demo_xml_1():
  with open('tests/fixture/bigstitcher_1.xml') as fh:
    return fh.read()
