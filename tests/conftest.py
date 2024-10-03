import pytest


@pytest.fixture(scope="session")
def bigstitcher_xml(request: pytest.FixtureRequest) -> str:
    fname = f"tests/fixture/bigstitcher_{request.param}.xml"

    with open(fname) as fh:
        return fh.read()
