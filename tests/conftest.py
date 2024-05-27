import pytest
@pytest.fixture
def demo_xml_0(scope='session'):
  with open('tests/fixture/bigstitcher_0.xml', mode='r') as fh:
    return fh.read()

@pytest.fixture(scope='session')
def demo_xml_1():
  with open('tests/fixture/bigstitcher_1.xml', mode='r') as fh:
    return fh.read()