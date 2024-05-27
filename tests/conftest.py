import pytest


@pytest.fixture(scope='session')
def xml_data(request):
  if request.param == 1:
    with open('tests/fixture/bigstitcher_0.xml') as fh:
      return fh.read()
  else:
    with open('tests/fixture/bigstitcher_1.xml') as fh:
      return fh.read()