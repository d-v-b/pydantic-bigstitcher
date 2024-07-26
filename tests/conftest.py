import pytest


@pytest.fixture(scope='session')
def xml_data(request) -> str:
  fname = f'tests/fixture/bigstitcher_{request.param}.xml'

  with open(fname) as fh:
    return fh.read()