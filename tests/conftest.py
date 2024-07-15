import pytest


@pytest.fixture(scope='session')
def xml_data(request):
  if request.param == 0:
    fname = 'tests/fixture/bigstitcher_0.xml'
  elif request.param == 1 :
    fname = 'tests/fixture/bigstitcher_1.xml'
  elif request.param == 2 :
    fname = 'tests/fixture/bigstitcher_2.xml'
  else:
    raise ValueError

  with open(fname) as fh:
    return fh.read()